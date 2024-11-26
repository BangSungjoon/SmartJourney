<template>
  <div class="subsidy-survey">
    
    

    <!-- 단계별 질문 -->
    <div class="question-container" v-if="!surveyComplete">
      <!-- 기본 정보 -->
      <div v-if="currentStep === 1" class="question-section input-wrapper">
        <h3>기본 정보를 입력해주세요</h3>
        <div class="form-group">
          <label>출생연도</label>
          <input 
            type="number" 
            v-model="userAnswers.birth_year" 
            class="form-control"
            placeholder="예: 1990"
            min="1"
            :max="new Date().getFullYear()"
            @input="validateBirthYear"
          >
        </div>
        <div class="form-group radio-options-container">
          <label>성별</label>
          <div class="radio-option">
            <input
              type="radio"
              id="male"
              value="male"
              v-model="userAnswers.gender"
            />
            <label for="male">남성</label>
          </div>
          <div class="radio-option">
            <input
              type="radio"
              id="female"
              value="female"
              v-model="userAnswers.gender"
            />
            <label for="female">여성</label>
          </div>
        </div>
      </div>

      <!-- 소득 수준 -->
      <div v-if="currentStep === 2" class="question-section">
        <h3>가구의 소득 수준을 선택해주세요</h3>
        <div class="radio-options-container">
          <div class="radio-option">
            <input
              type="radio"
              id="income-0-50"
              value="0-50"
              v-model="userAnswers.income_level"
            />
            <label for="income-0-50">중위소득 0~50%</label>
          </div>
          <div class="radio-option">
            <input
              type="radio"
              id="income-51-75"
              value="51-75"
              v-model="userAnswers.income_level"
            />
            <label for="income-51-75">중위소득 51~75%</label>
          </div>
          <div class="radio-option">
            <input
              type="radio"
              id="income-76-100"
              value="76-100"
              v-model="userAnswers.income_level"
            />
            <label for="income-76-100">중위소득 76~100%</label>
          </div>
          <div class="radio-option">
            <input
              type="radio"
              id="income-101-200"
              value="101-200"
              v-model="userAnswers.income_level"
            />
            <label for="income-101-200">중위소득 101~200%</label>
          </div>
          <div class="radio-option">
            <input
              type="radio"
              id="income-200-plus"
              value="200+"
              v-model="userAnswers.income_level"
            />
            <label for="income-200-plus">중위소득 200% 초과</label>
          </div>
        </div>
      </div>


      <!-- 생애주기 상태 -->
      <div v-if="currentStep === 3" class="question-section">
        <h3>해당하는 항목을 모두 선택해주세요</h3>
        <div class="checkbox-options-container">
          <div class="checkbox-option">
            <input
              type="checkbox"
              id="expecting"
              v-model="userAnswers.is_expecting"
            />
            <label for="expecting">예비부모/난임</label>
          </div>
          <div class="checkbox-option">
            <input
              type="checkbox"
              id="pregnant"
              v-model="userAnswers.is_pregnant"
            />
            <label for="pregnant">임산부</label>
          </div>
          <div class="checkbox-option">
            <input
              type="checkbox"
              id="birth"
              v-model="userAnswers.is_birth"
            />
            <label for="birth">출산/입양</label>
          </div>
        </div>
      </div>


     <!-- 직업 상태 -->
    <div v-if="currentStep === 4" class="question-section">
      <h3>현재 직업 상태를 선택해주세요</h3>
      <div class="radio-options-grid">
        <div class="radio-option">
          <input type="radio" id="farmer" value="farmer" v-model="userAnswers.occupation" />
          <label for="farmer">농업인</label>
        </div>
        <div class="radio-option">
          <input type="radio" id="fisher" value="fisher" v-model="userAnswers.occupation" />
          <label for="fisher">어업인</label>
        </div>
        <div class="radio-option">
          <input type="radio" id="livestock" value="livestock" v-model="userAnswers.occupation" />
          <label for="livestock">축산업인</label>
        </div>
        <div class="radio-option">
          <input type="radio" id="forester" value="forester" v-model="userAnswers.occupation" />
          <label for="forester">임업인</label>
        </div>
        <div class="radio-option">
          <input type="radio" id="employed" value="employed" v-model="userAnswers.occupation" />
          <label for="employed">근로자/직장인</label>
        </div>
        <div class="radio-option">
          <input type="radio" id="unemployed" value="unemployed" v-model="userAnswers.occupation" />
          <label for="unemployed">구직자/실업자</label>
        </div>
        <div class="radio-option">
          <input type="radio" id="other" value="other" v-model="userAnswers.occupation" />
          <label for="other">기타</label>
        </div>
      </div>
    </div>


      <!-- 학생 여부 -->
      <div v-if="currentStep === 5" class="question-section">
        <h3>학생이신가요?</h3>
        <div class="radio-options-container">
          <div class="radio-option">
            <input type="radio" id="none" value="none" v-model="userAnswers.student_status" />
            <label for="none">해당없음</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="elementary" value="elementary" v-model="userAnswers.student_status" />
            <label for="elementary">초등학생</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="middle" value="middle" v-model="userAnswers.student_status" />
            <label for="middle">중학생</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="high" value="high" v-model="userAnswers.student_status" />
            <label for="high">고등학생</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="college" value="college" v-model="userAnswers.student_status" />
            <label for="college">대학생/대학원생</label>
          </div>
        </div>
      </div>

      <!-- 가구 형태 -->
      <div v-if="currentStep === 6" class="question-section">
        <h3>해당하는 가구 형태를 모두 선택해주세요</h3>
        <div class="checkbox-options-container">
          <div class="checkbox-option">
            <input type="checkbox" id="multicultural" v-model="userAnswers.is_multicultural" />
            <label for="multicultural">다문화가족</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="north_defector" v-model="userAnswers.is_north_defector" />
            <label for="north_defector">북한이탈주민</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="single_parent" v-model="userAnswers.is_single_parent" />
            <label for="single_parent">한부모가정</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="single_person" v-model="userAnswers.is_single_person" />
            <label for="single_person">1인가구</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="many_children" v-model="userAnswers.is_many_children" />
            <label for="many_children">다자녀가구</label>
          </div>
        </div>
      </div>

      <!-- 주거 상태 -->
      <div v-if="currentStep === 7" class="question-section">
        <h3>주거 상태를 선택해주세요</h3>
        <div class="checkbox-options-container">
          <div class="checkbox-option">
            <input type="checkbox" id="no_house" v-model="userAnswers.is_no_house" />
            <label for="no_house">무주택세대</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="new_resident" v-model="userAnswers.is_new_resident" />
            <label for="new_resident">신규전입</label>
          </div>
        </div>
      </div>

            <!-- 사업자 정보 -->
      <div v-if="currentStep === 8" class="question-section">
        <h3>사업자 정보를 선택해주세요</h3>
        <div class="radio-options-grid">
          <div class="radio-option">
            <input type="radio" id="none-business" value="none" v-model="userAnswers.business_selection" />
            <label for="none-business">해당없음</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="prospective" value="prospective" v-model="userAnswers.business_selection" />
            <label for="prospective">예비창업자</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="operating" value="operating" v-model="userAnswers.business_selection" />
            <label for="operating">영업중</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="closing" value="closing" v-model="userAnswers.business_selection" />
            <label for="closing">폐업예정자</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="food" value="food" v-model="userAnswers.business_selection" />
            <label for="food">음식점업</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="manufacturing" value="manufacturing" v-model="userAnswers.business_selection" />
            <label for="manufacturing">제조업</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="it" value="it" v-model="userAnswers.business_selection" />
            <label for="it">정보통신업</label>
          </div>
          <div class="radio-option">
            <input type="radio" id="other-business" value="other" v-model="userAnswers.business_selection" />
            <label for="other-business">기타업종</label>
          </div>
        </div>
      </div>


      <!-- 특수 조건 -->
      <div v-if="currentStep === 9" class="question-section">
        <h3>해당하는 항목을 모두 선택해주세요</h3>
        <div class="checkbox-options-container">
          <div class="checkbox-option">
            <input type="checkbox" id="disabled" v-model="userAnswers.is_disabled" />
            <label for="disabled">장애인</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="veteran" v-model="userAnswers.is_veteran" />
            <label for="veteran">국가보훈대상자</label>
          </div>
          <div class="checkbox-option">
            <input type="checkbox" id="patient" v-model="userAnswers.is_patient" />
            <label for="patient">질병/질환자</label>
          </div>
        </div>
      </div>

      <!-- 네비게이션 버튼 -->
      <div class="navigation-buttons">
        <button @click="prevStep" v-if="currentStep > 1">이전</button>
        <button @click="nextStep" v-if="currentStep < totalSteps">다음</button>
        <button @click="submitSurvey" v-if="currentStep === totalSteps">제출</button>
      </div>
   <!-- 진행 상태 표시 -->
   <div class="progress-container">
        <div class="progress-bar">
          <div
            class="progress"
            :style="{ width: (currentStep / 9) * 100 + '%' }"
          ></div>
        </div>
        <p class="progress-text">{{ currentStep }} / 9</p>
      </div>
        <!-- 진행 상태 표시 -->
      </div>

      
      
      <!-- 완료 메시지와 결과 표시 -->
      <div v-else>
        <!-- <div class="completion-message"> -->
          <!-- <h3>설문이 완료되었습니다!</h3> -->
          <!-- <p>입력하신 정보를 바탕으로 맞춤형 보조금을 찾아드렸습니다.</p> -->
        <!-- </div> -->
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
/* 컨테이너 스타일 */
.question-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 화면 전체 높이 */
  text-align: center;
  background-color: #E9EAEC; /* 배경색 */
  font-family: 'Noto Sans KR', sans-serif;
  padding: 20px;
  box-sizing: border-box; /* 패딩 포함 크기 계산 */
}

