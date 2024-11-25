
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
// import PortResults from './PortResults.vue';

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
const saveAnswerAndNext = (ratioData) => {
  // 현재 질문이 숫자를 요구하는 경우 정수로 변환
  if (currentQuestion.value.inputType === 'number') {
    answer.value = parseInt(answer.value, 10);

    // 숫자 변환 실패 시 처리
    if (isNaN(answer.value)) {
      console.error('유효한 정수를 입력해주세요.');
      return;
    }
  }
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
    // 모든 질문 완료 시 결과 페이지로 이동
    // router.push('/results');

    router.push({
      name: 'Results',
      query: { resultData: JSON.stringify(ratioData) }
    });
    console.log('전달할 데이터:', ratioData);
    console.log('라우터 이동:', {
      name: 'Results',
      params: { resultData: ratioData },
});
  }

  // 현재 답변 초기화
  answer.value = '';
};

  // 옵션 선택 처리
  const saveAnswer = function () {
    console.log(result.value[0].answer)
    const token = store.token // 실제 사용자 토큰 값으로 대체
    const headers = {
    'Authorization': `Token ${token}`,
    };
    const requestData = {
      q1_expected_goal_amount: result.value[4].answer, // 예상금액
      q2_goal_duration: result.value[0].answer, // 달성 기간
      q3_income_source: result.value[5].answer, // 소득 경로
      q4_emergency_fund_status: result.value[2].answer, // 비상금
      q5_investment_priority: result.value[1].answer, // 투자할 때 중요하게 여기는 것
      q6_safety_or_liquidity: result.value[3].answer, // 안전성과 유동성
      q7_household_status: result.value[6].answer, // 가계 상황
    }
    axios({
        method: 'post',
        url: `${store.API_URL}/financial_products/save_answer/`,
        data: requestData,
        headers: headers // 헤더 추가
    }).then((res) => {
        console.log('answer 저장 성공')
        console.log(store.currentUserId)
        // router.push({ name: 'portlist', params: { id: store.currentUserId } })
        const answerId = res.data.id
        sendRatio(answerId, requestData)
    }).catch((error) => {
    if (error.response) {
      console.error('응답 데이터:', error.response.data);
      console.error('응답 상태 코드:', error.response.status);
    } else {
      console.error('요청 실패:', error.message);
    }
  });
  }
  // 진행률 계산
  const progressPercentage = computed(() =>
    ((currentQuestionIndex.value + 1) / questions.length) * 100
  );

let ratioData;
  // 비율 저장하는 함수
const sendRatio = function (answerId, requestData) {
    const token = store.token // 실제 사용자 토큰 값으로 대체

    const risk_port_return = riskPort(requestData) // 투자vs저축 return값
    const risk_low = risk_port_return.risk_low
    const risk_m_low = risk_port_return.risk_m_low
    const risk_m = risk_port_return.risk_m
    const risk_m_high = risk_port_return.risk_m_high
    const risk_high = risk_port_return.risk_high

    const save_inv_return = SaveInvTypeFunc(requestData) // 투자vs저축 return값
    const saving_score = save_inv_return.saving_score
    const inv_score = save_inv_return.inv_score

    const port_inv_return = PortInvType(requestData) // 투자 내 상품비율 return 값
    const dom_stock_score = port_inv_return.dom_stock_score
    const int_stock_score = port_inv_return.int_stock_score
    const bond_score = port_inv_return.bond_score
    const alt_invest_score = port_inv_return.alt_invest_score
    
    const port_save_return = PortSaveType(requestData) // 저축 내 상품비율 return 값
    const reg_save_score = port_save_return.reg_save_score
    const inst_save_score = port_save_return.inst_save_score

    const headers = {
    'Authorization': `Token ${token}`,
    };
    ratioData = {
            answer: answerId,
            low_ratio:risk_low,
            med_low_ratio:risk_m_low,
            med_ratio:risk_m,
            med_high_ratio:risk_m_high,
            high_ratio:risk_high,
            saving_ratio: saving_score,
            inv_ratio: inv_score,
            dom_stock_ratio: dom_stock_score,
            int_stock_ratio: int_stock_score,
            bond_ratio: bond_score,
            alt_invest_ratio: alt_invest_score,
            inst_save_ratio: inst_save_score,
            reg_save_ratio: reg_save_score,
        }

    axios({
        method: 'post',
        url: `${store.API_URL}/financial_products/save_ratio/${answerId}/`,
        data: ratioData,
        headers: headers // 헤더 추가
    }).then(() => {
        console.log('ratio 저장 성공')
        // router.push({ name: 'portresult' })
    }).catch(err => {
        console.log(err)
    })
}

