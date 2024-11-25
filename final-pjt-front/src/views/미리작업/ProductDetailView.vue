<template>
    <div class="product-detail">
        <div v-for="(bank, index) in bankInfos" :key="index" class="bank-info">
            <!-- 헤더 섹션 -->
            <div class="bank-header">
                <h2 class="bank-name">{{ bank.kor_co_nm }}</h2>
                <button 
                    @click="toggleFavorite(bank)" 
                    :class="['favorite-btn', { 'is-favorite': isFavorite(bank) }]"
                >
                    <span class="heart-icon">{{ isFavorite(bank) ? '♥' : '♡' }}</span>
                    {{ isFavorite(bank) ? '찜 취소' : '찜하기' }}
                </button>
            </div>

            <!-- 기본 정보 섹션 -->
            <div class="basic-info">
                <h3 class="product-name">{{ bank.fin_prdt_nm }}</h3>
                <div class="info-grid">
                    <div class="info-item">
                        <span class="label">상품 코드</span>
                        <span class="value">{{ bank.fin_prdt_cd }}</span>
                    </div>
                    <div class="info-item">
                        <span class="label">가입 대상</span>
                        <span class="value">{{ bank.join_member }}</span>
                    </div>
                </div>
            </div>

            <!-- 우대 조건 섹션 -->
            <div class="conditions-section">
                <div class="condition-box">
                    <h4>우대 조건</h4>
                    <p>{{ bank.spcl_cnd || '해당사항 없음' }}</p>
                </div>
                <div class="condition-box">
                    <h4>기타 조건</h4>
                    <p>{{ bank.etc_note || '해당사항 없음' }}</p>
                </div>
            </div>

            <!-- 예금 옵션 섹션 -->
            <div v-if="bank.depositoptions_set?.length" class="options-section">
                <h3 class="options-title">예금 옵션</h3>
                <div class="options-grid">
                    <div v-for="(option, optIndex) in bank.depositoptions_set" 
                         :key="optIndex"
                         class="option-card">
                        <div class="option-header">저축 기간: {{ option.save_trm }}개월</div>
                        <div class="rates">
                            <div class="rate-item">
                                <span class="rate-label">기본 금리</span>
                                <span class="rate-value">{{ option.intr_rate }}%</span>
                            </div>
                            <div class="rate-item highlight">
                                <span class="rate-label">최고 우대 금리</span>
                                <span class="rate-value">{{ option.intr_rate2 }}%</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 적금 옵션 섹션 -->
            <div v-if="bank.savingoptions_set?.length" class="options-section">
                <h3 class="options-title">적금 옵션</h3>
                <div class="options-grid">
                    <div v-for="(option, optIndex) in bank.savingoptions_set" 
                         :key="optIndex"
                         class="option-card">
                        <div class="option-header">
                            {{ option.rsrv_type_nm }} - {{ option.save_trm }}개월
                        </div>
                        <div class="rates">
                            <div class="rate-item">
                                <span class="rate-label">기본 금리</span>
                                <span class="rate-value">{{ option.intr_rate }}%</span>
                            </div>
                            <div class="rate-item highlight">
                                <span class="rate-label">최고 우대 금리</span>
                                <span class="rate-value">{{ option.intr_rate2 }}%</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { useFinStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
// defineProps(['id'])
const props = defineProps({
  id: Number,
});
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
.product-detail {
    color: #333;
    font-family: 'Noto Sans KR', sans-serif;
}

.bank-info {
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
}

.bank-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background: #f8f9fa;
    border-bottom: 1px solid #eee;
}

.bank-name {
    font-size: 1.5rem;
    margin: 0;
    color: #2c3e50;
    font-weight: 700;
}

.favorite-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    background: white;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.favorite-btn:hover {
    background: #f8f9fa;
}

.favorite-btn.is-favorite {
    background: #ff6b6b;
    color: white;
    border-color: #ff6b6b;
}

.heart-icon {
    font-size: 1.2em;
    line-height: 1;
}

.basic-info {
    padding: 20px;
    background: white;
}

.product-name {
    font-size: 1.3rem;
    color: #1a73e8;
    margin: 0 0 20px 0;
    font-weight: 500;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
}

.info-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.label {
    font-size: 0.9rem;
    color: #666;
    font-weight: 400;
}

.value {
    font-size: 1rem;
    font-weight: 500;
}

.conditions-section {
    padding: 20px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.condition-box {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 8px;
}

.condition-box h4 {
    margin: 0 0 10px 0;
    color: #2c3e50;
    font-weight: 500;
}

.condition-box p {
    margin: 0;
    line-height: 1.6;
    color: #666;
}

.options-section {
    padding: 20px;
}

.options-title {
    margin: 0 0 20px 0;
    color: #2c3e50;
    font-size: 1.2rem;
    font-weight: 500;
}

.options-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.option-card {
    background: #f8f9fa;
    border-radius: 8px;
    overflow: hidden;
}

.option-header {
    background: #e9ecef;
    padding: 12px;
    font-weight: 500;
    color: #495057;
}

.rates {
    padding: 16px;
}

.rate-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
}

.rate-item.highlight {
    color: #1a73e8;
    font-weight: 500;
}

.rate-label {
    font-size: 0.9rem;
}

.rate-value {
    font-size: 1.1rem;
    font-weight: 600;
}

/* 반응형 디자인을 위한 미디어 쿼리 */
@media (max-width: 768px) {
    .info-grid, .conditions-section {
        grid-template-columns: 1fr;
    }
    
    .options-grid {
        grid-template-columns: 1fr;
    }
}
</style>