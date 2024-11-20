<template>
    <div>
        <h1>내 주변 은행 찾기</h1>
    <div id="map" style="width:500px;height:400px;"></div>
    </div>
</template>

<script setup>
import { onMounted } from "vue";
import axios from "axios";
import { useFinStore } from '@/stores/counter';
const store = useFinStore()

// 환경 변수에서 API 키를 미리 가져옵니다.
const kakaoApiKey = import.meta.env.VITE_KAKAO_API_KEY;

onMounted(() => {
  // Kakao Maps API 스크립트를 동적으로 추가
  const kakaoScript = document.createElement('script');
  kakaoScript.type = "text/javascript"
  kakaoScript.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoApiKey}&autoload=false&libraries=services,clusterer,drawing`;
  kakaoScript.async = true;

  // head에 script 태그 추가
  document.head.appendChild(kakaoScript);

  // 스크립트가 로드되면 지도 초기화 함수 호출
  kakaoScript.onload = () => {
    // console.log('Kakao Maps 스크립트 로드 성공')
    if (window.kakao && window.kakao.maps) {
      console.log('맵 초기화')
      initializeMap(); // API가 로드된 후 지도 초기화
    } else {
      console.error("Kakao Maps API가 로드되지 않았습니다.");
    }
  };

  kakaoScript.onerror = () => {
    console.error("Kakao Maps API 스크립트 로드에 실패했습니다.");
  };
  
  console.log('태그 추가')
});

function initializeMap() {
  console.log('initializeMap 함수 호출')
  kakao.maps.load(function(){
    const container = document.getElementById("map");
    const options = {
      center: new kakao.maps.LatLng(37.501336, 127.039643), // 초기 지도 중심 좌표
      level: 3, // 초기 확대 레벨
    };
    console.log('지도 생성 전')
    // Kakao 지도 생성
    const map = new kakao.maps.Map(container, options);
    console.log('지도 생성 끝')

    // 은행 찾기
    searchBanks(map);
  
    kakao.maps.event.addListener(map, "idle", () => {
      searchBanks(map); // 보이는 화면 중심 기준으로 검색
    });
  })
}

function searchBanks(map) {
  const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  const ps = new kakao.maps.services.Places();

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
    console.log(place.place_name)
    createRecommend(place.place_name)
  });
}



// 은행 상품 받아오기
const createRecommend = function (bank) {
    axios({
        method:'get',
        url:`${store.API_URL}/financial_products/get_deposit/`,
        params: {
          bank:bank
        }
    })
    .then((response) => {
      console.log(response)
    })
    .catch((err) => {
      console.log('error')
    })
}







</script>

<style scoped>
#map {
  width: 100%;
  height: 400px;
  max-width: 500px;
  margin: auto;
}
</style>