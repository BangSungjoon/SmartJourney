<template>
    <div>
        <h1>환율 계산기</h1>
        <Exchange />
    </div>
</template>

<script setup>
import Exchange from '@/components/Exchange.vue';
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useFinStore } from '@/stores/counter'

const store = useFinStore()

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/financial_products/save_change_money/`
    })
        .then((res) => {
            console.log(res.data)
        })
        .catch(err => console.log(err))
})
</script>

<style lang="scss" scoped>

</style>