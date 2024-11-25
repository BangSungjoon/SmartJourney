<template>
    <div>
        <h2>은행 정보</h2>
        <ul>
            <li v-for="(bank, index) in bankInfos" :key="index">
                <div class="bank-header">
                    <strong>{{ bank.kor_co_nm }}</strong>
                    <button 
                        @click="toggleFavorite(bank)" 
                        :class="['favorite-btn', { 'is-favorite': isFavorite(bank) }]"
                    >
                        {{ isFavorite(bank) ? '찜 취소' : '찜하기' }}
                    </button>
                </div>
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

// 찜하기 상태 확인
const isFavorite = (bank) => {
    return bank.depositoptions_set ? 
        store.isDepositFavorite(bank.fin_prdt_cd) : 
        store.isSavingFavorite(bank.fin_prdt_cd);
}

// 찜하기 토글
const toggleFavorite = async (bank) => {
    const productType = bank.depositoptions_set ? 'deposit' : 'saving';
    try {
        const response = await axios({
            method: 'post',
            url: `${store.API_URL}/financial_products/${productType}_products/${bank.fin_prdt_cd}/like/`,
            headers: {
                Authorization: `Token ${store.token}`
            }
        });
        
        // DB 요청이 성공하면 store 상태 업데이트
        if (productType === 'deposit') {
            store.toggleDepositFavorite(bank.fin_prdt_cd);
        } else {
            store.toggleSavingFavorite(bank.fin_prdt_cd);
        }
        
        console.log('찜하기 성공:', response.data);
    } catch (error) {
        console.error('찜하기 실패:', error);
    }
}

</script>

<style scoped>
.bank-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.favorite-btn {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    background-color: #f0f0f0;
}

.favorite-btn.is-favorite {
    background-color: #4CAF50;
    color: white;
}
</style>