<template>
  <div class="carousel-wrapper">
    <!-- Carousel 컴포넌트 -->
    <Carousel :autoplay="3000" :wrap-around="true">
      <!-- 텍스트 기반 슬라이드 1 -->
      <Slide>
        <div class="banner">
          <h1>맞춤형 금융 포트폴리오 만들기</h1>
          <p>고객님의 투자 성향과 현재 재무 상황을 분석하여 위험도와 자산 유형에 딱 맞는 포트폴리오 구성을 추천해 드립니다.
            쉽고 직관적인 질문 답변으로 나만의 금융 전략을 세우고 스마트한 자산 관리를 시작해 보세요!</p>
        </div>
      </Slide>
      <!-- 텍스트 기반 슬라이드 2 -->
      <Slide>
        <div class="banner">
          <h1>서비스2</h1>
          <p>복잡한 자산 관리도 이제 간편하게</p>
        </div>
      </Slide>
      <!-- 텍스트 기반 슬라이드 3 -->
      <Slide>
        <div class="banner">
          <h1>서비스3</h1>
          <p>새로운 기술과 함께 더 나은 금융 생활을 경험하세요</p>
        </div>
      </Slide>
      <!-- 텍스트 기반 슬라이드 4 -->
      <Slide>
        <div class="banner">
          <h1>서비스4</h1>
          <p>사업의 시작부터 관리까지</p>
        </div>
      </Slide>
      <!-- 페이지네이션 추가 -->
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

export default defineComponent({
  name: "TextCarousel", // 컴포넌트 이름 정의
  components: {
    Carousel,   // Carousel 컴포넌트 등록
    Slide,      // Slide 컴포넌트 등록
    Pagination, // Pagination 컴포넌트 등록
  },
  data() {
    return {
      // 하단 네비게이션 항목
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
  width: 100%; /* 배너가 부모 너비를 모두 차지 */
  height: 40vh; /* 배너 높이 */
  background-color: white; /* 배너 배경색 */
  color: black; /* 텍스트 색상 */
  text-align: center; /* 텍스트 중앙 정렬 */
  padding: 50px 20px; /* 배너 여백 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 그림자 효과 */
}

.banner h1 {
  font-size: 2.5rem; /* 큰 제목 크기 */
  font-weight: bold; /* 큰 제목 두껍게 */
  margin-bottom: 1rem; /* 제목 아래 여백 */
}

.banner p {
  font-size: 1.2rem; /* 부제목 크기 */
  color: #bbb; /* 부제목 색상 */
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


