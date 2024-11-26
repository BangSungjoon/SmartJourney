<template>
  <div class="carousel-wrapper">
    <Carousel :autoplay="3000" :wrap-around="true">
      <Slide>
        <div class="banner" :style="{ backgroundImage: `url(${bannerImage1})` }">
          <div class="banner-content">
            <h1>나만의 맞춤 금융 플랜</h1>
            <p>간단한 질문으로 최적의 포트폴리오를 추천받으세요!</p>
          </div>
        </div>
      </Slide>
      <Slide>
        <div class="banner" :style="{ backgroundImage: `url(${bannerImage2})` }">
          <div class="banner-content">
            <h1>내 주변 은행 찾기</h1>
            <p>가까운 은행과 예적금 상품 정보를 한눈에 확인하세요!</p>
          </div>
        </div>
      </Slide>
      <Slide>
        <div class="banner" :style="{ backgroundImage: `url(${bannerImage3})` }">
          <div class="banner-content">
            <h1>금융 상품 비교하기</h1>
            <p>관심 있는 상품을 모아 조건을 비교하고, 나에게 맞는 금융 상품을 선택하세요!</p>
          </div>
        </div>
      </Slide>
      <Slide>
        <div class="banner" :style="{ backgroundImage: `url(${bannerImage4})` }">
          <div class="banner-content">
            <h1>맞춤형 혜택 찾기</h1>
            <p>간단한 정보 입력으로 받을 수 있는 보조금을 바로 확인하세요!</p>
          </div>
        </div>
      </Slide>
      <template #addons>
        <Pagination />
      </template>
    </Carousel>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import bannerImage1 from '@/assets/images/home/list1.png';
import bannerImage2 from '@/assets/images/home/list2.png';
import bannerImage3 from '@/assets/images/home/list3.png';
import bannerImage4 from '@/assets/images/home/list4.png';

export default defineComponent({
  name: "TextCarousel",
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      bannerImage1,
      bannerImage2,
      bannerImage3,
      bannerImage4,
      navItems: [
        "송금 마트편", 
        "내일을 준비한 커버", 
        "신규회원 혜택", 
        "모임 관리 꿀팁", 
        "리뷰 참여", 
        "이벤트 GET"
      ],
    };
  },
});
</script>

<style scoped>
/* 캐러셀 컨테이너 */
.carousel-wrapper {
  width: 100%;
  margin: 0 auto; /* 중앙 정렬 */
  font-family: 'Noto Sans KR', sans-serif;
}

/* 배너 스타일 */
.banner {
  width: 100%;
  height: 40vh;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

/* 배너 내용을 위한 새로운 스타일 */
.banner-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  text-align: center;
  /* background-color: rgba(144, 173, 198, 0.7);  */
  padding: 20px;
}

.banner h1 {
  font-size: 2.5rem; /* 큰 제목 크기 */
  font-weight: bold; /* 큰 제목 두껍게 */
  margin-bottom: 1rem; /* 제목 아래 여백 */
  font-family: 'Noto Sans KR', sans-serif;
  color: #007bff;
}

.banner p {
  font-size: 1.2rem; /* 부제목 크기 */
  color: black; /* 부제목 색상 */
  line-height: 1.6; /* 줄 간격 */
}

/* 하단 네비게이션 스타일 */
.carousel-navigation {
  display: flex; /* 네비게이션 버튼들을 가로로 정렬 */
  justify-content: space-around; /* 버튼 사이의 간격을 고르게 배치 */
  align-items: center; /* 버튼을 수직 중앙에 정렬 */
  margin-top: 20px; /* 캐러셀과 네비게이션 사이 간격 */
  background-color: #f8f9fa; /* 네비게이션 컨테이너의 배경색 (밝은 회색) */
  padding: 10px 0; /* 상하로 10px의 내부 여백 추가 */
  border-top: 1px solid #ddd; /* 상단에 얇은 구분선 추가 */
}

/* 네비게이션 버튼 스타일 */
.nav-item {
  background: none; /* 버튼의 배경색 제거 */
  border: none; /* 버튼의 테두리 제거 */
  font-size: 1rem; /* 버튼 텍스트의 크기를 1rem로 설정 (기본 폰트 크기) */
  color: #666; /* 버튼 텍스트 색상을 짙은 회색으로 설정 */
  padding: 10px 20px; /* 버튼 내부 여백 (상하 10px, 좌우 20px) */
  cursor: pointer; /* 마우스를 올렸을 때 커서를 클릭 가능 상태로 변경 */
  transition: color 0.3s ease; /* 색상 변경 시 부드럽게 전환 (0.3초) */
}

/* 네비게이션 버튼에 마우스를 올렸을 때 스타일 */
.nav-item:hover {
  color: black; /* 버튼 텍스트 색상을 검정으로 변경 */
  font-weight: bold; /* 텍스트를 두껍게 표시 */
}
</style>