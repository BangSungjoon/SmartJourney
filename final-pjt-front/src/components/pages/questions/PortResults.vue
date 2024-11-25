<template>
  <div class="portfolio-container">
    <!-- 좌우 레이아웃 -->
    <div class="content">
      <!-- 왼쪽 텍스트 및 필터 -->
      <div class="left-content">
        <!-- 헤더 -->
        <header class="portfolio-header">
          <h1>당신의 미래를 위해 찾고 싶은 상품</h1>
          <p>분류별로 원하는 항목 선택에 따라, 자동으로 원하는 상품을 찾아 보여줍니다.</p>
        </header>

        <!-- 필터 섹션 -->
        <div class="filters">
          <div class="filter-item">
            <select v-model="selectedCriteria" class="filter-dropdown">
              <option value="위험도">위험도</option>
              <option value="자산유형">자산 유형</option>
            </select>
            <span class="filter-description">에 따른 포트폴리오 추천받을래요!</span>
          </div>
        </div>

        <!-- 버튼 -->
        <div class="actions">
          <button @click="applyFilters">나의 선택 확인</button>
        </div>
      </div>

      <!-- 오른쪽 원형 배치 -->
      <div class="right-content">
        <div v-if="selectedCriteria === '위험도'" class="large-circle">
          위험도 기반 추천
        </div>

        <div v-else-if="selectedCriteria === '자산유형'" class="triangle-layout">
          <div class="small-circle">종목 1</div>
          <div class="small-circle">종목 2</div>
          <div class="small-circle">종목 3</div>
        </div>
      </div>
    </div>

    <!-- 하단 공유하기 버튼 -->
     
    <footer class="footer">
      <button class="share-button" @click="sharePortfolio">공유하기</button>
    </footer>
  </div>
</template>



<script setup>
import { ref } from 'vue';

const selectedCriteria = ref("위험도"); // 기본값
const applyFilters = () => {
  console.log(`선택된 기준: ${selectedCriteria.value}`);
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
  background-color: #000;
  color: #fff;
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
  background-color: #000;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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
  background-color: #000;
  color: #fff;
  border: none;
  border-bottom: 2px solid #fff;
  padding: 5px 10px;
  font-size: 2rem; /* 선택된 항목 글씨 크기 */
  cursor: pointer;
  outline: none;
}

/* 드롭다운 옵션 */
.filter-dropdown option {
  font-size: 1rem; /* 드롭다운 내부 옵션 글씨 크기 */
  background-color: #000; /* 옵션 배경색 (일관성 유지) */
  color: #fff; /* 옵션 글씨 색 */
}

.filter-dropdown:hover {
  border-bottom: 2px solid #a9a9ff;
}

/* 설명 텍스트 */
.filter-description {
  font-size: 2rem;
  color: #aaa;
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
  color: #fff;
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
  color: #fff;
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
</style>


