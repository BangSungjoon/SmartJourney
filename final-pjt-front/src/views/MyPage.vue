<template>
  <div class="my-page-container">
    <!-- 좌측 메뉴 -->
    <aside class="sidebar">
      <h2>MY PAGE</h2>
      <ul class="menu-list">
      <li class="menu-section">
          <h3>{{ user.username }}님의 활동</h3>
          <ul>
            <li><RouterLink :to="{ name: 'mypage-cart' }" active-class="active">내가 찜한 예/적금 상품</RouterLink></li>
            <li><RouterLink :to="{ name: 'mypage-subsidy' }" active-class="active">맞춤 보조금 찾기</RouterLink></li>
            <li><RouterLink :to="{ name: 'mypage-portlist' }" active-class="active">포트폴리오 관리</RouterLink></li>
            <li><RouterLink :to="{ name: 'mypage-chatbot' }" active-class="active">AI 금융 상담</RouterLink></li>
          </ul>
      </li>
      </ul>

    </aside>

    <!-- 우측 콘텐츠 -->
    <main class="content">
      <!-- <header class="content-header">
        <select class="filter-dropdown">
          <option>전체 플랫폼</option>
        </select>
        <input type="date" class="filter-date" />
        <input type="date" class="filter-date" />
        <button class="search-button">검색</button>
      </header> -->
      <div class="content-body">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useFinStore } from '@/stores/counter'
import axios from 'axios'
import { defineProps } from 'vue';

const props = defineProps({
id: {
  type: String,
  required: true
}
});

console.log(`props.id는 ${props.id}`); // id 값이 정상적으로 전달됨

const store = useFinStore()
const route = useRoute()
const user = ref('') // 사용자 데이터를 저장할 변수

onMounted(() => {
  const token = localStorage.getItem('token');
  if (token) {
      axios.get('http://127.0.0.1:8000/accounts/user/', {
          headers: { 'Authorization': `Token ${token}` }
      })
          .then((res) => {
              user.value = res.data;
              console.log(`userid는 ${user.value}`)
          })
          .catch((err) => console.log(err))
  }
})
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
height: calc(100vh - 40px);
overflow-y: auto;
}

.menu-section li a {
  text-decoration: none;
  color: #555;
  transition: color 0.3s ease;
  cursor: pointer;
}

.menu-section li .active {
  color: #007bff;
  font-weight: bold;
}

.menu-section li a:hover {
  color: #007bff;
}
</style>