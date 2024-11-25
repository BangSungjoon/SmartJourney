<template>
    <div>
        <div class="form-text" id="basic-addon4">옌화와 인도네시아 루피아는 100 단위입니다.</div>
        <div class="input-group mb-3">
            <select class="form-select bg-light custom-select" @change="choice" v-model="selectedExchange">
                <option disabled value="">어디로 떠나볼까요?</option>
                <option v-for="ex in exchange" :key="ex.id" :value="ex.id">{{ ex.cur_nm }}</option>
            </select>
            <span class="input-group-text custom-span">{{ selectCountry }}</span>
            <input type="text" class="form-control custom-input" v-model="foreignMoney" @input="updateKorMoney">
        </div>

        <div class="input-group">
            <input type="text" class="form-control custom-input" v-model="korMoney" @input="updateForeignMoney">
            <span class="input-group-text custom-span">KRW</span>
        </div>
    </div>
</template>


<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useFinStore } from '@/stores/counter'

const store = useFinStore()
const exchange = ref([])
const foreignMoney = ref(1)
const korMoney = ref(0)
const selectedExchange = ref('')  // 선택된 exchange 값 저장
const selectCountry = ref('')

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/financial_products/exchange/`
    })
        .then((res) => {
            console.log(res.data)
            exchange.value = res.data
            // exchange 목록이 로드되면 첫 번째 항목을 기본값으로 설정
            selectedExchange.value = exchange.value[exchange.value.length - 1].id
            selectCountry.value = exchange.value[exchange.value.length - 1].cur_unit
            choice()  // 기본값에 대한 환율 계산
        })
        .catch(err => console.log(err))
})

const choice = function () {
    console.log(selectedExchange.value)
    const country = exchange.value.find(ex => ex.id == selectedExchange.value)
    const dealBasR = parseFloat(country.deal_bas_r.replace(/,/g, ''))
    console.log(dealBasR)
    korMoney.value = foreignMoney.value*dealBasR
    selectCountry.value = country.cur_unit
}
const updateKorMoney = () => {
  const rate = getRate();
  korMoney.value = (foreignMoney.value * rate).toFixed(2);
};

const updateForeignMoney = () => {
  const rate = getRate();
  foreignMoney.value = (korMoney.value / rate).toFixed(2);
};

const getRate = () => {
  const selected = exchange.value.find(ex => ex.id === selectedExchange.value);
  return parseFloat(selected.deal_bas_r.replace(/,/g, ''));
};
</script>

<style scoped>
/* 높이를 조정하는 CSS */
.custom-select, .custom-input, .custom-span {
    height: 48px; /* 기본 Bootstrap보다 큰 높이로 설정 */
    font-size: 16px; /* 텍스트 크기 조정 */
}

.custom-input {
    padding: 10px; /* 입력 필드의 여백 조정 */
}

.custom-span {
    display: flex;
    align-items: center; /* 텍스트를 수직 중앙 정렬 */
    height: 48px; /* 동일한 높이로 설정 */
}
</style>
