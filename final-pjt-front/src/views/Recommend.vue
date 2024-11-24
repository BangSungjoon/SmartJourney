<template>
  <section class="hero-section fade-in-fwd">
      <div class="hero-content slide-top">
        <p class="hero-subtitle">은행 상품 찾기</p>
        <h1 class="hero-title">
          <span class="highlight">은행</span>을 선택하여 </h1>
          <h1 class="hero-title">
          <span class="highlight">예금 및 적금 상품</span>을 확인하세요.
        </h1>
        <!-- 은행 선택 드롭다운 -->
     <div class="dropdown-section">
       <select id="bank-select" v-model="selectedBank" @change="fetchBankProducts" class="dropdown">
         <option value="" disabled selected>은행을 선택하세요</option>
         <option v-for="(bank, index) in bankName" :key="index" :value="bank">{{ bank }}</option>
       </select>
     </div>
      </div>
    </section>



  <div class="container">

    <!-- 결과 테이블 -->
    <section v-if="bankInfo.length" class="results fade-in-fwd">
      <h2 class="results-title">{{ selectedBank }}의 상품 정보</h2>
      <table class="table">
        <thead>
          <tr>
            <th>No</th>
            <th>상품 명</th>
            <th>적립 유형</th>
            <th>예치 기간</th>
            <th>저축 금리</th>
            <th>최고 우대 금리</th>
            <th>상세보기</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(row, index) in bankInfo" :key="row.id">
            <!-- Main row -->
            <tr>
                <th scope="row" :rowspan="(row.depositoptions_set?.length || 0) + (row.savingoptions_set?.length || 0) + 1">
                    {{ index + 1 }}
                </th>
                <!-- <td :rowspan="(row.depositoptions_set?.length || 0) + (row.savingoptions_set?.length || 0) + 1">
                    {{ row.kor_co_nm }}
                </td> -->
            
                <td :rowspan="(row.depositoptions_set?.length || 0) + (row.savingoptions_set?.length || 0) + 1">
                    {{ row.fin_prdt_nm }}
                </td>
    

            </tr>

            <!-- depositoptions_set 렌더링 -->
             <tr v-for="(option, subindex) in row.depositoptions_set || []" :key="'deposit-' + subindex">
                <!-- 예금은 첫 번째 항목에서만 표시 -->
                <td v-if="subindex === 0">예금</td>
                <td v-else></td>
                <td>{{ option.save_trm }}개월</td>
                <td>{{ option.intr_rate }} %</td>
                <td>{{ option.intr_rate2 }} %</td>
                <td v-if="subindex === 0">DETAIL</td>
                <td v-else></td>
                <!-- <RouterLink :to="{ name: 'productDetail', params: { id: option.fin_prdt_cd} }">detail</RouterLink> -->
                <!-- <button>detail</button> -->
                <!-- <td>{{ row.join_member }}</td> -->
                <!-- <td class="ellipsis">{{ row.spcl_cnd }}</td> -->
            </tr>

            <!-- savingoptions_set 렌더링 -->
            <tr v-for="(option, subindex) in row.savingoptions_set || []" :key="'saving-' + subindex">
                <!-- 적립 유형은 첫 번째 항목에서만 표시 -->
                <td v-if="subindex === 0">{{ option.rsrv_type_nm }}</td>
                <td v-else></td>
                <td>{{ option.save_trm }}개월</td>
                <td>{{ option.intr_rate }} %</td>
                <td>{{ option.intr_rate2 }} %</td>
                <td v-if="subindex === 0">DETAIL</td>
                <td v-else></td>
                <!-- <RouterLink :to="{ name: 'productDetail', params: { id: option.fin_prdt_cd} }">detail</RouterLink> -->
                <!-- <td>{{ row.join_member }}</td> -->
                <!-- <td class="ellipsis">{{ row.spcl_cnd }}</td> -->
            </tr>
        </template>

        </tbody>
      </table>
    </section>

    <!-- 데이터 없음 -->
    <section v-else class="no-results">
      <p>은행을 선택하여 상품 정보를 확인하세요.</p>
    </section>
  </div>
</template>



<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useFinStore } from "@/stores/counter";

const store = useFinStore();
const bankName = ref([]); // 은행 목록
const bankInfo = ref([]); // 선택된 은행의 상품 정보
const selectedBank = ref(""); // 선택된 은행 이름

// 데이터 로드
onMounted(() => {
  axios
    .get(`${store.API_URL}/financial_products/save_deposit/`)
    .then((response) => {
      bankName.value = [...new Set(response.data.result.baseList.map((item) => item.kor_co_nm))];
    })
    .catch((error) => {
      console.error("은행 목록 로드 실패:", error);
    });
});

// 상품 정보 요청
const fetchBankProducts = function (event) {
    const selectedValue = event.currentTarget.value
    Promise.all([
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/recommend_deposit/`,
            params: {
                bank:selectedValue
            }
        }),
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/recommend_savings/`,
            params: {
                bank:selectedValue
            }
        })
    ])
    .then(([depositResponse, savingsResponse]) => {
        // console.log("Deposit Data:", depositResponse.data)
        // console.log("Savings Data:", savingsResponse.data)
        bankInfo.value = [
        ...depositResponse.data, // 예금 데이터
        ...savingsResponse.data, // 적금 데이터
        ];
    }) 
}
</script>

<style scoped>

/* Hero Section 스타일 */
.hero-section {
    display: flex;
    justify-content: center; /* 가로 중앙 정렬 */
    align-items: center; /* 세로 중앙 정렬 */
    text-align: center; /* 텍스트 중앙 정렬 */
    height: 100vh; /* 화면 전체 높이 */
    background-image: url('@/assets/images/shared/city2.jpg'); /* 배경 이미지 경로 */
    background-size: cover; /* 배경 크기 */
    background-position: center; /* 배경 위치 */
    background-repeat: no-repeat; /* 배경 반복 금지 */
    color: white; /* 기본 글자 색상 */
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  /* 콘텐츠 스타일 */
  .hero-content {
    max-width: 800px; /* 컨텐츠 최대 너비 */
    padding: 20px; /* 모바일 뷰에서도 여백 확보 */
  }
  
  /* 텍스트 스타일 */
  .hero-subtitle {
    font-size: 2rem;
    margin-bottom: 30px;
    color: #f1f1f1;
  }
  
  .hero-title {
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .hero-title .highlight {
    color: #ffd700; /* 강조 텍스트 색상 */
  }
  
  .hero-description {
    font-size: 1.5rem;
    line-height: 1.6;
    margin-bottom: 30px;
  }



.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Noto Sans KR", sans-serif;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1rem;
  color: #666;
}

.dropdown-section {
  text-align: center;
  margin-bottom: 20px;
}

.dropdown-label {
  font-size: 1.2rem;
  margin-right: 10px;
}

.dropdown {
  font-size: 1rem;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;



  appearance: none; /* 기본 스타일 제거 (브라우저 호환) */
  position: relative; /* 기본 위치 */
}

.results-title {
  margin: 20px 0;
  font-size: 1.5rem;
  text-align: left;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table th,
.table td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: center;
}

.table th {
  background-color: #f4f4f4;
}

.no-results {
  text-align: center;
  margin-top: 30px;
  font-size: 1.2rem;
  color: #888;
}

.fade-in-fwd {
	-webkit-animation: fade-in-fwd 1s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
	        animation: fade-in-fwd 1s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
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

</style>
