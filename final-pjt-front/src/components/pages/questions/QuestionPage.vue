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
import { ref, computed, watch } from 'vue';
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

// 현재 질문 인덱스를 ref로 관리
const currentQuestionIndex = ref(parseInt(route.params.id) - 1);

// 답변 저장 및 다음 질문으로 이동
const saveAnswerAndNext = async () => {
  try {
    // 현재 답변 저장
    result.value.push({
      questionId: currentQuestion.value.id,
      answer: answer.value
    });

    // 디버깅을 위한 로그
    console.log('Current index:', currentQuestionIndex.value);
    console.log('Questions length:', questions.length);
    console.log('Current answer:', answer.value);

    if (currentQuestionIndex.value < questions.length - 1) {
      // 다음 질문으로 이동
      const nextIndex = currentQuestionIndex.value + 1;
      console.log('Moving to question:', nextIndex + 1);
      
      await router.push({
        name: 'QuestionPage',
        params: { id: (nextIndex + 1).toString() }
      });
      
      // 답변 초기화
      answer.value = '';
      currentQuestionIndex.value = nextIndex;
    } else {
      // 마지막 질문일 경우
      console.log('Saving final answer...');
      await saveAnswer();
    }
  } catch (error) {
    console.error('Navigation error:', error);
  }
};

// 옵션 선택 처리
const handleOptionSelect = (option) => {
  answer.value = option;
  saveAnswerAndNext();
};

// saveAnswer 함수 수정
const saveAnswer = async () => {
  try {
    const requestData = {
      q1_expected_goal_amount: result.value[4].answer,
      q2_goal_duration: result.value[0].answer,
      q3_income_source: result.value[5].answer,
      q4_emergency_fund_status: result.value[2].answer,
      q5_investment_priority: result.value[1].answer,
      q6_safety_or_liquidity: result.value[3].answer,
      q7_household_status: result.value[6].answer,
    };

    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/financial_products/save_answer/`,
      data: requestData,
      headers: {
        'Authorization': `Token ${store.token}`
      }
    });

    console.log('Answer saved successfully:', response.data);
    const answerId = response.data.id;
    await sendRatio(answerId, requestData);  // requestData 전달
  } catch (error) {
    console.error('Error saving answer:', error);
    throw error;
  }
};

// 현재 질문 computed 속성
const currentQuestion = computed(() => questions[currentQuestionIndex.value]);

// 사용자의 응답 데이터
const answer = ref('');
const result = ref([]); // 모든 응답 데이터를 저장하는 배열

// 진행률 계산
const progressPercentage = computed(() =>
  ((currentQuestionIndex.value + 1) / questions.length) * 100
);

let ratioData;
// 비율 저장하는 함수
const sendRatio = async (answerId, requestData) => {
    try {
        const risk_port_return = riskPort(requestData)
        const save_inv_return = SaveInvTypeFunc(requestData)
        const port_inv_return = PortInvType(requestData)
        const port_save_return = PortSaveType(requestData)

        const ratioData = {
            answer: answerId,
            low_ratio: risk_port_return.risk_low,
            med_low_ratio: risk_port_return.risk_m_low,
            med_ratio: risk_port_return.risk_m,
            med_high_ratio: risk_port_return.risk_m_high,
            high_ratio: risk_port_return.risk_high,
            saving_ratio: save_inv_return.saving_score,
            inv_ratio: save_inv_return.inv_score,
            dom_stock_ratio: port_inv_return.dom_stock_score,
            int_stock_ratio: port_inv_return.int_stock_score,
            bond_ratio: port_inv_return.bond_score,
            alt_invest_ratio: port_inv_return.alt_invest_score,
            inst_save_ratio: port_save_return.inst_save_score,
            reg_save_ratio: port_save_return.reg_save_score,
        }

        const response = await store.savePortfolioResult(answerId, ratioData)
        
        // 결과 페이지로 이동
        router.push({
            name: 'portresult',
            params: { 
                answerId: answerId.toString()
            }
        })
    } catch (error) {
        console.error('Error saving ratio:', error)
        throw error
    }
}

// store의 savePortfolioResult 함수도 수정
const savePortfolioResult = async (answerId, ratioData) => {
    try {
        const response = await axios({
            method: 'post',
            url: `${API_URL}/financial_products/save_ratio/${answerId}/`,
            data: ratioData,
            headers: {
                'Authorization': `Token ${token.value}`,
                'Content-Type': 'application/json'
            }
        })
        console.log('포트폴리오 결과 장 성공:', response.data)
        return response.data
    } catch (error) {
        console.error('포트폴리오 결과 저장 실패:', error)
        if (error.response) {
            console.error('Server error details:', error.response.data)
        }
        throw error
    }
}

const riskPort = function (requestData) {
    let risk_low = 0
    let risk_m_low = 0
    let risk_m = 0
    let risk_m_high = 0
    let risk_high = 0
    
    const term = requestData.q2_goal_duration
    const important = requestData.q5_investment_priority
    const emerMoney = requestData.q4_emergency_fund_status
    const safeUtility = requestData.q6_safety_or_liquidity
    const goalMoney = requestData.q1_expected_goal_amount
    const job = requestData.q3_income_source
    const family = requestData.q7_household_status
    console.log(term)
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

// watch를 추가하여 route params 변경 감지
watch(
  () => route.params.id,
  (newId) => {
    currentQuestionIndex.value = parseInt(newId) - 1;
  }
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
  background-color: #E9EAEC;
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
  background-color: #90ADC6;
  border-color: #90ADC6;
}

/* Next 버튼 스타일 */
.next-button-container {
  margin-top: 20px;
}

.next-button {
  background-color: #90ADC6;
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
  background-color: #6196c4;
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
  background-color: #333652;
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
  