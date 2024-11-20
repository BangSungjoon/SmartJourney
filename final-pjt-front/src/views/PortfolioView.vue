<template>
    <div>
        <h1>포트폴리오 페이지</h1>
        <p>포트폴리오 소개가 들어갈 예정</p>
        <RouterLink :to="{ name:'portlist' }">포트폴리오 리스트 보러가기</RouterLink>
        <PortfolioForm />
    </div>
</template>

<script setup>
import PortfolioForm from '@/components/PortfolioForm.vue';
import { RouterLink, RouterView } from 'vue-router'

</script>

<style lang="scss" scoped>

</style>