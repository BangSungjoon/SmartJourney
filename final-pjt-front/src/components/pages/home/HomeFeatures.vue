<template>
    <section class="home-features">
      <!-- 첫 번째 섹션 -->
      <div class="feature-row">
        <div class="feature-text">
          <h3>간단한 질문으로 나에게 최적화된 금융 플랜을 설계하세요</h3>
          <p>고객님의 투자 성향과 현재 재무 상황을 분석하여 위험도와 자산 유형에 딱 맞는 포트폴리오 구성을 추천해 드립니다. <br />
            쉽고 직관적인 질문 답변으로 나만의 금융 전략을 세우고 스마트한 자산 관리를 시작해 보세요!</p>
          <!-- <a href="#">이동 링크</a> -->
        </div>
        <div class="image-grid">
          <img src="@/assets/images/home/main1.jpg" alt="Feature 1" />
        </div>
      </div>
  
      <!-- 두 번째 섹션 -->
      <div class="feature-row reverse">
        <div class="feature-text">
          <h3>내 주변 은행, 한눈에 확인하세요</h3>
          <p>은행을 지도에서 바로 확인하고, 원하는 은행을 선택해 예적금 상품 정보를 확인해 보세요.</p>
          <!-- <a href="#">이동 링크</a> -->
        </div>
        <div class="image-grid">
          <img src="@/assets/images/home/main2.jpg" alt="Feature 2" />
        </div>
      </div>


      <!-- 세 번째 섹션 -->
      <div class="feature-row">
        <div class="feature-text">
          <h3>금융 상품도 비교의 시대, 관심 상품을 한곳에 모아보세요</h3>
          <p>원하는 은행의 상품 정보를 바로 확인하고, 장바구니에 담아 관심 상품을 한곳에 모아보세요. <br />
            조건을 비교하며 나만의 금융 목표에 가장 잘 맞는 상품을 찾을 수 있습니다.</p>
          <!-- <a href="#">이동 링크</a> -->
        </div>
        <div class="image-grid">
          <img src="@/assets/images/home/feature1.jpg" alt="Feature 1" />
        </div>
      </div>

      <div class="feature-row reverse">
        <div class="feature-text">
          <h3>나에게 딱 맞는 혜택을 찾아드립니다</h3>
          <p>간단한 정보 입력으로 받을 수 있는 보조금을 손쉽게 확인하세요. <br />
            고객님의 조건에 맞는 다양한 지원 혜택과 보조금을 정리해드립니다.</p>
          <!-- <a href="#">이동 링크</a> -->
        </div>
        <div class="image-grid">
          <img src="@/assets/images/shared/hand.jpg" alt="Feature 2" />
        </div>
      </div>

    </section>
  </template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const features = ref([]); // 모든 feature-row 요소를 추적
const observer = ref(null); // Intersection Observer 인스턴스

const handleIntersection = (entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      // 요소가 보이면 'visible' 클래스 추가
      entry.target.classList.add("visible");
    } else {
      // 필요 시 요소가 화면 밖으로 나가면 'visible' 클래스 제거
      entry.target.classList.remove("visible");
    }
  });
};

onMounted(() => {
  observer.value = new IntersectionObserver(handleIntersection, {
    threshold: 0.2, // 요소가 20% 보이면 콜백 실행
  });

  // 모든 feature-row 요소를 관찰
  features.value = document.querySelectorAll(".feature-row");
  features.value.forEach((feature) => observer.value.observe(feature));
});

onBeforeUnmount(() => {
  // 컴포넌트가 파괴될 때 observer 해제
  if (observer.value) {
    features.value.forEach((feature) =>
      observer.value.unobserve(feature)
    );
    observer.value.disconnect();
  }
});
</script>



  
  <style scoped>
  .home-features {
    padding: 50px 20px;
    background-color: #f9f9f9;
    display: flex;
    flex-direction: column;
    gap: 50px; /* 섹션 간 간격 */
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  .feature-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 7px; /* 텍스트와 이미지 간 간격 */
    padding: 0 4rem; /* 섹션 좌우 여백 추가 */
  }
  
  .feature-row.reverse {
    flex-direction: row-reverse; /* 텍스트와 이미지를 반대로 배치 */
  }
  
  .feature-text {
    flex: 1;
    max-width: 50%; /* 텍스트 너비 제한 */
  }
  
  .feature-text h3 {
    font-size: 2.2rem;
    color: #333;
    margin-bottom: 20px;
  }
  
  .feature-text p {
    font-size: 1rem;
    color: #666;
    line-height: 1.6;
    padding-top: 30px;
  }
  
  .image-grid {
    flex: 1;
    display: flex;
    justify-content: center;
  }
  
  .image-grid img {
  width: 40rem; /* 부모 컨테이너에 맞춤 */
  height: auto; /* 원본 비율 유지 */
  object-fit: cover; /* 필요 시 이미지 잘림 방지 */
  border-radius: 0.625rem; /* 모서리를 둥글게 (10px = 0.625rem) */
  box-shadow: 0 0.25rem 0.625rem rgba(0, 0, 0, 0.1); /* 그림자 추가 */
}

.fade-in-fwd {
	-webkit-animation: fade-in-fwd 1.5s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
	        animation: fade-in-fwd 1.5s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
}

 @-webkit-keyframes fade-in-fwd {
  0% {
    -webkit-transform: translateZ(-80px);
            transform: translateZ(-80px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateZ(0);
            transform: translateZ(0);
    opacity: 1;
  }
}
@keyframes fade-in-fwd {
  0% {
    -webkit-transform: translateZ(-80px);
            transform: translateZ(-80px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateZ(0);
            transform: translateZ(0);
    opacity: 1;
  }
}

.feature-row {
  opacity: 0; /* 초기 상태: 투명 */
  transform: translateY(20px); /* 약간 아래로 이동 */
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.feature-row.visible {
  opacity: 1; /* 보일 때: 불투명 */
  transform: translateY(0); /* 원래 위치 */
}

  </style>
  