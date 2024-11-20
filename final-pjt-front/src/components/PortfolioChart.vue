<template>
    <div>
        <!-- 위험도에 따른 포폴 구성 비율 -->
        <canvas id="riskChart"></canvas>
        <!-- 자산 유형(저축 / 투자)에 따른 포폴 구성 비율 -->
        <canvas id="saveInv"></canvas>
        <!-- 자산 유형(투자 상품 내)에 따른 포폴 구성 비율 -->
        <canvas id="InvChart"></canvas>
        <!-- 자산 유형(저축 상품 내)에 따른 포폴 구성 비율 -->
        <canvas id="saveChart"></canvas>
    </div>
</template>

<script setup>
import { onMounted, nextTick } from 'vue';
const props = defineProps({ 'portfolio': Object })
console.log(props.portfolio.answer)

onMounted(() => {
    nextTick(() => { // DOM 업데이트가 완료된 후 차트를 그릴 수 있게 보장하는 메서드
        const ctx = document.getElementById('riskChart');

        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['저위험', '중저위험', '중위험', '중고위험', '고위험'],
                datasets: [{
                    label: '위험도에 따른 투자 비율 구성',
                    data: [props.portfolio.low_ratio, props.portfolio.med_low_ratio, props.portfolio.med_ratio, props.portfolio.med_high_ratio, props.portfolio.high],
                    backgroundColor: [
                        '#4CAF50', // 저위험 (밝고 차분한 초록)
                        '#FFD700', // 중저위험 (노란색)
                        '#FF6347', // 중위험 (토마토 색, 약간 강렬한 빨강)
                        '#FF4500', // 중고위험 (주황색)
                        '#FF0000'  // 고위험 (강렬한 빨강)
                    ],
                    hoverOffset: 4
                }]
            },
        });

        const ctx1 = document.getElementById('saveInv');

        new Chart(ctx1, {
            type: 'doughnut',
            data: {
                labels: ['저축', '투자'],
                datasets: [{
                    label: '투자 저축 비율',
                    data: [props.portfolio.saving_ratio*100, props.portfolio.inv_ratio*100],
                    backgroundColor: [
                        '#4CAF50', // (밝고 차분한 초록)
                        '#FF0000'  // (강렬한 빨강)
                    ],
                    hoverOffset: 4
                }]
            },
        });

        const ctx2 = document.getElementById('InvChart');
        new Chart(ctx2, {
            type: 'doughnut',
            data: {
                labels: ['국내 주식형', '해외 주식형', '채권형', '대안투자'],
                datasets: [{
                    label: '자산 유형(투자 상품 내)에 따른 포트폴리오',
                    data: [props.portfolio.dom_stock_ratio*100, props.portfolio.int_stock_ratio*100, props.portfolio.bond_ratio*100, props.portfolio.alt_invest_ratio*100],
                    backgroundColor: [
                        '#4CAF50', // 저위험 (밝고 차분한 초록)
                        '#FFD700', // 중저위험 (노란색)
                        '#FF4500', // 중고위험 (주황색)
                        '#FF0000'  // 고위험 (강렬한 빨강)
                    ],
                    hoverOffset: 4
                }]
            },
        });

        const ctx3 = document.getElementById('saveChart');
        new Chart(ctx3, {
            type: 'doughnut',
            data: {
                labels: ['적금/정기예금', '보통예금'],
                datasets: [{
                    label: '자산 유형(저축 상품 내)에 따른 포트폴리오',
                    data: [props.portfolio.inst_save_ratio*100, props.portfolio.reg_save_ratio*100],
                    backgroundColor: [
                        '#4CAF50', // 저위험 (밝고 차분한 초록)
                        '#FF0000'  // 고위험 (강렬한 빨강)
                    ],
                    hoverOffset: 4
                }]
            },
        });
    })
})

</script>

<style scoped>

</style>