<template>
    <div>
        <h2>내가 찜한 예금 상품</h2>
        <MyCart :products="depositProducts" title="예금 상품" />
        <h2>내가 찜한 적금 상품</h2>
        <MyCart :products="savingProducts" title="적금 상품" />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useFinStore } from '@/stores/counter'
import axios from 'axios'
import MyCart from '@/components/MyCart.vue'

const route = useRoute()
const store = useFinStore()
const depositProducts = ref([])
const savingProducts = ref([])

onMounted(() => {
    // const userId = route.params.id;
    
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/user/products/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        depositProducts.value = res.data.deposit_products;
        savingProducts.value = res.data.saving_products;
        
        // store의 favorites 상태도 업데이트
        store.depositFavorites = res.data.deposit_products.map(p => p.fin_prdt_cd);
        store.savingFavorites = res.data.saving_products.map(p => p.fin_prdt_cd);
    })
    .catch((err) => console.log(err))
})
</script>
