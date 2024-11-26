<template>
    <div class="page-container">
      <div class="content">
        <div class="login-container">
          <!-- 로그인 제목 -->
          <h1 class="login-title">로그인</h1>
  
          <!-- 로그인 입력 -->
          <form @submit.prevent="logIn" class="login-form">
            <label for="username">아이디*</label>
            <input
              type="text"
              id="username"
              v-model="username"
              placeholder="아이디를 입력하세요"
              required
            />
  
            <label for="password">비밀번호*</label>
            <input
              type="password"
              id="password"
              v-model="password"
              placeholder="비밀번호를 입력하세요"
              required
            />
  
            <!-- 제출 버튼 -->
            <button type="submit" class="submit-button">로그인</button>
          </form>
  
          <!-- 회원가입 안내 -->
          <!-- <div class="signup-redirect">
            <p>처음 방문하셨나요?</p>
            <button @click="goToSignup" class="redirect-button">
              회원가입
            </button>
          </div> -->
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref } from 'vue'
import { useFinStore } from '@/stores/counter';

const username = ref(null)
const password = ref(null)
const store = useFinStore()

const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}
</script>

<style scoped>
/* 전체 컨테이너 */
.login-container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Noto Sans KR', sans-serif;
  margin-top: -100px; /* 정중앙에서 살짝 위로 이동 */
}

/* 제목 */
.login-title {
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 30px;
}

/* 로그인 폼 */
.login-form {
  border-top: 1px solid #ddd;
  padding-top: 20px;
}

.login-form label {
  display: block;
  margin: 15px 0 5px;
  font-size: 0.9rem;
}

.login-form input {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.login-form input:focus {
  outline: none;
  border-color: #007bff; /* 포커스 시 파란색 테두리 */
}

/* 제출 버튼 */
.submit-button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

.submit-button:hover {
  background-color: #0056b3;
}

/* 회원가입 안내 */
.signup-redirect {
  text-align: center;
  margin-top: 20px;
}

.signup-redirect p {
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: #333;
}

.redirect-button {
  padding: 10px 20px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
}

.redirect-button:hover {
  background-color: #218838;
}

.page-container {
  display: flex;
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  height: 100vh; /* 전체 화면 높이 */
  background-color: #f9f9f9; /* 배경색 */
}

/* 메인 콘텐츠 영역 */
.content {
  flex: 1; /* 콘텐츠가 빈 공간을 채우도록 설정 */
}

/* Footer 영역 */
footer {
  height: 100px; /* 고정 높이 */
  background-color: #333; /* Footer 배경색 */
  color: white; /* 텍스트 색상 */
  display: flex;
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  font-size: 1rem;
}
</style>