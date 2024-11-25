<template>
  <div class="subsidy-survey">
    <h2>맞춤형 보조금 찾기</h2>
    
    <!-- 진행 상태 표시 -->
    <div class="progress-bar">
      <div :style="{ width: `${(currentStep/totalSteps) * 100}%` }" class="progress"></div>
    </div>

    <!-- 단계별 질문 -->
    <div class="question-container" v-if="!surveyComplete">
      <!-- 기본 정보 -->
      <div v-if="currentStep === 1" class="question-section">
        <h3>기본 정보를 입력해주세요</h3>
        <div class="form-group">
          <label>출생연도</label>
          <input 
            type="number" 
            v-model="userAnswers.birth_year" 
            placeholder="예: 1990"
            min="1"
            :max="new Date().getFullYear()"
            @input="validateBirthYear"
          >
        </div>
        <div class="form-group">
          <label>성별</label>
          <select v-model="userAnswers.gender">
            <option value="male">남성</option>
            <option value="female">여성</option>
          </select>
        </div>
      </div>

      <!-- 소득 수준 -->
      <div v-if="currentStep === 2" class="question-section">
        <h3>가구의 소득 수준을 선택해주세요</h3>
        <div class="form-group">
          <select v-model="userAnswers.income_level">
            <option value="0-50">중위소득 0~50%</option>
            <option value="51-75">중위소득 51~75%</option>
            <option value="76-100">중위소득 76~100%</option>
            <option value="101-200">중위소득 101~200%</option>
            <option value="200+">중위소득 200% 초과</option>
          </select>
        </div>
      </div>

      <!-- 생애주기 상태 -->
      <div v-if="currentStep === 3" class="question-section">
        <h3>해당하는 항목을 모두 선택해주세요</h3>
        <div class="checkbox-group">
          <label>
            <input type="checkbox" v-model="userAnswers.is_expecting">
            예비부모/난임
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_pregnant">
            임산부
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_birth">
            출산/입양
          </label>
        </div>
      </div>

      <!-- 직업 상태 -->
      <div v-if="currentStep === 4" class="question-section">
        <h3>현재 직업 상태를 선택해주세요</h3>
        <div class="form-group">
          <select v-model="userAnswers.occupation">
            <option value="farmer">농업인</option>
            <option value="fisher">어업인</option>
            <option value="livestock">축산업인</option>
            <option value="forester">임업인</option>
            <option value="employed">근로자/직장인</option>
            <option value="unemployed">구직자/실업자</option>
            <option value="other">기타</option>
          </select>
        </div>
      </div>

      <!-- 학생 여부 -->
      <div v-if="currentStep === 5" class="question-section">
        <h3>학생이신가요?</h3>
        <div class="form-group">
          <select v-model="userAnswers.student_status">
            <option value="none">해당없음</option>
            <option value="elementary">초등학생</option>
            <option value="middle">중학생</option>
            <option value="high">고등학생</option>
            <option value="college">대학생/대학원생</option>
          </select>
        </div>
      </div>

      <!-- 가구 형태 -->
      <div v-if="currentStep === 6" class="question-section">
        <h3>해당하는 가구 형태를 모두 선택해주세요</h3>
        <div class="checkbox-group">
          <label>
            <input type="checkbox" v-model="userAnswers.is_multicultural">
            다문화가족
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_north_defector">
            북한이탈주민
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_single_parent">
            한부모가정
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_single_person">
            1인가구
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_many_children">
            다자녀가구
          </label>
        </div>
      </div>

      <!-- 주거 상태 -->
      <div v-if="currentStep === 7" class="question-section">
        <h3>주거 상태를 선택해주세요</h3>
        <div class="checkbox-group">
          <label>
            <input type="checkbox" v-model="userAnswers.is_no_house">
            무주택세대
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_new_resident">
            신규전입
          </label>
        </div>
      </div>

      <!-- 사업자 정보 -->
      <div v-if="currentStep === 8" class="question-section">
        <h3>사업자 정보를 선택해주세요</h3>
        <div class="form-group">
          <label>사업자 상태</label>
          <select v-model="userAnswers.business_status">
            <option value="none">해당없음</option>
            <option value="prospective">예비창업자</option>
            <option value="operating">영업중</option>
            <option value="closing">폐업예정자</option>
          </select>
        </div>
        <div class="form-group" v-if="userAnswers.business_status !== 'none'">
          <label>사업 분야</label>
          <select v-model="userAnswers.business_type">
            <option value="none">해당없음</option>
            <option value="food">음식점업</option>
            <option value="manufacturing">제조업</option>
            <option value="it">정보통신업</option>
            <option value="other">기타업종</option>
          </select>
        </div>
      </div>

      <!-- 특수 조건 -->
      <div v-if="currentStep === 9" class="question-section">
        <h3>해당하는 항목을 모두 선택해주세요</h3>
        <div class="checkbox-group">
          <label>
            <input type="checkbox" v-model="userAnswers.is_disabled">
            장애인
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_veteran">
            국가보훈대상자
          </label>
          <label>
            <input type="checkbox" v-model="userAnswers.is_patient">
            질병/질환자
          </label>
        </div>
      </div>

      <!-- 네비게이션 버튼 -->
      <div class="navigation-buttons">
        <button @click="prevStep" v-if="currentStep > 1">이전</button>
        <button @click="nextStep" v-if="currentStep < totalSteps">다음</button>
        <button @click="submitSurvey" v-if="currentStep === totalSteps">제출</button>
      </div>
    </div>

    <!-- 완료 메시지와 결과 표시 -->
    <div v-else>
      <div class="completion-message">
        <h3>설문이 완료되었습니다!</h3>
        <p>입력하신 정보를 바탕으로 맞춤형 보조금을 찾아드렸습니다.</p>
      </div>
      <MySubsidy />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useFinStore } from '@/stores/counter'
