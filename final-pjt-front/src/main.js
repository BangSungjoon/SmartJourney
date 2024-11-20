// import './assets/main.css'
// const kakaoMapApiKey = import.meta.env.VITE_KAKAO_API_KEY;
// const script = document.createElement('script');
// script.defer = true;
// script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoMapApiKey}&libraries=services,clusterer,drawing`;
// script.onload = () => {
//     console.log("Kakao Maps API loaded successfully");
//     // 지도 초기화 로직이 필요하다면 여기서 처리할 수 있습니다.
//   };
// document.head.appendChild(script);

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// import dotenv from 'dotenv';

// dotenv.config();

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
