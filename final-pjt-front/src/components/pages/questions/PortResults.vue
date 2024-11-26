<template>
  <div class="portfolio-container">
    <div class="content">
      <div class="left-content">
        <header class="portfolio-header">
          <h1>당신의 미래를 위해 찾고 싶은 상품</h1>
          <p>분류별로 원하는 항목 선택에 따라, 자동으로 원하는 상품을 찾아 보여줍니다.</p>
        </header>

        <div class="filters">
          <div class="filter-item">
            <select v-model="selectedCriteria" class="filter-dropdown">
              <option value="위험도">위험도</option>
              <option value="자산유형">자산 유형</option>
            </select>
            <span class="filter-description">에 따른 포트폴리오 추천받을래요!</span>
          </div>
        </div>

        <div class="actions">
          <button @click="applyFilters">다시 검사 받기</button>
        </div>
      </div>

      <div class="position-relative" v-if="resultData">
        <!-- 위험도 차트 -->
        <div v-if="selectedCriteria === '위험도'" class="single-chart position-absolute top-50 start-50 translate-middle">
          <PortChart
            class="chart-container" 
            :portfolio="resultData" 
            :selectedType="selectedCriteria"
          />
        </div>

        <!-- 자산유형 차트 캐러셀 -->
        <div v-else class="carousel-wrapper">
          <div class="carousel">
            <button class="carousel-button prev" @click="prevSlide" v-show="currentSlide > 0">&lt;</button>
            
            <div class="carousel-container">
              <div class="carousel-slide" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
                <div v-for="index in 3" :key="index" class="slide">
                  <PortChart
                    class="chart-container" 
                    :portfolio="resultData" 
                    :selectedType="selectedCriteria"
                    :chartIndex="index - 1"
                  />
                </div>
              </div>
            </div>
            
            <button class="carousel-button next" @click="nextSlide" v-show="currentSlide < 2">&gt;</button>
          </div>
          
          <!-- 슬라이드 인디케이터 추가 -->
          <div class="carousel-indicators">
            <span 
              v-for="index in 3" 
              :key="index"
              :class="['indicator', { active: currentSlide === index - 1 }]"
              @click="currentSlide = index - 1"
            ></span>
          </div>
        </div>
      </div>
      <div v-else>
        <p>데이터를 불러오는 중...</p>
      </div>
    </div>

    <!-- <footer class="footer">
      <button class="share-button" @click="sharePortfolio">공유하기</button>
    </footer> -->
  </div>
</template>

<script setup>
import axios from 'axios';
import PortChart from './PortChart.vue';
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useFinStore } from '@/stores/counter';

const store = useFinStore();
const route = useRoute();
const router = useRouter()
const resultData = ref(null);
const selectedCriteria = ref("위험도");
const currentSlide = ref(0);

onMounted(async () => {
    try {
        const answerId = route.params.answerId;
        const response = await store.getPortfolioResult(answerId);
        console.log('Portfolio data loaded:', response);
        resultData.value = response;
    } catch (error) {
        console.error('Error loading portfolio data:', error);
    }
});

const applyFilters = () => {
    // console.log(`선택된 기준: ${selectedCriteria.value}`);
    const id = route.params.answerId
    console.log(route.params.answerId)
    axios({
      method: 'delete',
      url:`${store.API_URL}/financial_products/portfolio/${id}/`,
      headers: {
        'Authorization': `Token ${store.token}`
      }
    })
    .then(() => {
      router.push({ name: 'portfolio_main' })
    })
    .catch(err => console.log(err))
};

const sharePortfolio = () => {
    // 공유 기능 구현
    console.log('공유하기 클릭');
};

// 선택 기준이 변경될 때 슬라이드 초기화
watch(selectedCriteria, () => {
  currentSlide.value = 0;
});

const nextSlide = () => {
  if (currentSlide.value < 2) {
    currentSlide.value++;
  }
};

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--;
  }
};
</script>



<style scoped>
/* 전체 컨테이너 */
.portfolio-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  background-color: #E9EAEC;
  color: #000000;
  box-sizing: border-box;
}

