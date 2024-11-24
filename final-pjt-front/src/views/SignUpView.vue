<template>
     <div class="page-container">
        <div class="content">
            <div class="signup-container">
            <!-- 회원가입 제목 -->
            <h1 class="signup-title">회원가입</h1>
        
            <!-- 기본정보 입력 -->
            <form @submit.prevent="handleSubmit" class="signup-form">
                <label for="username">아이디*</label>
                <input
                type="text"
                id="username"
                v-model="username"
                placeholder="영어 소문자, 숫자 조합 4~13자리"
                required
                />
        
                <label for="password">비밀번호*</label>
                <input
                type="password"
                id="password"
                v-model="password1"
                placeholder="영문자, 숫자, 특수문자 조합 8~16자리"
                required
                />
        
                <label for="confirm-password">비밀번호 확인*</label>
                <input
                type="password"
                id="confirm-password"
                v-model="password2"
                placeholder="비밀번호를 다시 입력하세요"
                required
                />
        
                <!-- 제출 버튼 -->
                <button type="submit" class="submit-button">회원가입</button>
            </form>
            </div>
        </div>
    </div>
</template>
  

  <script>

  </script>
  

  <style scoped>
  /* 전체 컨테이너 */
  .signup-container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: -300px; /* 위로 50px 이동 */
  }
  
  /* 제목 */
  .signup-title {
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 30px;
  }
  
  /* 진행 바 */
  .progress-bar {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
  }
  
  .step {
    text-align: center;
    flex: 1;
    position: relative;
  }
  
  .step p {
    margin-top: 10px;
    font-size: 0.9rem;
  }
  
  .step .number {
    display: inline-block;
    width: 40px;
    height: 40px;
    line-height: 40px;
    border-radius: 50%;
    background-color: #ddd;
    color: white;
    font-weight: bold;
  }
  
  .step.active .number {
    background-color: #007bff;
  }
  
  .step.completed .number {
    background-color: #28a745;
  }
  
  /* 기본정보 입력 섹션 */
  .signup-form {
    border-top: 1px solid #ddd;
    padding-top: 20px;
  }
  
  .signup-form h2 {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .signup-form span {
    font-size: 0.9rem;
    color: #888;
  }
  
  .signup-form label {
    display: block;
    margin: 15px 0 5px;
    font-size: 0.9rem;
  }
  
  .signup-form input {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .signup-form input:focus {
    outline: none;
    border-color: #007bff;
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



  /* 페이지 전체를 감싸는 컨테이너 */
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
  
  