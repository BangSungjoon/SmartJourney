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
            <th scope="col"></th>
            <th scope="col">금융 회사 명</th>
            <th scope="col">상품 명</th>
            <th scope="col">예치 기간</th>
            <th scope="col">저축 금리</th>
            <th scope="col">최고 우대 금리</th>        
            </tr>
        </thead>
        <tbody>
            <template v-for="(row, index) in bankInfo" :key="row.id">
                <tr>
                <th scope="row" :rowspan="row.depositoptions_set.length + 1">{{ index+1 }}</th>
                    <td :rowspan="row.depositoptions_set.length + 1">{{ row.kor_co_nm }}</td>
                    <td :rowspan="row.depositoptions_set.length + 1">{{ row.fin_prdt_nm }}</td>
                </tr>

                <tr v-for="(option, subindex) in row.depositoptions_set" :key="subindex.id">
                    <td>{{ option.save_trm }}개월</td>
                    <td>{{ option.intr_rate }} %</td>
                    <td>{{ option.intr_rate2 }} %</td>

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
        console.log(response.data.result.baseList)

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



// 상품 조회
const selectBank = function (event) {
    const selectedValue = event.currentTarget.value
    axios({
        method:'get',
        url:`${store.API_URL}/financial_products/recommend_deposit/`,
        params: {
            bank:selectedValue
        }
    })
    .then((response) => {
      // 화면에 li로 출력
      bankInfo.value = response.data
    console.log(bankInfo)
    })
}

</script>

<style scoped>

</style>