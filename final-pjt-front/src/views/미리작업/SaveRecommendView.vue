<template>
    <div>
        <h1>예적금 추천 받기</h1>
        <!-- <form :action="`${store.API_URL}/financial_products/save_deposit/`"></form>
        <button @click.prevent="createRecommend">예금 적금 db 저장</button> -->
        <form :action="`${store.API_URL}/financial_products/save_deposit/`"></form>
        <button @click.prevent="dePositRecommend">정기 예금 추천 받기</button>
        <!-- <form :action="`${store.API_URL}/financial_products/save_deposit/`"></form>
        <button @click.prevent="createRecommend">적금 추천 받기</button> -->
        <Recommend/>
    </div>
</template>

<script setup>
import axios from 'axios';
import { useFinStore } from '@/stores/counter';
import Recommend from '@/components/Recommend.vue';

const store = useFinStore()
const createRecommend = function () {
    axios({
        method:'get',
        url:`${store.API_URL}/financial_products/save_deposit_savings/`,
    })
}
</script>

<style scoped>

</style>