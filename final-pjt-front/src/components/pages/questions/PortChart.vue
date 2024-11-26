<template>
    <div class="chart-container">
        <div class="chart-wrapper">
            <div v-if="selectedType === '위험도'" class="asset-chart">
                <h3>위험도에 따른 포트폴리오</h3>
                <canvas id="riskChart"></canvas>
            </div>
            <div v-else-if="selectedType === '자산유형' && chartIndex === 0" class="asset-chart">
                <h3>투자/저축 비율</h3>
                <canvas id="saveInv"></canvas>
            </div>
            <div v-else-if="selectedType === '자산유형' && chartIndex === 1" class="asset-chart">
                <h3>투자 상품 구성</h3>
                <canvas id="InvChart"></canvas>
            </div>
            <div v-else-if="selectedType === '자산유형' && chartIndex === 2" class="asset-chart">
                <h3>저축 상품 구성</h3>
                <canvas id="saveChart"></canvas>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, nextTick, watch } from 'vue';

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

const createCharts = () => {
    nextTick(() => {
        if (props.selectedType === '위험도') {
            const ctx = document.getElementById('riskChart');
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['저위험', '중저위험', '중위험', '중고위험', '고위험'],
                    datasets: [{
                        label: '위험도에 따른 투자 비율 구성',
                        data: [
                            props.portfolio.low_ratio, 
                            props.portfolio.med_low_ratio, 
                            props.portfolio.med_ratio, 
                            props.portfolio.med_high_ratio, 
                            props.portfolio.high_ratio
                        ],
                        backgroundColor: [
                            '#C2C0A6',
                            '#A8B545',
                            '#6A8C69',
                            '#53736A',
                            '#024554',
                        ],
                        hoverOffset: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                padding: 20
                            }
                        },
                        tooltip: {
                            enabled: true,
                            position: 'average',
                            intersect: true,
                            mode: 'index'
                        }
                    },
                    layout: {
                        padding: {
                            top: 20,
                            bottom: 20
                        }
                    }
                }
            });
        } else {
            // 자산유형 차트들 생성
            const createAssetCharts = () => {
                // saveInv 차트
                const ctx1 = document.getElementById('saveInv');
                new Chart(ctx1, {
                    type: 'doughnut',
                    data: {
                        labels: ['저축', '투자'],
                        datasets: [{
                            label: '투자 저축 비율',
                            data: [props.portfolio.saving_ratio*100, props.portfolio.inv_ratio*100],
                            backgroundColor: ['#F3B562', '#8CBEB2'],
                            hoverOffset: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    padding: 20
                                }
                            },
                            tooltip: {
                                enabled: true,
                                position: 'average',
                                intersect: true,
                                mode: 'index'
                            }
                        },
                        layout: {
                            padding: {
                                top: 20,
                                bottom: 20
                            }
                        }
                    }
                });

                // InvChart 차트
                const ctx2 = document.getElementById('InvChart');
                new Chart(ctx2, {
                    type: 'doughnut',
                    data: {
                        labels: ['국내 주식형', '해외 주식형', '채권형', '대안투자'],
                        datasets: [{
                            label: '투자 상품 구성',
                            data: [
                                props.portfolio.dom_stock_ratio*100, 
                                props.portfolio.int_stock_ratio*100, 
                                props.portfolio.bond_ratio*100, 
                                props.portfolio.alt_invest_ratio*100
                            ],
                            backgroundColor: [
                            '#F06060',
                            '#F3B562',
                            '#5C4B51',
                            '#8CBEB2',],
                            hoverOffset: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    padding: 20
                                }
                            },
                            tooltip: {
                                enabled: true,
                                position: 'average',
                                intersect: true,
                                mode: 'index'
                            }
                        },
                        layout: {
                            padding: {
                                top: 20,
                                bottom: 20
                            }
                        }
                    }
                });

                // saveChart 차트
                const ctx3 = document.getElementById('saveChart');
                new Chart(ctx3, {
                    type: 'doughnut',
                    data: {
                        labels: ['적금/정기예금', '보통예금'],
                        datasets: [{
                            label: '저축 상품 구성',
                            data: [
                                props.portfolio.inst_save_ratio*100, 
                                props.portfolio.reg_save_ratio*100
                            ],
                            backgroundColor: ['#5C4B51', '#F06060'],
                            hoverOffset: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    padding: 20
                                }
                            },
                            tooltip: {
                                enabled: true,
                                position: 'average',
                                intersect: true,
                                mode: 'index'
                            }
                        },
                        layout: {
                            padding: {
                                top: 20,
                                bottom: 20
                            }
                        }
                    }
                });
            };
            createAssetCharts();
        }
    });
};

watch(() => props.selectedType, createCharts);

onMounted(createCharts);
</script>

<style scoped>
.chart-container {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
}

.chart-wrapper {
    width: 600px;
    height: 600px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
}

.asset-chart {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.asset-chart h3 {
    color: #000000;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

canvas {
    width: 100% !important;
    height: 100% !important;
    max-width: 500px;
    max-height: 500px;
}
</style>