import axios from 'axios'
import MySubsidy from '@/components/MySubsidy.vue'
onMounted(() => {
  Promise.all([
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/subsidy_list_save/`,
        }),
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/subsidy_detail_save/`,          
        }),
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/support_conditions_save/`,
        }),
    ])
    .then(res=>{
      console.log('성공')
    })
    .catch(err => {
      console.log(err)
    })
});




const store = useFinStore()
const currentStep = ref(1)
const totalSteps = 9
const surveyComplete = ref(false)

const userAnswers = ref({
  birth_year: null,
  gender: '',
  income_level: '',
  is_expecting: false,
  is_pregnant: false,
  is_birth: false,
  occupation: '',
  student_status: 'none',
  is_multicultural: false,
  is_north_defector: false,
  is_single_parent: false,
  is_single_person: false,
  is_many_children: false,
  is_no_house: false,
  is_new_resident: false,
  business_status: 'none',
  business_type: 'none',
  is_disabled: false,
  is_veteran: false,
  is_patient: false
})

const nextStep = () => {
  // 각 단계별 필수 입력 검사
  if (currentStep.value === 1) {
    if (!userAnswers.value.birth_year || userAnswers.value.birth_year <= 0) {
      alert('올바른 출생연도를 입력해주세요')
      return
    }
    if (!userAnswers.value.gender) {
      alert('성별을 선택해주세요')
      return
    }
  }
  
  if (currentStep.value === 2) {
    if (!userAnswers.value.income_level) {
      alert('가구의 소득 수준을 선택해주세요')
      return
    }
  }
  
  if (currentStep.value === 4) {
    if (!userAnswers.value.occupation) {
      alert('현재 직업 상태를 선택해주세요')
      return
    }
  }

  if (currentStep.value < totalSteps) {
    currentStep.value++
  }
}

const prevStep = () => {
  if (currentStep.value > 1) {
    currentStep.value--
  }
}

const submitSurvey = function () {
    // 최종 제출 전 필수 항목 검사
    if (!userAnswers.value.birth_year || userAnswers.value.birth_year <= 0) {
        alert('올바른 출생연도를 입력해주세요')
        return
    }
    if (!userAnswers.value.gender) {
        alert('성별을 선택해주세요')
        return
    }
    if (!userAnswers.value.income_level) {
        alert('가구의 소득 수준을 선택해주세요')
        return
    }
    if (!userAnswers.value.occupation) {
        alert('현재 직업 상태를 선택해주세요')
        return
    }

    const token = store.token
    const headers = {
        'Authorization': `Token ${token}`,
    };

    axios({
        method: 'post',
        url: `${store.API_URL}/financial_products/user_conditions_save/`,
        data: userAnswers.value,
        headers: headers
    }).then(() => {
        console.log('유저 조건 저장 성공')
        surveyComplete.value = true
    }).catch(err => {
        console.error('에러 상세:', err.response?.data)
        alert('저장 중 오류가 발생했습니다. 필수 항목을 모두 입력했는지 확인해주세요.')
    })
}

const validateBirthYear = () => {
  if (userAnswers.value.birth_year <= 0) {
    userAnswers.value.birth_year = null
  }
  if (userAnswers.value.birth_year > new Date().getFullYear()) {
    userAnswers.value.birth_year = new Date().getFullYear()
  }
}
</script>

<style scoped>
.subsidy-survey {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.subsidy-survey h2 {
  text-align: center;
  margin-bottom: 30px;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #eee;
  border-radius: 5px;
  margin-bottom: 30px;
}

.progress-bar .progress {
  height: 100%;
  background-color: #4CAF50;
  border-radius: 5px;
  transition: width 0.3s ease;
}

.question-section {
  margin-bottom: 30px;
}

.question-section h3 {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 10px;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 30px;
}

.navigation-buttons button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

.navigation-buttons button:hover {
  background-color: #45a049;
}

.completion-message {
  text-align: center;
  padding: 30px;
}

.completion-message h3 {
  margin-bottom: 15px;
}
</style>