const riskPort = function (requestData) {
    const term = requestData.q2_goal_duration;
    const important = requestData.q5_investment_priority
    const emerMoney = requestData.q4_emergency_fund_status
    const safeUtility = requestData.q6_safety_or_liquidity
    const goalMoney = requestData.q1_expected_goal_amount
    const job = requestData.q3_income_source
    const family = requestData.q7_household_status
    console.log(term)
    let risk_low = 0      // 저위험
    let risk_m_low = 0    // 중저위험
    let risk_m = 0        // 중위험
    let risk_m_high = 0   // 중고위험
    let risk_high = 0     // 고위험
    // 목표 기간 - 가중치 0.4
    if (term <= 1) {
        risk_low += 0.4*80
        risk_m_low += 0.4*20
    }
    else if (1 < term < 5) {
        risk_low += 0.4*50
        risk_m_low += 0.4*30
        risk_m += 0.4*20
    }
    else if (5 <= term) {
        risk_low += 0.4*20
        risk_m_low += 0.4*20
        risk_m += 0.4*30
        risk_m_high += 0.4*20
        risk_high += 0.4*10
    }
    // 투자할 때 더 중요하게 여기는 것 - 가중치 0.3
    if (important === '손실 최소화') {
        risk_low += 0.3*80
        risk_m_low += 0.3*20
    }
    else if (important === '균형') {
        risk_low += 0.3*30
        risk_m_low += 0.3*30
        risk_m += 0.3*20
        risk_m_high += 0.3*10
        risk_high += 0.3*10
    }
    else if (important === '수익 극대화') {
        risk_m_low += 0.3*20
        risk_m += 0.3*20
        risk_m_high += 0.3*30
        risk_high += 0.3*30
    }
    // 비상자금 여부 - 가중치 0.2
    if (emerMoney === '없음') {
        risk_low += 0.2*80
        risk_m_low += 0.2*20
    }
    else if (emerMoney === '약간 있음(3~6개월 생활비 마련)') {
        risk_low += 0.2*50
        risk_m_low += 0.2*30
        risk_m += 0.2*20
    }
    else if (emerMoney === '충분함(6개월 이상 생활비 마련)') {
        risk_low += 0.2*30
        risk_m_low += 0.2*20
        risk_m += 0.2*20
        risk_m_high += 0.2*20
        risk_high += 0.2*10
    }
    // 안전성과 유동성 중 중요한 부분 - 가중치 0.1
    if (safeUtility === '안정성') {
        risk_low += 0.1*80
        risk_m_low += 0.1*20
    }
    else if (safeUtility === '유동성') {
        risk_low += 0.1*40
        risk_m_low += 0.1*30
        risk_m += 0.1*20
        risk_m_high += 0.1*10
    }
    else if (safeUtility === '균형') {
        risk_low += 0.1*50
        risk_m_low += 0.1*30
        risk_m += 0.1*20
    }
    // 목표를 달성하기 위해 필요한 애상 금액
    if (goalMoney <= 1000) {
        risk_low += 5
    }
    else if (5000 <= goalMoney) {
        risk_high += 5
    }
    // 현재 소득을 얻는 형태
    if (job === '정규직') {
        risk_m_high += 3
        risk_high += 2
    }
    else if (job === '계약직/프리랜서') {
        risk_low += 3
        risk_m_low += 2
    }
    else if (job === '투자 소득') {
        risk_high += 5
    }
    else if (job === '무직') {
        risk_low += 5
    }
    // 가계 상황 (피부양자 여부 등)
    if (family === '외벌이, 피부양자 있음') {
        risk_low += 3
        risk_m_low += 2
    }
    else if (family === '외벌이, 피부양자 없음') {
        risk_low += 2
        risk_m_low += 1
    }
    else if (family === '맞벌이, 피부양자 있음') {
        risk_m_low += 3
        risk_m += 2
    }
    else if (family === '맞벌이, 피부양자 없음') {
        risk_m += 3
        risk_high += 2
    }
    console.log(risk_low)
    const total = risk_low + risk_m_low + risk_m + risk_m_high + risk_high
    let riskArray = [risk_low, risk_m_low, risk_m, risk_m_high, risk_high]
    riskArray.forEach((risk, index) => {
        riskArray[index] = (risk/total)*100
    });
    [risk_low, risk_m_low, risk_m, risk_m_high, risk_high] = riskArray
    // console.log([risk_low, risk_m_low, risk_m, risk_m_high, risk_high])
    return {risk_low, risk_m_low, risk_m, risk_m_high, risk_high}
}

