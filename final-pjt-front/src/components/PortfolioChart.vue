<template>
    <div>
        <canvas id="myChart"></canvas>
    </div>
</template>

<script setup>
import { onMounted, nextTick } from 'vue';

onMounted(() => {
    nextTick(() => { // DOM 업데이트가 완료된 후 차트를 그릴 수 있게 보장하는 메서드
        const ctx = document.getElementById('myChart');

        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['저위험', '중저위험', '중위험', '중고위험', '고위험'],
                datasets: [{
                    label: '포트폴리오',
                    data: [12, 19, 3, 5, 2],
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
    })
})

</script>

<style scoped>

</style>