<template>
    <div>
        <h1>포트폴리오 페이지</h1>
        <div class="row">
            <PortfolioForm class="col" />
            <div class="col">
                <Portfolio v-if="store.risk_port != [0, 0, 0, 0, 0]" />
                <div v-else style="min-height: 1em;"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import PortfolioForm from '@/components/PortfolioForm.vue';
import Portfolio from '@/components/Portfolio.vue';
import { onMounted } from 'vue';
import { useFinStore } from '@/stores/counter'

const store = useFinStore

onMounted(() => {
    store.risk_port = [0, 0, 0, 0, 0]
})
</script>

<style lang="scss" scoped>

</style>