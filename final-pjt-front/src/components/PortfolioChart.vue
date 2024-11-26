<template>
    <div class="chart-container">
        <!-- 위험도 차트 -->
        <div v-if="selectedType === '위험도'" class="chart-wrapper">
            <h3>위험도에 따른 포트폴리오</h3>
            <div class="chart">
                <canvas id="riskChart"></canvas>
            </div>
        </div>

        <!-- 자산유형 차트들 (캐러셀) -->
        <div v-else class="chart-carousel">
            <button class="carousel-btn prev" @click="prevChart" v-show="currentIndex > 0">&lt;</button>
            
            <div class="chart-wrapper">
                <div class="carousel-track" :style="{ transform: `translateX(-${currentIndex * 400}px)` }">
                    <!-- 투자/저축 비율 차트 -->
                    <div class="chart-item">
                        <h3>투자/저축 비율</h3>
                        <div class="chart">
                            <canvas id="saveInv"></canvas>
                        </div>
                    </div>
                    <!-- 투자 상품 구성 차트 -->
                    <div class="chart-item">
                        <h3>투자 상품 구성</h3>
                        <div class="chart">
                            <canvas id="InvChart"></canvas>
                        </div>
                    </div>
                    <!-- 저축 상품 구성 차트 -->
                    <div class="chart-item">
                        <h3>저축 상품 구성</h3>
                        <div class="chart">
                            <canvas id="saveChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <button class="carousel-btn next" @click="nextChart" v-show="currentIndex < 2">&gt;</button>

            <!-- 캐러셀 인디케이터 -->
            <!-- <div class="carousel-indicators">
                <span 
                    v-for="n in 3" 
                    :key="n"
                    :class="['indicator', { active: currentIndex === n - 1 }]"
                    @click="currentIndex = n - 1"
                ></span>
            </div> -->
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch, onUnmounted } from 'vue';

const props = defineProps({
    portfolio: {
        type: Object,
        required: true
    },
    selectedType: {
        type: String,
        required: true,
        default: '위험도'
    },
    chartIndex: {
        type: Number,
        default: 0
    }
});

let charts = [];
const currentIndex = ref(0);

const nextChart = () => {
    if (currentIndex.value < 2) {
        currentIndex.value++;
        createCharts();
    }
};

const prevChart = () => {
    if (currentIndex.value > 0) {
        currentIndex.value--;
        createCharts();
    }
};

const destroyCharts = () => {
    charts.forEach(chart => {
        if (chart) chart.destroy();
    });
    charts = [];
};

const createCharts = () => {
    destroyCharts();
    nextTick(() => {
        if (props.selectedType === '위험도') {
            const ctx = document.getElementById('riskChart')?.getContext('2d');
            if (ctx) {
                charts.push(new window.Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['저위험', '중저위험', '중위험', '중고위험', '고위험'],
                        datasets: [{
                            data: [
                                props.portfolio.low_ratio, 
                                props.portfolio.med_low_ratio, 
                                props.portfolio.med_ratio, 
                                props.portfolio.med_high_ratio, 
                                props.portfolio.high
                            ],
                            backgroundColor: [
                                '#4CAF50', '#FFD700', '#FF6347', '#FF4500', '#FF0000'
                            ],
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                    }
                }));
            }
        } else {
            const chartIds = ['saveInv', 'InvChart', 'saveChart'];
            chartIds.forEach((id, index) => {
                const ctx = document.getElementById(id)?.getContext('2d');
                if (ctx) {
                    const chartData = {
                        0: {
                            data: [props.portfolio.saving_ratio*100, props.portfolio.inv_ratio*100],
                            labels: ['저축', '투자'],
                            colors: ['#4CAF50', '#FF0000']
                        },
                        1: {
                            data: [
                                props.portfolio.dom_stock_ratio*100,
                                props.portfolio.int_stock_ratio*100,
                                props.portfolio.bond_ratio*100,
                                props.portfolio.alt_invest_ratio*100
                            ],
                            labels: ['국내 주식형', '해외 주식형', '채권형', '대안투자'],
                            colors: ['#4CAF50', '#FFD700', '#FF4500', '#FF0000']
                        },
                        2: {
                            data: [props.portfolio.inst_save_ratio*100, props.portfolio.reg_save_ratio*100],
                            labels: ['적금/정기예금', '보통예금'],
                            colors: ['#4CAF50', '#FF0000']
                        }
                    }[index];

                    charts.push(new window.Chart(ctx, {
                        type: 'doughnut',
                        data: {
                            labels: chartData.labels,
                            datasets: [{
                                data: chartData.data,
                                backgroundColor: chartData.colors,
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                        }
                    }));
                }
            });
        }
    });
};

watch(() => [props.selectedType, currentIndex.value], createCharts);
onMounted(createCharts);
onUnmounted(destroyCharts);
</script>

<style scoped>
.chart-container {
    width: 100%;
    min-height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    margin: 20px 0;
    position: relative;
}

.chart-wrapper {
    width: 400px;
    height: 400px;
    position: relative;
    overflow: hidden;
}

.chart-carousel {
    position: relative;
    width: 400px;
    height: 450px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.carousel-track {
    display: flex;
    transition: transform 0.3s ease;
    width: 1200px;
    height: 400px;
}

.chart-item {
    width: 400px;
    height: 400px;
    flex-shrink: 0;
    padding: 20px;
}

.chart {
    width: 100%;
    height: 300px;
    position: relative;
    margin-bottom: 20px;
}

.carousel-btn {
    position: absolute;
    top: 45%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.3);
    color: white;
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 2;
    font-size: 1.2rem;
}

.carousel-btn:hover {
    background: rgba(0, 0, 0, 0.5);
}

.carousel-btn.prev {
    left: -50px;
}

.carousel-btn.next {
    right: -50px;
}

.carousel-indicators {
    display: flex;
    gap: 10px;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px;
    z-index: 3;
}

/* .indicator {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.indicator.active {
    background: rgba(0, 0, 0, 0.6);
}

.indicator:hover {
    background: rgba(0, 0, 0, 0.4);
} */

h3 {
    text-align: center;
    margin: 0 0 20px 0;
    color: #333;
    font-size: 1.2rem;
    height: 20px;
}

canvas {
    max-width: 100% !important;
    max-height: 100% !important;
}
</style>