// 저축 vs 투자
const SaveInvTypeFunc = function (requestData) {
    const term = requestData.q2_goal_duration;
    const important = requestData.q5_investment_priority
    const emerMoney = requestData.q4_emergency_fund_status
    const safeUtility = requestData.q6_safety_or_liquidity
    const goalMoney = requestData.q1_expected_goal_amount
    const job = requestData.q3_income_source
    const family = requestData.q7_household_status
    let saving_score = 0; // 저축 상품 점수
    let inv_score = 0   // 투자 상품 점수

    //q1
    if (term <= 1) {
        saving_score += 80 * 0.4
        inv_score += 20 * 0.4
    } else if (term > 1 && term < 5) {
        saving_score += 50 * 0.4
        inv_score += 50 * 0.4
    } else if (term >= 5) {
        saving_score += 20 * 0.4
        inv_score += 80 * 0.4
    } 
    //q2
    if (important === '손실 최소화') {
        saving_score += 80 * 0.3
        inv_score += 20 * 0.3
    } else if (important === '균형') {
        saving_score += 50 * 0.3
        inv_score += 50 * 0.3
    } else if (important === '수익 극대화') {
        saving_score += 20 * 0.3
        inv_score += 80 * 0.3
    }
    // q3
    if (emerMoney === '없음') {
        saving_score += 80 * 0.2
        inv_score += 20 * 0.2
    } else if (emerMoney === '약간 있음(3~6개월 생활비 마련)') {
        saving_score += 50 * 0.2
        inv_score += 50 * 0.2
    } else if (emerMoney === '충분함(6개월 이상 생활비 마련)') {
        saving_score += 20 * 0.2
        inv_score += 80 * 0.2
    }
    // q4
    if (safeUtility === '안정성') {
        saving_score += 80 * 0.1
        inv_score += 20 * 0.1
    } else if (safeUtility === '균형') {
        saving_score += 50 * 0.1
        inv_score += 50 * 0.1
    } else if (safeUtility === '유동성') {
        saving_score += 50 * 0.1
        inv_score += 50 * 0.1
    }
    // q5
    if (goalMoney <= 1000) {
        saving_score += 5
    } else if (goalMoney >= 5000) {
        inv_score += 5
    }
    // q6
    if (job=== '정규직') {
        inv_score += 3
    } else if (job === '계약직/프리랜서') {
        saving_score += 3
    } else if (job === '투자 소득') {
        inv_score += 5
    } else if (job === '무직') {
        saving_score += 5
    }
    // q7
    if (family === '외벌이, 피부양자 있음') {
        saving_score += 5
        inv_score -= 5
    } else if (family === '외벌이, 피부양자 없음') {
        saving_score += 3
        inv_score -= 3
    } else if (family === '맞벌이, 피부양자 있음') {
        saving_score += 3
        inv_score += 3
    } else if (family === '맞벌이, 피부양자 없음') {
        saving_score -= 5
        inv_score += 5
    }

    const temp_saving_score = saving_score
    saving_score = saving_score/(saving_score + inv_score)
    inv_score = inv_score/(temp_saving_score + inv_score)

        return{saving_score, inv_score}
}


