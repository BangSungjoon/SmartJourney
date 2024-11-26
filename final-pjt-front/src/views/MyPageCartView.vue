<template>
    <div class="cart-container">
        <h2 class="page-title">내가 찜한 금융 상품</h2>
        
        <!-- 상품 유형 선택 버튼 -->
        <div class="product-type-selector">
            <button 
                :class="['type-btn', { active: selectedType === 'deposit' }]"
                @click="selectedType = 'deposit'"
            >
                예금 상품
            </button>
            <button 
                :class="['type-btn', { active: selectedType === 'saving' }]"
                @click="selectedType = 'saving'"
            >
                적금 상품
            </button>
        </div>

        <!-- 선택된 유형에 따른 상품 목록 -->
        <div class="products-grid" v-if="selectedProducts.length">
            <div v-for="product in selectedProducts" :key="product.fin_prdt_cd" class="product-card">
                <h3>{{ product.fin_prdt_nm }}</h3>
                <p class="bank-name">{{ product.kor_co_nm }}</p>
                <p class="interest">최고 금리: {{ product.intr_rate2 }}%</p>
                <div class="card-buttons">
                    <button class="detail-btn" @click="openModal(product)">상세보기</button>
                    <button class="unfavorite-btn" @click="removeFavorite(product)">
                        <i class="fas fa-heart"></i>
                    </button>
                </div>
            </div>
        </div>
        <div v-else class="no-products">
            찜한 {{ selectedType === 'deposit' ? '예금' : '적금' }} 상품이 없습니다.
        </div>

        <!-- 상세 정보 모달 -->
        <div v-if="showModal" class="modal-overlay" @click="closeModal">
            <div class="modal-content" @click.stop>
                <button class="modal-close" @click="closeModal">&times;</button>
                <h2>{{ selectedProduct?.fin_prdt_nm }}</h2>
                <div class="modal-body">
                    <p><strong>은행명:</strong> {{ selectedProduct?.kor_co_nm }}</p>
                    <p><strong>최고 금리:</strong> {{ selectedProduct?.intr_rate2 }}%</p>
                    <p><strong>최저 금리:</strong> {{ selectedProduct?.intr_rate }}%</p>
                    <p><strong>가입 방법:</strong> {{ selectedProduct?.join_way }}</p>
                    <p><strong>가입 대상:</strong> {{ selectedProduct?.join_member }}</p>
                    
                    <!-- 상세 옵션 정보 추가 -->
                    <div v-if="selectedProduct?.options?.length" class="options-table">
                        <h3>금리 정보</h3>
                        <table>
                            <thead>
                                <tr>
                                    <th>저축 금액</th>
                                    <th>저축 기간</th>
                                    <th>금리</th>
                                    <th>비고</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="option in selectedProduct.options" :key="option.id">
                                    <td>{{ option.save_trm }}개월</td>
                                    <td>{{ option.intr_rate }}%</td>
                                    <td>{{ option.intr_rate2 }}%</td>
                                    <td>{{ option.etc_note }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <p class="product-info">{{ selectedProduct?.etc_note }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useFinStore } from '@/stores/counter'
import axios from 'axios'

const store = useFinStore()
const selectedType = ref('deposit')
const showModal = ref(false)
const selectedProduct = ref(null)
const depositProducts = ref([])
const savingProducts = ref([])

// 선택된 유형에 따른 상품 목록
const selectedProducts = computed(() => {
    return selectedType.value === 'deposit' ? depositProducts.value : savingProducts.value
})

// 상품 데이터 가져오기
const fetchProducts = async () => {
    try {
        const response = await axios({
            method: 'get',
            url: `${store.API_URL}/accounts/user/products/`,
            headers: {
                Authorization: `Token ${store.token}`
            }
        })

        // 예금 상품 상세 정보 가져오기
        depositProducts.value = await Promise.all(
            response.data.deposit_products.map(async (product) => {
                try {
                    const detailResponse = await axios({
                        method: 'get',
                        url: `${store.API_URL}/financial_products/recommend_deposit_detail/`,
                        params: {
                            fincode: product.fin_prdt_cd
                        }
                    });
                    if (detailResponse.data.length > 0) {
                        const detailProduct = detailResponse.data[0];
                        return {
                            ...detailProduct,
                            intr_rate2: Math.max(...(detailProduct.depositoptions_set?.map(opt => parseFloat(opt.intr_rate2)) || [0]))
                        };
                    }
                } catch (err) {
                    console.log(err);
                }
                return product;
            })
        );

        // 적금 상품 상세 정보 가져오기
        savingProducts.value = await Promise.all(
            response.data.saving_products.map(async (product) => {
                try {
                    const detailResponse = await axios({
                        method: 'get',
                        url: `${store.API_URL}/financial_products/recommend_savings_detail/`,
                        params: {
                            fincode: product.fin_prdt_cd
                        }
                    });
                    if (detailResponse.data.length > 0) {
                        const detailProduct = detailResponse.data[0];
                        return {
                            ...detailProduct,
                            intr_rate2: Math.max(...(detailProduct.savingoptions_set?.map(opt => parseFloat(opt.intr_rate2)) || [0]))
                        };
                    }
                } catch (err) {
                    console.log(err);
                }
                return product;
            })
        );
    } catch (err) {
        console.log(err)
    }
}

// 상세 정보 가져오기
const fetchProductDetail = async (product) => {
    try {
        // 상품 타입 확인 (예금/적금)
        const productType = selectedType.value === 'deposit' ? 'deposit' : 'savings';
        const response = await axios({
            method: 'get',
            url: `${store.API_URL}/financial_products/recommend_${productType}_detail/`,
            params: {
                fincode: product.fin_prdt_cd
            }
        });

        if (response.data.length > 0) {
            const detailProduct = response.data[0];
            // 옵션 정보 설정
            const options = productType === 'deposit' ? 
                detailProduct.depositoptions_set : 
                detailProduct.savingoptions_set;

            selectedProduct.value = {
                ...detailProduct,
                options: options,
                intr_rate2: Math.max(...(options?.map(opt => parseFloat(opt.intr_rate2)) || [0]))
            };
            showModal.value = true;
        }
    } catch (err) {
        console.log(err);
    }
};

// 찜 해제
const removeFavorite = async (product) => {
    try {
        const productType = selectedType.value === 'deposit' ? 'deposit' : 'saving';
        await axios({
            method: 'post',
            url: `${store.API_URL}/financial_products/${productType}_products/${product.fin_prdt_cd}/like/`,
            headers: {
                Authorization: `Token ${store.token}`
            }
        })
        // 찜 해제 후 목록에서 제거
        if (selectedType.value === 'deposit') {
            depositProducts.value = depositProducts.value.filter(p => p.fin_prdt_cd !== product.fin_prdt_cd)
        } else {
            savingProducts.value = savingProducts.value.filter(p => p.fin_prdt_cd !== product.fin_prdt_cd)
        }
    } catch (err) {
        console.log(err)
    }
}

// 모달 관련 함수
const openModal = (product) => {
    fetchProductDetail(product);
}

const closeModal = () => {
    showModal.value = false
    selectedProduct.value = null
}

// 초기 데이터 로드
fetchProducts()
</script>

<style scoped>
.cart-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.page-title {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
}

.product-type-selector {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.type-btn {
    padding: 0.5rem 2rem;
    border: 2px solid #007bff;
    background: transparent;
    color: #007bff;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.type-btn.active {
    background: #007bff;
    color: white;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
}

.product-card {
    background: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    position: relative;
    display: flex;
    flex-direction: column;
    min-height: 200px;
}

.product-card:hover {
    transform: translateY(-5px);
}

.product-card h3 {
    margin: 0 0 1rem;
    color: #333;
}

.bank-name {
    color: #666;
    margin-bottom: 0.5rem;
}

.interest {
    color: #007bff;
    font-weight: bold;
    margin-bottom: 1rem;
}

.card-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
}

.detail-btn {
    padding: 0.5rem 1rem;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.unfavorite-btn {
    background: none;
    border: none;
    color: #ff4444;
    cursor: pointer;
    font-size: 1.2rem;
}

.no-products {
    text-align: center;
    color: #666;
    padding: 2rem;
}

/* 모달 스타일 */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    width: 90%;
    max-width: 600px;
    max-height: 80vh;
    overflow: hidden;
    position: relative;
}

.modal-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
}

.modal-body {
    margin-top: 1rem;
    max-height: calc(80vh - 6rem);
    overflow-y: auto;
    padding-right: 1rem;
    border-radius: 8px;
}

.modal-body p {
    margin-bottom: 0.5rem;
}

.product-info {
    margin-top: 1rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 5px;
}

/* 옵션 테이블 스타일 추가 */
.options-table {
    margin-top: 1.5rem;
    overflow-x: auto;
}

.options-table h3 {
    margin-bottom: 1rem;
    color: #333;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #dee2e6;
}

th {
    background-color: #f8f9fa;
    font-weight: bold;
}

tr:hover {
    background-color: #f8f9fa;
}

/* 스크롤바 스타일링 (선택사항) */
.modal-body::-webkit-scrollbar {
    width: 8px;
}

.modal-body::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb:hover {
    background: #555;
}
</style>
