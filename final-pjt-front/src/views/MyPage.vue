<template>
    <div class="my-page-container">
      <!-- 좌측 메뉴 -->
      <aside class="sidebar">
        <h2>MY PAGE</h2>
        <ul class="menu-list">
        <li class="menu-section">
            <h3>나의 활동</h3>
            <ul>
            <li>회원 정보 수정</li>
            <li>포트폴리오 관리</li>
            <li class="active">내가 찜한 예/적금 상품</li>
            </ul>
        </li>
        </ul>

      </aside>
  
      <!-- 우측 콘텐츠 -->
      <main class="content">
        <header class="content-header">
          <select class="filter-dropdown">
            <option>전체 플랫폼</option>
          </select>
          <input type="date" class="filter-date" />
          <input type="date" class="filter-date" />
          <button class="search-button">검색</button>
        </header>
        <div class="content-body">
          <p>이용 내역이 없습니다.</p>
        </div>
      </main>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  </script>
  
  <style scoped>
  /* 전체 컨테이너 */
  .my-page-container {
    display: flex;
    height: 100vh;
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  /* 좌측 메뉴 */
  .sidebar {
    width: 30%;
    background-color: #f8f8f8;
    border-right: 1px solid #ddd;
    padding: 4rem 0 0 18%
  }
  
  .sidebar h2 {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .menu-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .menu-section {
    margin-bottom: 20px;
  }
  
  .menu-section h3 {
    font-size: 1rem;
    font-weight: bold;
    margin-bottom: 10px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
  }
  
  .menu-section ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .menu-section li {
    margin-bottom: 10px;
    cursor: pointer;
    color: #555;
  }
  
  .menu-section li.active {
    color: #007bff;
    font-weight: bold;
  }
  
  /* 우측 콘텐츠 */
  .content {
    flex: 1;
    padding: 20px;
  }
  
  .content-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .filter-dropdown {
    padding: 5px 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .filter-date {
    padding: 5px 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .search-button {
    padding: 5px 15px;
    font-size: 1rem;
    background-color: #000;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .search-button:hover {
    background-color: #444;
  }
  
  .content-body {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 5px;
    border: 1px solid #ddd;
    text-align: center;
    color: #555;
  }
  </style>
  