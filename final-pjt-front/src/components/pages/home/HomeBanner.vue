<template>
    <section class="home-banner">
      <h1>Welcome to Our Service</h1>
      <p>Explore the best features and services we offer.</p>
    </section>
  </template>
  
  <script>
  export default {
    name: "HomeBanner",
  };
  </script>
  
  <style scoped>
 .home-banner {
  background-image: url('@/assets/images/home/home-banner.jpg');
  background-size: cover; /* 이미지 크기를 컨테이너에 맞춤 */
  background-position: center; /* 중앙 정렬 */
  width: 100%; /* 배너가 화면 너비를 차지 */
  height: 100vh; /* 배너 높이를 뷰포트 높이에 맞춤 */
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /*텍스트를 위쪽으로 정렬 */
  align-items: center; /*수평 중앙 정렬 */
  text-align: center;
  color: white;
  padding-top: calc(100vh / 5); /* 화면 높이의 1/3 지점에 위치 */
  font-family: 'Noto Sans KR', sans-serif;
}
  
  .home-banner h1 {
    font-size: 2.5rem;
    color: #333;
  }
  
  .home-banner p {
    font-size: 1.2rem;
    color: #666;
  }
  </style>
  