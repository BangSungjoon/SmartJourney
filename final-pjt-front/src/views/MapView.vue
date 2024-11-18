<template>
    <div>
        <h1>내 주변 은행 찾기</h1>
    <div id="map" style="width:500px;height:400px;"></div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';

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
  const container = document.getElementById('map'); // 지도 컨테이너
  if (!container) {
    console.error("지도 컨테이너를 찾을 수 없습니다.");
    return;
  }

  const options = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도 중심 좌표
    level: 3, // 확대 레벨
  };

  // Kakao 지도 생성
  const map = new kakao.maps.Map(container, options);

  // 은행 검색 실행
  searchBanks(map);
}

function searchBanks(map) {
  const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  const ps = new kakao.maps.services.Places(); // Places 객체 생성

  // 키워드로 장소 검색
  ps.keywordSearch("은행", (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      const bounds = new kakao.maps.LatLngBounds();

      // 검색 결과를 지도에 표시
      data.forEach((place) => {
        displayMarker(map, place, infowindow);
        bounds.extend(new kakao.maps.LatLng(place.y, place.x));
      });

      // 지도 범위를 검색된 장소로 재설정
      map.setBounds(bounds);
    } else {
      console.error("장소 검색 실패:", status);
    }
  });
}

function displayMarker(map, place, infowindow) {
  // 마커 생성
  const marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  // 마커 클릭 이벤트 추가
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