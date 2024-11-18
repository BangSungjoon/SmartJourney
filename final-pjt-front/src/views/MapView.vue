<template>
    <div>
        <h1>내 주변 은행 찾기</h1>
    <div id="map" style="width:500px;height:400px;"></div>
    </div>
</template>

<script setup>
import { onMounted } from "vue";

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    kakao.maps.load(() => {
      initializeMap(); // API가 로드된 후 지도 초기화
    });
  } else {
    console.error("Kakao Maps API가 로드되지 않았습니다.");
  }
});

function initializeMap() {
  const container = document.getElementById("map");
  if (!container) {
    console.error("지도 컨테이너를 찾을 수 없습니다.");
    return;
  }

  const options = {
    center: new kakao.maps.LatLng(37.501336, 127.039643), // 초기 지도 중심 좌표
    level: 3, // 초기 확대 레벨
  };

  // Kakao 지도 생성
  const map = new kakao.maps.Map(container, options);

  // 초기 장소 검색 실행
  searchBanks(map);

  // 지도 이동/확대 이벤트
  kakao.maps.event.addListener(map, "idle", () => {
    searchBanks(map); // 보이는 화면 중심 기준으로 검색
  });
}

function searchBanks(map) {
  const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  const ps = new kakao.maps.services.Places();

  ps.keywordSearch(
    "은행",
    (data, status) => {
      if (status === kakao.maps.services.Status.OK) {
    

        // 마커 표시
        data.forEach((place) => {
          displayMarker(map, place, infowindow);
        });
      } else {
        console.error("장소 검색 실패:", status);
      }
    },
    {
      location: map.getCenter(), // 현재 지도 중심 좌표
      radius: 5000, // 검색 반경 (단위: 미터)
    }
  );
}

function displayMarker(map, place, infowindow) {

  const marker = new kakao.maps.Marker({
    map: map, // 지도 객체
    position: new kakao.maps.LatLng(place.y, place.x), // 마커 위치
  });

  kakao.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(
      `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`
    );
    infowindow.open(map, marker);
  });
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