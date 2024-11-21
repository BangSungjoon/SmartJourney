<template>
    <div>
        <h3>추천 리스트</h3>
        <select class="form-select" aria-label="Default select example" @change.prevent="selectBank">
            <option selected disabled>은행</option>
            <option v-for="(name, index) in bankName" :key="name.id">{{ name }}</option>
         

            <!-- <option v-for="ex in exchange" :key="ex.id" :value="ex.cur_nm" @click="click(ex.id)">{{ ex.cur_nm }}</option> -->

        </select>

        <table class="table">
    <thead>
        <tr>
            <th scope="col">No</th>
            <th scope="col">금융 회사 명</th>
            <th scope="col">상품 명</th>
            <th scope="col">적립 유형</th>
            <th scope="col">예치 기간</th>
            <th scope="col">저축 금리</th>
            <th scope="col">최고 우대 금리</th>
            <th scope="col">가입 대상</th>
            <th scope="col">우대 조건</th>
        </tr>
    </thead>
    <tbody>
        <template v-for="(row, index) in bankInfo" :key="row.id">
            <!-- Main row -->
            <tr>
                <th scope="row" :rowspan="(row.depositoptions_set?.length || 0) + (row.savingoptions_set?.length || 0) + 1">
                    {{ index + 1 }}
                </th>
                <td :rowspan="(row.depositoptions_set?.length || 0) + (row.savingoptions_set?.length || 0) + 1">
                    {{ row.kor_co_nm }}
                </td>
                <td :rowspan="(row.depositoptions_set?.length || 0) + (row.savingoptions_set?.length || 0) + 1">
                    {{ row.fin_prdt_nm }}
                </td>
            </tr>

            <!-- depositoptions_set 렌더링 -->
             <!-- depositoptions_set 렌더링 -->
             <tr v-for="(option, subindex) in row.depositoptions_set || []" :key="'deposit-' + subindex">
                <!-- 예금은 첫 번째 항목에서만 표시 -->
                <td v-if="subindex === 0">예금</td>
                <td v-else></td>
                <td>{{ option.save_trm }}개월</td>
                <td>{{ option.intr_rate }} %</td>
                <td>{{ option.intr_rate2 }} %</td>
                <td>{{ row.join_member }}</td>
                <td class="ellipsis">{{ row.spcl_cnd }}</td>
            </tr>

            <!-- savingoptions_set 렌더링 -->
            <tr v-for="(option, subindex) in row.savingoptions_set || []" :key="'saving-' + subindex">
                <!-- 적립 유형은 첫 번째 항목에서만 표시 -->
                <td v-if="subindex === 0">{{ option.rsrv_type_nm }}</td>
                <td v-else></td>
                <td>{{ option.save_trm }}개월</td>
                <td>{{ option.intr_rate }} %</td>
                <td>{{ option.intr_rate2 }} %</td>
                <td>{{ row.join_member }}</td>
                <td class="ellipsis">{{ row.spcl_cnd }}</td>
            </tr>
        </template>
    </tbody>
</table>

    </div>
</template>

<script setup>
import axios from 'axios';
import { useFinStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
const store = useFinStore()
const bankInfo = ref([])
const bankName = ref([])

// 이름 등록
onMounted( ()=> {
    createRecommend()
    axios({
        method:'get',
        url:`${store.API_URL}/financial_products/save_deposit/`,
    })
    .then((response)=> {
        // console.log(response.data.result.baseList)

        bankName.value = [...new Set(response.data.result.baseList.map((item)=>item.kor_co_nm))] 
    //    console.log(bankName.value)
    })
})

const createRecommend = function () {
    axios({
        method:'get',
        url:`${store.API_URL}/financial_products/save_deposit_savings/`,
    })
}

// 예금 상품 조회, 적금 상품 조회
const selectBank = function (event) {
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
        console.log("Deposit Data:", depositResponse.data)
        console.log("Savings Data:", savingsResponse.data)
        bankInfo.value = [
        ...depositResponse.data, // 예금 데이터
        ...savingsResponse.data, // 적금 데이터
        ];
        console.log("bankInfo Data:", bankInfo.value)
    }) 
}

// const depositRecommend = function (selectedValue) {
//     axios({
//         method:'get',
//         url:`${store.API_URL}/financial_products/recommend_savings/`,
//         params: {
//             bank:selectedValue
//         }
//     })
//     .then((response) => {
//         bankInfo.value.push(response.data) 
//         console.log(bankInfo)
//     })
// }

</script>

<style scoped>

.ellipsis {
    max-width: 150px; /* 최대 너비 설정 */
    white-space: nowrap; /* 텍스트 줄바꿈 방지 */
    overflow: hidden; /* 넘치는 텍스트 숨김 */
    text-overflow: ellipsis; /* 줄임표(...) 표시 */
}

</style>