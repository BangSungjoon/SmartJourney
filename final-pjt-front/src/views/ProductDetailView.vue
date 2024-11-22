<template>
    <div>
        <h2>은행 정보</h2>
        <ul>
            <li v-for="(bank, index) in bankInfos" :key="index">
                <strong>{{ bank.kor_co_nm }}</strong>
                <p>상품명: {{ bank.fin_prdt_nm }}</p>
                <p>상품 코드: {{ bank.fin_prdt_cd }}</p>
                <p>가입 대상: {{ bank.join_member }}</p>
                <p>우대 조건: {{ bank.spcl_cnd }}</p>
                <p>기타 조건: {{ bank.etc_note }}</p>

                <h3 v-if="bank.depositoptions_set && bank.depositoptions_set.length > 0">예금 옵션</h3>
                <ul v-if="bank.depositoptions_set && bank.depositoptions_set.length > 0">
                    <li v-for="(option, optIndex) in bank.depositoptions_set" :key="optIndex">
                        <p>저축 기간: {{ option.save_trm }}개월</p>
                        <p>기본 금리: {{ option.intr_rate }}%</p>
                        <p>최고 우대 금리: {{ option.intr_rate2 }}%</p>
                        <p>적립 유형: {{ option.rsrv_type_nm }}</p>
                    </li>
                </ul>

                <h3 v-if="bank.savingoptions_set && bank.savingoptions_set.length > 0">적금 옵션</h3>
                <ul v-if="bank.savingoptions_set && bank.savingoptions_set.length > 0">
                    <li v-for="(option, optIndex) in bank.savingoptions_set" :key="optIndex">
                        <p>저축 기간: {{ option.save_trm }}개월</p>
                        <p>기본 금리: {{ option.intr_rate }}%</p>
                        <p>최고 우대 금리: {{ option.intr_rate2 }}%</p>
                        <p>적립 유형: {{ option.rsrv_type_nm }}</p>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script setup>
// defineProps(['id'])
const props = defineProps(['id'])

import axios from 'axios';
import { useFinStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
const store = useFinStore()
const bankInfos = ref([])
const ulElement = document.querySelector('#ul')

// 정보 불러오기
const getDetail = function(id) {
    Promise.all([
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/recommend_deposit_datail/`,
            params: {
                fincode:id
            }
        }),
        axios({
            method:'get',
            url:`${store.API_URL}/financial_products/recommend_savings_detail/`,
            params: {
                fincode:id
            }
        })
    ])
    .then(([depositResponse, savingsResponse]) => {
        // const result = {}; // 임시 객체

        if (depositResponse.data.length > 0) {
          
            bankInfos.value = depositResponse.data; // 결과를 bankInfo에 저장a
            console.log(bankInfos.value)
        } else if (savingsResponse.data.length > 0) {
        
            bankInfos.value = savingsResponse.data; // 결과를 bankInfo에 저장a
            console.log(bankInfos.value)       
        }
    });
}

onMounted(() => {
    getDetail(props.id);
        }
);

// getDetail(id)

</script>

<style scoped>

</style>