/* 질문 제목 스타일 */
.question-section h3 {
  font-size: 2.5rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 30px;
}

.input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px; /* 출생연도와 성별 섹션 간 간격 */
  margin-bottom: 30px; /* 전체 섹션 아래 여백 */
}

.form-group {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 400px; /* 입력 필드의 최대 너비 */
  gap: 10px; /* 라벨과 입력 박스 간격 */
}

/* 라디오 옵션 컨테이너 */
.radio-options-container {
  display: flex;
  flex-direction: column;
  gap: 20px; /* 옵션 간격 */
  width: 100%;
  max-width: 600px; /* 전체 너비 제한 */
}

/* 라디오 옵션 스타일 */
.radio-option {
  display: flex;
  align-items: center;
  background-color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s, background-color 0.3s;
}

.radio-option:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

/* 라디오 버튼 숨김 및 커스텀 원 스타일 */
.radio-option input[type="radio"] {
  display: none; /* 기본 라디오 버튼 숨기기 */
}

.radio-option label {
  display: flex;
  align-items: center;
  gap: 10px; /* 원과 텍스트 간격 */
  font-size: 1rem;
  color: #333;
  cursor: pointer;
}

.radio-option label::before {
  content: '';
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-radius: 50%;
  transition: background-color 0.3s, border-color 0.3s;
}

