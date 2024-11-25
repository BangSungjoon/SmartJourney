<template>
    <div>
        <h2>포트폴리오 리스트 페이지</h2>
        <div class="row">
            <ul class="list-group col" v-if="portfolios">
                <li 
                    class="list-group-item" 
                    v-for="portfolio in portfolios" 
                    :key="portfolio.answer"
                >
                    <span @click="clickDetail(portfolio)">
                        {{ new Date(portfolio.created_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }}
                    </span>
                    <button 
                        class="btn btn-danger btn-sm" 
                        @click="deletePortfolio(portfolio)"
                        v-if="portfolio.user_id == currentUserId"
                    >
                        삭제
                    </button>
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
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useFinStore } from '@/stores/counter'

const store = useFinStore()
const route = useRoute()
const portfolios = ref([])
const selectedPortfolio = ref(null) // 선택된 포트폴리오를 저장할 변수
const currentUserId = computed(() => store.currentUserId)  // 로그인한 사용자의 id

const token = store.token           // 실제 사용자 토큰 값으로 대체
const headers = {
    'Authorization': `Token ${token}`,
};

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

// 클릭하면 포트폴리오가 보이게 값을 넣어준다.
const clickDetail = function (portfolio) {
    console.log(portfolio)
    selectedPortfolio.value = portfolio
}

const deletePortfolio = (portfolio) => {
    console.log(portfolio.answer)
    if (!confirm('이 포트폴리오를 정말 삭제하시겠어요?')) return;
    axios({
        method: 'delete',
        url: `${store.API_URL}/financial_products/portfolio/${portfolio.answer}/`,
        headers,
    })
        .then(() => {
            portfolios.value = portfolios.value.filter(
                (item) => item.answer !== portfolio.answer
            );
            alert('포트폴리오가 삭제되었습니다.');
        })
        .catch((err) => {
            console.error(err);
            alert('포트폴리오 삭제에 실패했습니다.');
        });
}
</script>
