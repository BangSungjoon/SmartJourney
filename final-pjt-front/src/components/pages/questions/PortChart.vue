<template>
    <div class="chart-container">
        <div v-if="selectedType === '위험도'" class="single-chart">
            <canvas id="riskChart"></canvas>
        </div>
        <div v-else-if="selectedType === '자산유형'" class="triangle-layout">
            <canvas id="saveInv"></canvas>
            <canvas id="InvChart"></canvas>
            <canvas id="saveChart"></canvas>
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
                            '#4CAF50',
                            '#FFD700',
                            '#FF6347',
                            '#FF4500',
                            '#FF0000'
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
                            backgroundColor: ['#4CAF50', '#FF0000'],
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
                            backgroundColor: ['#4CAF50', '#FFD700', '#FF4500', '#FF0000'],
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
                            backgroundColor: ['#4CAF50', '#FF0000'],
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
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    background: linear-gradient(180deg, #111827 0%, #1f2937 100%);
}

.single-chart {
    width: 800px;
    height: 800px;
    position: relative;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.triangle-layout {
    position: relative;
    width: 600px;
    height: 600px;
    display: grid;
    grid-template-areas:
        ". top ."
        "left . right";
    gap: 20px;
    padding: 2rem;
    transform: translateX(-300px);
}

.triangle-layout canvas {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    backdrop-filter: blur(10px);
    padding: 1rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
</style>