/* 선택된 상태 스타일 */
.radio-option input[type="radio"]:checked + label::before {
  background-color: #90ADC6;
  border-color: #90ADC6;
}
/* 체크박스 옵션 컨테이너 */
.checkbox-options-container {
  display: flex;
  flex-direction: column;
  gap: 20px; /* 옵션 간격 */
  width: 100%;
  max-width: 600px; /* 전체 너비 제한 */
}

/* 체크박스 옵션 스타일 */
.checkbox-option {
  display: flex;
  align-items: center;
  background-color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s, background-color 0.3s;
}

.checkbox-option:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

/* 체크박스 숨기기 */
.checkbox-option input[type="checkbox"] {
  display: none; /* 기본 체크박스 숨김 */
}

/* 체크박스 커스텀 스타일 */
.checkbox-option label {
  display: flex;
  align-items: center;
  gap: 10px; /* 체크박스와 텍스트 간격 */
  font-size: 1rem;
  color: #333;
  cursor: pointer;
}

.checkbox-option label::before {
  content: '';
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-radius: 4px;
  transition: background-color 0.3s, border-color 0.3s;
}

/* 체크된 상태 */
.checkbox-option input[type="checkbox"]:checked + label::before {
  background-color: #90ADC6;
  border-color: #90ADC6;
}


/* 4개씩 두 줄로 나타내는 그리드 스타일 */
.radio-options-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 각 줄에 4개 */
  gap: 20px; /* 항목 간격 */
  width: 100%;
  max-width: 800px; /* 최대 너비 */
  margin: 20px auto; /* 가운데 정렬 */
}

/* 개별 라디오 버튼 스타일 */
.radio-option {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s, background-color 0.3s;
}

.radio-option:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

/* 숨겨진 라디오 버튼 */
.radio-option input[type="radio"] {
  display: none; /* 기본 라디오 버튼 숨김 */
}

/* 라벨 스타일 및 커스텀 원 */
.radio-option label {
  display: flex;
  align-items: center;
  gap: 10px; /* 원과 텍스트 간격 */
  font-size: 1rem;
  color: #333;
  cursor: pointer;
}

.radio-option label::before {
  content: '';
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-radius: 50%;
  transition: background-color 0.3s, border-color 0.3s;
}

/* 선택된 상태 */
.radio-option input[type="radio"]:checked + label::before {
  background-color: #90ADC6;
  border-color: #90ADC6;
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
/* 이전/다음 버튼 */
.navigation-buttons {
  display: flex;
  gap: 10px; /* 버튼 간격 */
  margin-top: 20px;
}

.navigation-buttons button {
  background-color: #90ADC6;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.navigation-buttons button:hover {
  background-color: #6196c4;
}

.navigation-buttons button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
.completion-message {
  font-family: 'Noto Sans KR', sans-serif;
}

</style>