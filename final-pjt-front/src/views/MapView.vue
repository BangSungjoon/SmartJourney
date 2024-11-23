<template>
    <div>
      <!-- 소개 섹션 -->
      <section class="hero-section">
        <div class="hero-content">
          <h1 class="hero-title">내 주변 은행을 찾아보세요</h1>
          <p class="hero-description">
            지금 가장 가까운 은행과 예금 및 적금 상품을 확인하고<br />
            나만의 금융 플랜을 세워보세요.
          </p>
        </div>
      </section>
  
      <!-- 지도와 상품 추천 섹션 -->
      <div class="main-content">
        <div class="container">
          <h1 class="title">내 주변 은행 찾기</h1>
          <div id="map"></div>
  
          <!-- 은행 상품 정보 -->
          <div class="bank-info" v-if="selectedBank">
            <h2 class="bank-title">{{ selectedBank }}의 상품입니다</h2>
  
            <!-- 예금 상품 -->
            <div class="product-section">
              <h3>예금 상품</h3>
              <div class="product-grid">
                <div
                  v-for="(product, index) in depositProducts"
                  :key="index"
                  class="product-item"
                >
                  <span class="product-badge">{{ getAlphabet(index) }}</span>
                  <div class="product-details">
                    <p class="product-name">{{ product.fin_prdt_nm }}</p>
                    <p class="product-desc">{{ product.kor_co_nm }}</p>
                    <p class="product-rate">
                      이율: {{ product.intr_rate }}% (우대: {{ product.intr_rate2 }}%)
                    </p>
                    <p class="product-term">기간: {{ product.save_trm }}개월</p>
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
                  <span class="product-badge">{{ getAlphabet(index + depositProducts.length) }}</span>
                  <div class="product-details">
                    <p class="product-name">{{ product.fin_prdt_nm }}</p>
                    <p class="product-desc">{{ product.kor_co_nm }}</p>
                    <p class="product-rate">
                      이율: {{ product.intr_rate }}% (우대: {{ product.intr_rate2 }}%)
                    </p>
                    <p class="product-term">기간: {{ product.save_trm }}개월</p>
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

// 상태 관리
const selectedBank = ref(null); // 선택된 은행
const bankProducts = ref([]); // 은행 상품 목록
const depositProducts = ref([]); // 예금 상품 목록
const savingsProducts = ref([]); // 적금 상품 목록

onMounted(() => {
  const kakaoScript = document.createElement("script");
  kakaoScript.type = "text/javascript";
  kakaoScript.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoApiKey}&autoload=false&libraries=services,clusterer,drawing`;
  kakaoScript.async = true;

  // Kakao Maps 스크립트 로드
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

function initializeMap() {
  kakao.maps.load(() => {
    const container = document.getElementById("map");
    const options = {
      center: new kakao.maps.LatLng(37.501336, 127.039643),
      level: 3,
    };
    const map = new kakao.maps.Map(container, options);

    searchBanks(map);

    kakao.maps.event.addListener(map, "idle", () => {
      searchBanks(map);
    });
  });
}

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
      radius: 5000,
    }
  );
}

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

    // 은행 이름 저장
    selectedBank.value = place.place_name;

    // 은행 상품 정보 요청
    fetchBankProducts(place.place_name);
  });
}

function fetchBankProducts(bankName) {
  axios
    .get(`${store.API_URL}/financial_products/get_deposit/`, {
      params: { bank: bankName },
    })
    .then((response) => {
      const data = response.data;

      if (!data.length) {
        setDefaultProducts(); // 디폴트 데이터로 설정
        return;
      }

      // 상품 분류
      depositProducts.value = data.filter((product) => product.type === "예금");
      savingsProducts.value = data.filter((product) => product.type === "적금");
    })
    .catch((error) => {
      console.error("은행 상품 정보 요청 실패:", error);
      setDefaultProducts(); // 요청 실패 시 디폴트 데이터로 설정
    });
}

function setDefaultProducts() {
  depositProducts.value = [
    {
      fin_prdt_nm: "기본 예금 상품 A",
      kor_co_nm: "은행 A",
      intr_rate: 2.5,
      intr_rate2: 3.0,
      save_trm: 12,
    },
    {
      fin_prdt_nm: "기본 예금 상품 B",
      kor_co_nm: "은행 B",
      intr_rate: 2.0,
      intr_rate2: 2.8,
      save_trm: 24,
    },
    {
      fin_prdt_nm: "기본 예금 상품 C",
      kor_co_nm: "은행 C",
      intr_rate: 1.8,
      intr_rate2: 2.3,
      save_trm: 36,
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
    {
      fin_prdt_nm: "기본 적금 상품 B",
      kor_co_nm: "은행 B",
      intr_rate: 2.8,
      intr_rate2: 3.2,
      save_trm: 24,
    },
    {
      fin_prdt_nm: "기본 적금 상품 C",
      kor_co_nm: "은행 C",
      intr_rate: 2.5,
      intr_rate2: 3.0,
      save_trm: 36,
    },
  ];
}
</script>


<style scoped>
body {
  margin: 0;
  font-family: 'Noto Sans KR', sans-serif;
  overflow-x: hidden;
  
}

/* Hero Section */
.hero-section {
  height: 100vh;
  background: url('@/assets/images/portfolio/port1.jpg') no-repeat center center/cover;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  position: relative;
}

.hero-content {
  max-width: 800px;
}

.hero-title {
  font-size: 2.5rem;
  margin-bottom: 20px;
  font-weight: bold;
}

.hero-description {
  font-size: 1.2rem;
  line-height: 1.6;
}

/* Main Content */
.main-content {
  padding: 20px;
  background-color: #f9f9f9;
}

/* 지도 */
#map {
  width: 100%;
  height: 500px;
  border: 1px solid #ccc;
  margin: 20px 0;
}

/* 상품 섹션 */
.bank-info {
  margin-top: 20px;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-section {
  margin-bottom: 40px;
}

.product-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}
</style>


  