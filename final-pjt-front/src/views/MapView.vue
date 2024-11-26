<template>
  <div>
    <div class="store-container">
      <!-- 상단 섹션 -->
      <section class="store-header slide-top">
        <h1 class="store-title">당신과 가까이에 있는 은행을 찾아보세요</h1>
        <p class="store-subtitle">지금 가장 가까운 은행과 예금 및 적금 상품을 확인하고<br />
          나만의 금융 플랜을 세워보세요.</p>
      </section>

      <!-- 이미지 섹션 -->
      <section class="store-image">
        <img src="@/assets/images/portfolio/port1.jpg" alt="Store Image" class="store-main-image" />
      </section>

      <!-- 스크롤 다운 버튼 추가 -->
      <div class="scroll-down-btn" @click="scrollToMap">
        <span class="arrow"></span>
      </div>
    </div>
  
    <div class="main-layout">
      <!-- 지도 -->
      <div id="map" class="map-container"></div>

      <!-- 리스트 (초기에는 빈 공간) -->
      <div class="bank-info">
        <div v-if="selectedBank">
          <h2 class="bank-title"><span class="highlight">{{ selectedBank }}</span>의 상품입니다</h2>
          

          <!-- 상품이 없을 경우 -->
          <div v-if="!depositProducts.length && !savingsProducts.length">
            <p class="no-data-message">상품을 조회할 수 없습니다.</p>
          </div>
          <div v-else>
          <!-- 상품이 있는 경우 -->
          <!-- 예금 상품 -->
          <div class="product-section">
            <h3>예금 상품</h3>
            <div class="product-grid ">
              <div
                v-for="(product, index) in depositProducts"
                :key="index"
                class="product-item"
              >
                <!-- <span class="product-badge">{{ getAlphabet(index) }}</span> -->
                <div class="product-details">
                  <p class="product-name">{{ product.fin_prdt_nm }}</p>
                  <!-- <p class="product-desc">{{ product.kor_co_nm }}</p> -->
                  <div v-for="(option, index) in product.depositoptions_set">
                    <p class="product-rate">
                      이율: {{ option.intr_rate }}% (우대: {{ option.intr_rate2 }}%) / 기간: {{ option.save_trm }}개월
                    </p>
                    <!-- <p class="product-term">기간: {{ option.save_trm }}개월</p> -->
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 적금 상품 -->
          <div class="product-section">
            <h3>적금 상품</h3>
            <div class="product-grid">
              <div
                v-for="(product, index) in savingsProducts"
                :key="index"
                class="product-item"
              >
                <!-- <span class="product-badge">{{ getAlphabet(index + depositProducts.length) }}</span> -->
                <div class="product-details">
                  <p class="product-name">{{ product.fin_prdt_nm }}</p>
                  <!-- <p class="product-desc">{{ product.kor_co_nm }}</p> -->
                  <div v-for="(option, index) in product.savingoptions_set">
                    <p class="product-rate">
                      이율: {{ option.intr_rate }}% (우대: {{ option.intr_rate2 }}%) / 기간: {{ option.save_trm }}개월
                    </p>
                    <!-- <p class="product-term">기간: {{ option.save_trm }}개월</p> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>
  

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useFinStore } from "@/stores/counter";

const store = useFinStore();
const kakaoApiKey = import.meta.env.VITE_KAKAO_API_KEY;

// Vue 상태 관리
const selectedBank = ref(""); // 선택된 은행 이름
const depositProducts = ref([]); // 예금 상품 목록
const savingsProducts = ref([]); // 적금 상품 목록
const bankInfos = ref([]); // 선택된 은행의 상품 정보

// 알파벳 반환 함수
function getAlphabet(index) {
  return String.fromCharCode(65 + index); // A, B, C 등 반환
}

