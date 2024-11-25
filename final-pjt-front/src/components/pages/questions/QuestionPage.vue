
<template>
  <div class="question-container">
    <!-- 질문 표시 -->
    <h1 class="question-title">{{ currentQuestion.text }}</h1>
    <!-- 입력 필드 + 화살표 버튼 -->
    <div v-if="currentQuestion.inputType === 'number'" class="input-wrapper">
      <input
      type="number"
      class="form-control"
      v-model="answer"
      placeholder="숫자를 입력하세요"
      />
    
      <!-- Next 버튼 -->
      <div class="next-button-container">
      <button
        class="next-button"
        :disabled="!answer"
        @click="saveAnswerAndNext"
      >
        Next
      </button>
      </div>
    </div>
    
      <!-- 라디오 버튼 스타일 옵션 -->
      <div v-else-if="currentQuestion.inputType === 'select'" class="radio-options-container">
        <div
          v-for="(option, index) in currentQuestion.options"
          :key="index"
          class="radio-option"
          @click="handleOptionSelect(option)"
        >
          <div :class="['radio-circle', { selected: answer === option }]"></div>
          <span>{{ option }}</span>
        </div>
      </div>

  
      <!-- 진행 상태 표시 -->
      <div class="progress-container">
        <div class="progress-bar">
          <div
            class="progress"
            :style="{ width: progressPercentage + '%' }"
          ></div>
        </div>
        <p class="progress-text">{{ currentQuestionIndex + 1 }} / {{ questions.length }}</p>
      </div>
  </div>
</template>
  
  <script setup>
import axios from 'axios'
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useFinStore } from '@/stores/counter';

const store = useFinStore()
// Router 사용
const router = useRouter();
const route = useRoute();

// 질문 데이터
const questions = [
  { id: 1, text: '목표를 언제까지 달성하고 싶으신가요? (단위: 년 후)', inputType: 'number' },
  { id: 2, text: '투자할 때 더 중요하게 여기는 것은 무엇인가요?', inputType: 'select', options: ['손실 최소화', '균형', '수익 극대화'] },
  { id: 3, text: '비상 자금이 마련되어 있나요?', inputType: 'select', options: ['없음', '약간 있음(3~6개월 생활비 마련)', '충분함(6개월 이상 생활비 마련)'] },
  { id: 4, text: '안정성과 유동성 중 더 중요하게 여기는 것은 무엇인가요?', inputType: 'select', options: ['안정성', '균형', '유동성'] },
  { id: 5, text: '목표 금액이 얼마인가요? (단위: 만원)', inputType: 'number' },
  { id: 6, text: '현재 소득은 어떻게 얻고 계신가요?', inputType: 'select', options: ['정규직', '계약직/프리랜서', '투자 소득', '무직'] },
  { id: 7, text: '가계 상황은 어떠신가요?', inputType: 'select', options: ['외벌이, 피부양자 있음', '외벌이, 피부양자 없음', '맞벌이, 피부양자 있음', '맞벌이, 피부양자 없음'] },
];

// 현재 질문 상태
const currentQuestionIndex = computed(() => parseInt(route.params.id) - 1);
const currentQuestion = computed(() => questions[currentQuestionIndex.value]);

// 사용자의 응답 데이터
const answer = ref('');
const result = ref([]); // 모든 응답 데이터를 저장하는 배열

// 옵션 선택 처리
const handleOptionSelect = (option) => {
  answer.value = option; // 선택한 옵션 저장
  saveAnswerAndNext(); // 답변 저장 및 다음 질문 이동
};

// 답변 저장 및 다음 질문으로 이동
const saveAnswerAndNext = () => {
  // 현재 답변 저장
  result.value[currentQuestionIndex.value] = {
    questionId: currentQuestion.value.id,
    answer: answer.value,
  };

  // 다음 질문으로 이동
  const nextIndex = currentQuestionIndex.value + 1;
  if (nextIndex < questions.length) {
    router.push({ params: { id: nextIndex + 1 } }); // 다음 질문으로 이동
  } else {
    saveAnswer(); // 설문조사 완료 시 데이터 제출
  }

  // 현재 답변 초기화
  answer.value = '';
};

// // 설문조사 데이터 제출
// const submitSurvey = () => {
//   console.log('최종 응답 데이터:', result.value);
//   console.log(result.value[1].answer)

// };


  // 옵션 선택 처리(승주)
  const saveAnswer = function () {
    const token = store.token // 실제 사용자 토큰 값으로 대체
    const headers = {
    'Authorization': `Token ${token}`,
    };
    axios({
        method: 'post',
        url: `${store.API_URL}/financial_products/save_answer/`,
        data: {
            q1_expected_goal_amount: result.value[0].answer,
            q2_goal_duration: result.value[1].answer,
            q3_income_source: result.value[2].answer,
            q4_emergency_fund_status: result.value[3].answer,
            q5_investment_priority: result.value[4].answer,
            q6_safety_or_liquidity: result.value[5].answer,
            q7_household_status: result.value[6].answer,
        },
        headers: headers // 헤더 추가
    }).then((res) => {
        console.log('answer 저장 성공')
        console.log(store.currentUserId)
        router.push({ name: 'portlist', params: { id: store.currentUserId } })
        const answerId = res.data.id
        sendRatio(answerId)
    }).catch(err => console.log(err))
  }
  
  // 진행률 계산
  const progressPercentage = computed(() =>
    ((currentQuestionIndex.value + 1) / questions.length) * 100
  );

  </script>
  
  <style scoped>
 .question-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  background-color: #f7c15c;
  padding: 20px;
  font-family: 'Noto Sans KR', sans-serif;
}

.question-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 30px;
  color: #333;
}

/* 라디오 버튼 스타일 */
.radio-options-container {
  display: flex; /* 플렉스 컨테이너로 변경 */
  flex-direction: column; /* 세로로 정렬 */
  gap: 20px; /* 버튼 간격 */
  width: 100%;
  max-width: 600px; /* 전체 너비 제한 */
}

.radio-option {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 10px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, background-color 0.3s;
}

.radio-option:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.radio-circle {
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-radius: 50%;
  margin-right: 10px;
  transition: background-color 0.3s, border-color 0.3s;
}

.radio-circle.selected {
  background-color: #007bff;
  border-color: #007bff;
}

/* Next 버튼 스타일 */
.next-button-container {
  margin-top: 20px;
}

.next-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.next-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.next-button:hover:not(:disabled) {
  background-color: #0056b3;
}

/* 진행 상태 */
.progress-container {
  margin-top: 7rem; /* 폼과 진행률 간격 */
  width: 80%;
  max-width: 400px;
}

.progress-bar {
  background-color: #e0e0e0;
  border-radius: 10px;
  height: 10px;
  position: relative;
}

.progress {
  background-color: #007bff;
  height: 100%;
  border-radius: 10px;
  transition: width 0.3s ease;
}

.progress-text {
  text-align: center;
  margin-top: 10px;
  font-size: 0.9rem;
  color: #666;
}

  </style>
  