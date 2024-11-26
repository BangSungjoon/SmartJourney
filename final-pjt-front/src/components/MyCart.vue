<template>
    <div class="cart-container">
        <div v-if="products.length" class="product-grid">
            <div v-for="product in products" :key="product.fin_prdt_cd" class="product-card">
                <h3>{{ product.kor_co_nm }}</h3>
                <p>{{ product.fin_prdt_nm }}</p>
                <div class="product-actions">
                    <RouterLink 
                        :to="{ name: 'productDetail', params: { id: product.fin_prdt_cd }}" 
                        class="detail-btn"
                    >
                        상세보기
                    </RouterLink>
                    <button @click="removeFromCart(product)" class="remove-btn">
                        찜 취소
                    </button>
                </div>
            </div>
        </div>
        <div v-else class="no-items">
            <p>찜한 {{ title }}이 없습니다.</p>
        </div>
    </div>
</template>

<script setup>
import { useFinStore } from '@/stores/counter';
import axios from 'axios';

const store = useFinStore();
const props = defineProps({
    products: {
        type: Array,
        required: true
    },
    title: {
        type: String,
        required: true
    }
});

const removeFromCart = async (product) => {
    const productType = props.title.includes('예금') ? 'deposit' : 'saving';
    try {
        const headers = {
            Authorization: `Token ${store.token}`
        }
        await axios({
            method: 'post',
            url: `${store.API_URL}/financial_products/${productType}_products/${product.fin_prdt_cd}/like/`,
            headers: headers
        });
        
        // store 상태 업데이트
        if (productType === 'deposit') {
            store.toggleDepositFavorite(product.fin_prdt_cd);
            // 화면에서 상품 제거
            const index = props.products.findIndex(p => p.fin_prdt_cd === product.fin_prdt_cd);
            if (index > -1) {
                props.products.splice(index, 1);
            }
        } else {
            store.toggleSavingFavorite(product.fin_prdt_cd);
            // 화면에서 상품 제거
            const index = props.products.findIndex(p => p.fin_prdt_cd === product.fin_prdt_cd);
            if (index > -1) {
                props.products.splice(index, 1);
            }
        }
    } catch (error) {
        console.error('찜 취소 실패:', error);
    }
}
</script>

<style scoped>
.cart-container {
    padding: 20px;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

.product-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 16px;
    background: white;
}

.product-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 16px;
}

.detail-btn, .remove-btn {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.detail-btn {
    background-color: #4CAF50;
    color: white;
    text-decoration: none;
}

.remove-btn {
    background-color: #f44336;
    color: white;
}

.no-items {
    text-align: center;
    padding: 40px;
    color: #666;
}
</style>