/* 좌우 레이아웃 */
.content {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 왼쪽과 오른쪽 50%씩 */
  /* gap: 20px; */
  font-family: 'Noto Sans KR', sans-serif;
  width: 100%; /* 화면 가로를 가득 채움 */
  height: 100%; /* 화면 세로를 가득 채움 */
}

/* 왼쪽 섹션 */
.left-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 100px;
  background-color: #E9EAEC;
  border-radius: 8px;
  /* box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); */
}

.portfolio-header h1 {
  font-size: 2.7rem;
  font-weight: bold;
  margin-bottom: 15px;
}

.portfolio-header p {
  font-size: 1.3rem;
  color: #aaa;
}

/* 필터 섹션 */
.filters {
  margin-top: 20px;
}

.filter-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1rem;
}

/* 드롭다운 */
.filter-dropdown {
  appearance: none;
  background-color: #E9EAEC;
  color: #000000;
  border: none;
  border-bottom: 2px solid #000000;
  padding: 5px 10px;
  font-size: 2rem; /* 선택된 항목 글씨 크기 */
  cursor: pointer;
  outline: none;
}

/* 드롭다운 옵션 */
.filter-dropdown option {
  font-size: 1rem; /* 드롭다운 내부 옵션 글씨 크기 */
  background-color: #E9EAEC; /* 옵션 배경색 (일관성 유지) */
  color: #000000; /* 옵션 글씨 색 */
}

.filter-dropdown:hover {
  border-bottom: 2px solid #a9a9ff;
}

/* 설명 텍스트 */
.filter-description {
  font-size: 2rem;
  color: #000000;
  margin-left: 10px;
}

/* 버튼 */
.actions {
  margin-top: 60px;
}

.actions button {
  padding: 10px 20px;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.actions button:hover {
  background-color: #0056b3;
}


/* 하단 공유하기 버튼 */
.footer {
  width: 100%;
  position: absolute;
  bottom: 20px; /* 하단 간격 */
  text-align: center; /* 버튼을 중앙으로 정렬 */
}

.share-button {
  padding: 10px 20px;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.share-button:hover {
  background-color: #0056b3;
}



/* 오른쪽 섹션 */
.right-content {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: relative;
}

/* 큰 원 */
.large-circle {
  width: 200px;
  height: 200px;
  background-color: #007bff;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #000000;
  font-size: 1.2rem;
  font-weight: bold;
}

/* 작은 원 */
.triangle-layout {
  position: relative;
  width: 300px;
  height: 300px;
}

.triangle-layout .small-circle {
  width: 100px;
  height: 100px;
  background-color: #28a745;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #000000;
  font-size: 1rem;
  font-weight: bold;
  position: absolute;
}

.triangle-layout .small-circle:nth-child(1) {
  top: 0;
  left: 50%;
  transform: translateX(-50%);
}

.triangle-layout .small-circle:nth-child(2) {
  bottom: 0;
  left: 0;
}

.triangle-layout .small-circle:nth-child(3) {
  bottom: 0;
  right: 0;
}

/* 차트 컨테이너 공통 스타일 */
.chart-container {
  width: 60%;  /* 차트 크기를 더 작게 조정 */
  margin: 0 auto;
  background: transparent;
}

/* 단일 차트 컨테이너 */
.single-chart {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 캐러셀 스타일 */
.carousel-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.carousel {
  width: 100%;
  height: 600px;  /* 고정 높이 설정 */
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-container {
  width: 600px;  /* 고정 너비 설정 */
  height: 600px;  /* 고정 높이 설정 */
  overflow: hidden;
}

.carousel-slide {
  display: flex;
  transition: transform 0.5s ease;
  height: 100%;
}

.slide {
  min-width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.3);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: rgb(255, 255, 255);
  font-size: 20px;
  z-index: 1;
}

.carousel-button.prev {
  left: 50px;
}

.carousel-button.next {
  right: 50px;
}

/* 슬라이드 인디케이터 스타일 */
.carousel-indicators {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.indicator.active {
  background: rgba(255, 255, 255, 0.8);
}

/* 차트 컨테이너 스타일 수정 */
.chart-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>


