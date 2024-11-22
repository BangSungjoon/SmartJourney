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
import axios from 'axios'
import MyCart from '@/components/MyCart.vue'

const route = useRoute()
const depositProducts = ref([])
const savingProducts = ref([])

onMounted(() => {
    const userId = route.params.id;

    console.log(route.params.id)
    axios.get(`http://127.0.0.1:8000/accounts/user/${userId}/`) // 여기서 userId로 상품을 가져옴
        .then((res) => {
            depositProducts.value = res.data.deposit_products;
            savingProducts.value = res.data.saving_products;
        })
        .catch((err) => console.log(err))
})
</script>
