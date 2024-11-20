<template>
    <div>
        <h1>포트폴리오 리스트 페이지</h1>
        <div class="row">
            <ul class="list-group col" v-if="portfolios">
                <li 
                    class="list-group-item" 
                    v-for="portfolio in portfolios" 
                    :key="portfolio.answer"
                    @click="clickDetail(portfolio)"
                >
                    {{ new Date(portfolio.created_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }}
                </li>
            </ul>
            <!-- <PortfolioChart /> -->
             <div class="col">
                <PortfolioChart 
                    v-if="selectedPortfolio" 
                    :portfolio="selectedPortfolio" 
                    :key="selectedPortfolio.answer"
                />
             </div>
        </div>
    </div>
</template>

<script setup>
import PortfolioChart from '@/components/PortfolioChart.vue';
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'
import { useFinStore } from '@/stores/counter'

const store = useFinStore()
const route = useRoute()
const token = store.token // 실제 사용자 토큰 값으로 대체
const headers = {
    'Authorization': `Token ${token}`,
};
const portfolios = ref([])
const selectedPortfolio = ref(null) // 선택된 포트폴리오를 저장할 변수

onMounted(() => {
    console.log(`params id는 ${route.params.id}`)
	axios({
		method: 'get',
		url: `${store.API_URL}/financial_products/my_portfolios/${route.params.id}/`,
        headers: headers
	})
		.then((res) => {
			console.log(res.data)
            portfolios.value = res.data
            console.log(portfolios.value)
		})
		.catch(err => console.log(err))
})

const clickDetail = function (portfolio) {
    console.log(portfolio)
    selectedPortfolio.value = portfolio
}
</script>

<style lang="scss" scoped>

</style>