// 투자 상품 내
const PortInvType = function (requestData) {
    const term = requestData.q2_goal_duration;
    const important = requestData.q5_investment_priority
    const emerMoney = requestData.q4_emergency_fund_status
    // const safeUtility = requestData.q6_safety_or_liquidity
    const goalMoney = requestData.q1_expected_goal_amount
    const job = requestData.q3_income_source
    const family = requestData.q7_household_status
    let dom_stock_score = 0; // 국내 주식형
    let int_stock_score = 0   // 해외 주식형
    let bond_score = 0   // 채권형
    let alt_invest_score = 0   // 대안투자
    

    //q1
    if (term <= 1) {
        dom_stock_score += 10 * 0.4
        int_stock_score += 10 * 0.4
        bond_score += 80 * 0.4
    } else if (term > 1 && term < 5) {
        dom_stock_score += 30 * 0.4
        int_stock_score += 20 * 0.4
        bond_score += 40 * 0.4
        alt_invest_score += 10 * 0.4
    } else if (term >= 5) {
        dom_stock_score += 30 * 0.4
        int_stock_score += 40 * 0.4
        bond_score += 10 * 0.4
        alt_invest_score += 20 * 0.4
    } 
    // q2
    if (important === '손실 최소화') {
        dom_stock_score += 10 * 0.3
        int_stock_score += 10 * 0.3
        bond_score += 80 * 0.3
    } else if (important === '균형') {
        dom_stock_score += 25 * 0.3
        int_stock_score += 25 * 0.3
        bond_score += 30 * 0.3
        alt_invest_score += 20 * 0.3
    } else if (important === '수익 극대화') {
        dom_stock_score += 30 * 0.3
        int_stock_score += 40 * 0.3
        bond_score += 10 * 0.3
        alt_invest_score += 20 * 0.3
    }
    // q3
    if (emerMoney === '없음') {
        dom_stock_score += 10 * 0.3
        int_stock_score += 10 * 0.3
        bond_score += 80 * 0.3
    } else if (emerMoney === '약간 있음(3~6개월 생활비 마련)') {
        dom_stock_score += 30 * 0.3
        int_stock_score += 20 * 0.3
        bond_score += 40 * 0.3
        alt_invest_score += 10 * 0.3
    } else if (emerMoney === '충분함(6개월 이상 생활비 마련)') {
        dom_stock_score += 30 * 0.3
        int_stock_score += 40 * 0.3
        bond_score += 10 * 0.3
        alt_invest_score += 20 * 0.3
    }
    // q5
    if (goalMoney <= 1000) {
        bond_score += 5
    } else if (goalMoney >= 5000) {
        dom_stock_score += 3
        alt_invest_score += 3
    }
    // q6
    if (job === '정규직') {
        int_stock_score += 3
        alt_invest_score += 2
    } else if (job === '계약직/프리랜서') {
        dom_stock_score += 3
        bond_score += 2
    } else if (job === '투자 소득') {
        alt_invest_score += 5
    } else if (job === '무직') {
        bond_score += 5
    }
    // q7
    if (family === '외벌이, 피부양자 있음') {
        dom_stock_score += 3
        bond_score += 5
    } else if (family === '외벌이, 피부양자 없음') {
        dom_stock_score += 2
        int_stock_score += 2
        bond_score += 3
    } else if (family === '맞벌이, 피부양자 있음') {
        int_stock_score += 2
        bond_score += 2
        alt_invest_score += 3
    } else if (family === '맞벌이, 피부양자 없음') {
        int_stock_score +=3
        alt_invest_score += 5
    }

    const temp_dom_stock_score = dom_stock_score
    const temp_int_stock_score = int_stock_score
    const temp_bond_score = bond_score
    const temp_alt_invest_score = alt_invest_score
    dom_stock_score = temp_dom_stock_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)
    int_stock_score = temp_int_stock_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)
    bond_score = temp_bond_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)
    alt_invest_score = temp_alt_invest_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)

        return{dom_stock_score, int_stock_score, bond_score, alt_invest_score}
}

