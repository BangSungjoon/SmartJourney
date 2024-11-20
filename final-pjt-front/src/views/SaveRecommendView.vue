<template>
    <div>
        <h1>예적금 추천 받기</h1>
        <form :action="`${store.API_URL}/financial_products/save_deposit/`"></form>
        <button @click.prevent="createRecommend">추천 받기</button>
    </div>
</template>

<script setup>
import axios from 'axios';
import { useFinStore } from '@/stores/counter';

const store = useFinStore()
const createRecommend = function () {
    axios({
        method:'get',
        url:`${store.API_URL}/financial_products/get_deposit/`,
    })
}
    





</script>

<style scoped>

</style>