// Kakao Maps API 초기화
onMounted(() => {
  const kakaoScript = document.createElement("script");
  kakaoScript.type = "text/javascript";
  kakaoScript.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoApiKey}&autoload=false&libraries=services,clusterer,drawing`;
  kakaoScript.async = true;

  kakaoScript.onload = () => {
    if (window.kakao && window.kakao.maps) {
      initializeMap();
    } else {
      console.error("Kakao Maps API가 로드되지 않았습니다.");
    }
  };
  kakaoScript.onerror = () => {
    console.error("Kakao Maps API 스크립트 로드 실패");
  };

  document.head.appendChild(kakaoScript);
});

// 지도 초기화
function initializeMap() {
  kakao.maps.load(() => {
    const container = document.getElementById("map");
    const options = {
      center: new kakao.maps.LatLng(37.501336, 127.039643),
      level: 3,
    };
    const map = new kakao.maps.Map(container, options);

    // 초기 검색
    searchBanks(map);

    // 지도 이동 시 재검색
    kakao.maps.event.addListener(map, "idle", () => {
      searchBanks(map);
    });
  });
}

// 은행 검색
function searchBanks(map) {
  const ps = new kakao.maps.services.Places();
  const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

  ps.keywordSearch(
    "은행",
    (data, status) => {
      if (status === kakao.maps.services.Status.OK) {
        data.forEach((place) => {
          displayMarker(map, place, infowindow);
        });
      } else {
        console.error("장소 검색 실패:", status);
      }
    },
    {
      location: map.getCenter(),
      radius: 5000, // 반경 5km
    }
  );
}

// 마커 표시 및 클릭 이벤트 등록
function displayMarker(map, place, infowindow) {
  const marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  kakao.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(
      `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`
    );
    infowindow.open(map, marker);

    // 선택된 은행 설정
    selectedBank.value = place.place_name;

    // 은행 상품 정보 가져오기
    fetchBankProducts(place.place_name);
  });
}

// 은행 상품 정보 요청
function fetchBankProducts(bankName) {
   // bankName 변환 로직
   if (bankName.startsWith("KB국민은행")) {
    bankName = "국민은행";
  } else if (bankName.startsWith("IBK")) {
    bankName = "중소기업은행";
  } else if (bankName.startsWith("NH농협")) {
    bankName = "농협은행";
  }
  // console.log(bankName)
  Promise.all([
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/get_map_deposit/`,
            params: {
                bank:bankName
            }
        }),
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/get_map_savings/`,
            params: {
                bank:bankName
            }
        })
    ])
    .then(([depositResponse, savingsResponse]) => {
        // console.log("Deposit Data:", depositResponse.data)
        console.log("Savings Data:", savingsResponse.data)
        depositProducts.value = [...depositResponse.data]
        savingsProducts.value = [...savingsResponse.data]
        // bankInfos.value = [
        // ...depositResponse.data, // 예금 데이터
        // ...savingsResponse.data, // 적금 데이터
        // ];
        // console.log(ban)
    }) 
    .catch((error) => {
      console.error("은행 상품 정보 요청 실패:", error);
      setDefaultProducts(); // 요청 실패 시 기본값 설정
    });
}

// 기본 상품 설정
function setDefaultProducts() {
  depositProducts.value = [
    {
      fin_prdt_nm: "기본 예금 상품 A",
      kor_co_nm: "은행 A",
      intr_rate: 2.5,
      intr_rate2: 3.0,
      save_trm: 12,
    },
  ];

  savingsProducts.value = [
    {
      fin_prdt_nm: "기본 적금 상품 A",
      kor_co_nm: "은행 A",
      intr_rate: 3.0,
      intr_rate2: 3.5,
      save_trm: 12,
    },
  ];
}

// 스크롤 함수 추가
const scrollToMap = () => {
  const mapElement = document.querySelector('.main-layout')
  mapElement.scrollIntoView({ behavior: 'smooth' })
}
</script>


<style scoped>
/* 기본 body 설정 */
body {
  margin: 0;
  font-family: 'Noto Sans KR', sans-serif;
  color: #333;
  background-color: #f9f9f9;
}

/* 스토어 컨테이너 */
.store-container {
  position: relative;
  text-align: center;
  padding: 20px;
  background-color: #fff;
  height: 100vh; /* 배너 높이를 뷰포트 높이에 맞춤 */
}

/* 상단 섹션 */
.store-header {
  padding: 3%;
}

.store-title {
  font-size: 3rem; /* 제목 크기 조정 */
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
  font-family: 'Noto Sans KR', sans-serif;
}

.store-subtitle {
  font-size: 1rem; /* 부제목 크기 조정 */
  margin-top: 10px;
  line-height: 1.5;
  color: #666;
}

/* 이미지 섹션 */
.store-image {
  margin: auto; /*이미지와 텍스트 간 간격 */
  width: 100%;
  max-width: 1200px; /* 최대 너비 제한 */
  padding: 0 20px; /* 화면 양쪽 여백 추가 */
  box-sizing: border-box; /* 패딩 포함 크기 조정 */
}

.store-main-image {
  width: 100%; /* 이미지가 컨테이너에 맞게 조정 */
  height: auto; /* 비율 유지 */
  max-height: 500px; /* 최대 높이 제한 */
  /* border-radius: 10px; 약간의 둥근 테두리 */
  /* box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 그림자 효과 */
}

/* 전체 레이아웃 */
.main-layout {
  display: flex;
  width: 100%;
  height: 100vh; /* 화면 전체 높이 */
  overflow: hidden;
}

/* 지도 영역 */
.map-container {
  flex: 3; /* 3/5 공간 차지 */
  height: 100%;
  border-right: 1px solid #ddd; /* 경계선 */
}

/* 리스트 영역 */
.bank-info {
  flex: 2; /* 2/5 공간 차지 */
  height: 100%;
  background-color: white;
  padding: 20px;
  overflow-y: auto; /* 스크롤 가능 */
  box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  font-family: 'Noto Sans KR', sans-serif;
}

/* 상품 섹션 */
.product-section {
  margin-bottom: 40px;
}

.product-name {
  font-weight: bold;
}

.product-section h3 {
  text-align: center;
  padding-top: 20px;
}

.product-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.product-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 15px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.product-badge {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  background-color: #007bff;
  color: white;
  border-radius: 50%;
  font-weight: bold;
  /* text-align: center; */
}

.product-details {
  flex: 1;
  text-align: center;
}

.highlight {
  color: #ffd700; /* 강조 텍스트 색상 */
}

  /* 애니메이션 스타일 */
  .slide-top {
    animation: slide-top 0.8s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
  }
  
  @keyframes slide-top {
    0% {
      transform: translateY(50px);
      opacity: 0;
    }
    100% {
      transform: translateY(0);
      opacity: 1;
    }
  }

  .slide-in-blurred-top {
	-webkit-animation: slide-in-blurred-top 1s cubic-bezier(0.230, 1.000, 0.320, 1.000) both;
	        animation: slide-in-blurred-top 1s cubic-bezier(0.230, 1.000, 0.320, 1.000) both;
}

 @-webkit-keyframes slide-in-blurred-top {
  0% {
    -webkit-transform: translateY(-1000px) scaleY(2.5) scaleX(0.2);
            transform: translateY(-1000px) scaleY(2.5) scaleX(0.2);
    -webkit-transform-origin: 50% 0%;
            transform-origin: 50% 0%;
    -webkit-filter: blur(40px);
            filter: blur(40px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0) scaleY(1) scaleX(1);
            transform: translateY(0) scaleY(1) scaleX(1);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    -webkit-filter: blur(0);
            filter: blur(0);
    opacity: 1;
  }
}

/* 스크롤 다운 버튼 스타일 */
.scroll-down-btn {
  position: absolute;
  bottom: 100px;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: white;
  /* box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); */
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}

.scroll-down-btn:hover {
  transform: translateX(-50%) translateY(-5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

.arrow {
  border: solid #333;
  border-width: 0 2px 2px 0;
  display: inline-block;
  padding: 4px;
  transform: rotate(45deg);
  margin-top: -5px;
}

/* 애니메이션 추가 */
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

.scroll-down-btn {
  animation: bounce 2s infinite;
}

</style>


  