// 저축 상품 내
const PortSaveType = function (requestData) {
    const term = requestData.q2_goal_duration;
    // const important = requestData.q5_investment_priority
    const emerMoney = requestData.q4_emergency_fund_status
    const safeUtility = requestData.q6_safety_or_liquidity
    const goalMoney = requestData.q1_expected_goal_amount
    const job = requestData.q3_income_source
    const family = requestData.q7_household_status
    let reg_save_score = 0   // 보통예금
    let inst_save_score = 0; // 적금/정기예금

    //q1
    if (term <= 1) {
        reg_save_score += 80 * 0.4
        inst_save_score += 20 * 0.4
    } else if (term > 1 && term < 5) {
        reg_save_score += 50 * 0.4
        inst_save_score += 50 * 0.4
    } else if (term >= 5) {
        reg_save_score += 20 * 0.4
        inst_save_score += 80 * 0.4
    } 
    // q3
    if (emerMoney === '없음') {
        reg_save_score += 80 * 0.2
        inst_save_score += 20 * 0.2
    } else if (emerMoney === '약간 있음(3~6개월 생활비 마련)') {
        reg_save_score += 50 * 0.2
        inst_save_score += 50 * 0.2
    } else if (emerMoney === '충분함(6개월 이상 생활비 마련)') {
        reg_save_score += 20 * 0.2
        inst_save_score += 80 * 0.2
    }
    // q4
    if (safeUtility === '안정성') {
        reg_save_score += 20 * 0.3
        inst_save_score += 80 * 0.3
    } else if (safeUtility === '균형') {
        reg_save_score += 50 * 0.3
        inst_save_score += 50 * 0.3
    } else if (safeUtility === '유동성') {
        reg_save_score += 80 * 0.3
        inst_save_score += 20 * 0.3
    }
    // q5
    if (goalMoney <= 1000) {
        reg_save_score += 5
    } else if (goalMoney >= 5000) {
        inst_save_score += 5
    }
    // q6
    if (job === '정규직') {
        reg_save_score += 40 * 0.1
        inst_save_score += 60 * 0.1
    } else if (job === '계약직/프리랜서') {
        reg_save_score += 60 * 0.1
        inst_save_score += 40 * 0.1
    } else if (job === '투자 소득') {
        reg_save_score += 50 * 0.1
        inst_save_score += 50 * 0.1
    } else if (job === '무직') {
        reg_save_score += 70 * 0.1
        inst_save_score += 30 * 0.1
    }
    // q7
    if (family === '외벌이, 피부양자 있음') {
        reg_save_score -= 3
        inst_save_score += 3
    } else if (family === '외벌이, 피부양자 없음') {
        reg_save_score -= 2
        inst_save_score += 2
    } else if (family === '맞벌이, 피부양자 있음') {
        inst_save_score += 2
    } else if (family === '맞벌이, 피부양자 없음') {
        reg_save_score += 2
        inst_save_score -= 2
    }

    const temp_reg_save_score = reg_save_score
    reg_save_score = reg_save_score/(reg_save_score + inst_save_score)
    inst_save_score = inst_save_score/(temp_reg_save_score + inst_save_score)

        return{reg_save_score, inst_save_score}
}

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
  