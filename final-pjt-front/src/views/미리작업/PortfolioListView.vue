<template>
    <div class="portfolio-list-container">
        <h2 class="page-title">나의 포트폴리오 기록</h2>
        <div class="portfolio-content">
            <!-- 왼쪽 리스트 섹션 -->
            <div class="portfolio-list" v-if="portfolios">
                <div 
                    class="portfolio-item" 
                    v-for="portfolio in portfolios" 
                    :key="portfolio.answer"
                    :class="{ 'selected': selectedPortfolio?.answer === portfolio.answer }"
                    @click="clickDetail(portfolio)"
                >
                    <div class="portfolio-info">
                        <div class="date">
                            {{ new Date(portfolio.created_at).toLocaleString('ko-KR', 
                                { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }}
                        </div>
                        <button 
                            class="delete-btn" 
                            @click.stop="deletePortfolio(portfolio)"
                            v-if="portfolio.user_id == currentUserId"
                        >
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
                <div v-if="portfolios.length === 0" class="no-portfolios">
                    아직 생성된 포트폴리오가 없습니다.
                </div>
            </div>

            <!-- 오른쪽 차트 섹션 -->
            <div class="portfolio-detail">
                <div v-if="selectedPortfolio" class="chart-section">
                    <!-- 차트 타입 선택 버튼 -->
                    <div class="chart-type-selector">
                        <button 
                            :class="['type-btn', { active: selectedChartType === 'risk' }]"
                            @click="selectedChartType = 'risk'"
                        >
                            위험도 분석
                        </button>
                        <button 
                            :class="['type-btn', { active: selectedChartType === 'asset' }]"
                            @click="selectedChartType = 'asset'"
                        >
                            자산 유형 분석
                        </button>
                    </div>
                    
                    <div class="chart-container">
                        <PortfolioChart 
                            :portfolio="selectedPortfolio"
                            :key="`${selectedPortfolio.answer}-${selectedChartType}`"
                            :selectedType="selectedChartType === 'risk' ? '위험도' : '자산유형'"
                        />
                    </div>
                </div>
                <div v-else class="no-selection">
                    <i class="fas fa-chart-pie"></i>
                    <p>포트폴리오를 선택하면 상세 정보를 확인할 수 있습니다.</p>
                </div>
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

const selectedChartType = ref('risk') // 차트 타입 선택을 위한 ref 추가

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

<style scoped>
.portfolio-list-container {
    padding: 2rem;
    height: 100%;
}

.page-title {
    font-size: 2rem;
    color: #333;
    margin-bottom: 2rem;
    text-align: center;
}

.portfolio-content {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 2rem;
    height: calc(100% - 100px);
}

/* 왼쪽 리스트 스타일 */
.portfolio-list {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 1.5rem;
    overflow-y: auto;
    max-height: 600px;
}

.portfolio-item {
    background: rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    margin-bottom: 1rem;
    padding: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 1px solid rgba(0, 0, 0, 0.1);
}

.portfolio-item:hover {
    background: rgba(0, 0, 0, 0.2);
    transform: translateY(-2px);
}

.portfolio-item.selected {
    background: rgba(79, 70, 229, 0.2);
    border: 1px solid rgba(79, 70, 229, 0.5);
}

.portfolio-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.date {
    color: #333;
    font-size: 0.9rem;
    font-weight: 500;
}

.delete-btn {
    background: none;
    border: none;
    color: #ff4757;
    cursor: pointer;
    padding: 5px;
    opacity: 0.7;
    transition: opacity 0.3s ease;
}

.delete-btn:hover {
    opacity: 1;
}

/* 오른쪽 차트 섹션 스타일 */
.portfolio-detail {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
}

.chart-section {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.chart-type-selector {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}

.type-btn {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    background: rgba(0, 0, 0, 0.1);
    color: #333;
    cursor: pointer;
    transition: all 0.3s ease;
}

.type-btn:hover {
    background: rgba(79, 70, 229, 0.1);
}

.type-btn.active {
    background: rgba(79, 70, 229, 0.2);
    color: #333;
    font-weight: bold;
}

.chart-container {
    width: 80%;
    height: 80%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.no-selection {
    text-align: center;
    color: #333;
}

.no-selection i {
    font-size: 4rem;
    margin-bottom: 1rem;
    color: #666;
}

.no-selection p {
    font-size: 1.1rem;
}

.no-portfolios {
    text-align: center;
    color: #333;
    padding: 2rem;
}

/* 스크롤바 스타일링 */
.portfolio-list::-webkit-scrollbar {
    width: 8px;
}

.portfolio-list::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.1);
}

.portfolio-list::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.2);
}

.portfolio-list::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 0, 0, 0.3);
}
</style>
