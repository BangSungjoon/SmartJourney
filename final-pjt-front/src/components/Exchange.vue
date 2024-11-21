<template>
    <div>
        <div class="form-text" id="basic-addon4">옌화와 인도네시아 루피아는 100 단위입니다.</div>
        <div class="input-group mb-3">
            <select class="form-select bg-light" @change="choice" v-model="selectedExchange">
                <option disabled value="">어디로 떠나볼까요?</option>
                <option v-for="ex in exchange" :key="ex.id" :value="ex.id">{{ ex.cur_nm }}</option>
            </select>
            <span class="input-group-text">{{ selectCountry }}</span>
            <input type="text" class="form-control" v-model="foreignMoney" @input="updateKorMoney">
        </div>

        <div class="input-group">
            <input type="text" class="form-control" v-model="korMoney" @input="updateForeignMoney">
            <span class="input-group-text">KRW</span>
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

// foreignMoney 값이 변경될 때마다 korMoney 값을 갱신하도록 watch 추가
// watch(foreignMoney, (newVal, oldVal) => {
//     if (selectedExchange.value) {
//         const country = exchange.value.find(ex => ex.id == selectedExchange.value)
//         const dealBasR = parseFloat(country.deal_bas_r.replace(/,/g, ''))
//         korMoney.value = newVal * dealBasR
//     }
// })

// // korMoney 값이 변경될 때마다 foreignMoney 값을 갱신
// watch(korMoney, (newVal, oldVal) => {
//     if (selectedExchange.value) {
//         const country = exchange.value.find(ex => ex.id == selectedExchange.value)
//         const dealBasR = parseFloat(country.deal_bas_r.replace(/,/g, ''))
//         foreignMoney.value = newVal / dealBasR
//     }
// })
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

</style>