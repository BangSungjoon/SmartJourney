<template>
    <div class="portfolio-container">
      <!-- 헤더 -->
      <header class="portfolio-header">
        <h1>당신의 미래를 위해 찾고 싶은 상품</h1>
        <p>분류별로 원하는 항목 선택에 따라, 자동으로 원하는 상품을 찾아 보여줍니다.</p>
      </header>
  
      <!-- 필터 섹션 -->
      <div class="filters">
        <div class="filter-group">
          <select v-model="selectedRisk">
            <option value="저위험">위험도</option>
            <option value="중위험">자산유형</option>
          </select> 에 따라 상품 추천 받을게요!
        </div>
      </div>
  
      <!-- 버튼 -->
      <div class="actions">
        <button @click="applyFilters">나의 선택 확인</button>
      </div>
  
      <!-- 상품 리스트 -->
      <div class="portfolio-list">
        <PortfolioCard
          v-for="(portfolio, index) in filteredPortfolios"
          :key="index"
          :portfolio="portfolio"
        />
      </div>
      

    </div>
  </template>

<script setup>

</script>

<style scoped>
.portfolio-container {
    display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%; /* 화면 너비 */
  height: 100vh; /* 화면 높이 */
  padding: 20px;
  color: #fff;
  background-color: #000; /* 배경색 */
  box-sizing: border-box; /* 패딩 포함 */
}

.portfolio-header {
  text-align: center;
  margin-bottom: 30px;
}

.portfolio-header h1 {
  font-size: 2rem;
  font-weight: bold;
}

.portfolio-header p {
  font-size: 1rem;
  color: #aaa;
}

.filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.filter-group {
  flex: 1;
  margin-right: 10px;
}

.filter-group:last-child {
  margin-right: 0;
}

.filter-group label {
  display: block;
  margin-bottom: 5px;
  font-size: 0.9rem;
  color: #aaa;
}

.filter-group select {
  width: 100%;
  padding: 8px;
  font-size: 1rem;
  border-radius: 4px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
}

.actions {
  text-align: center;
  margin-bottom: 30px;
}

.actions button {
  margin: 0 10px;
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

.portfolio-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
</style>