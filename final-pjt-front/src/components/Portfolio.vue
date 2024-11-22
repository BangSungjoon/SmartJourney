<template>
    <div>
        <canvas id="myChart"></canvas>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useFinStore } from '@/stores/counter';
const store = useFinStore()
console.log(store.risk_port)
onMounted(() => {
    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: [
                '저위험',
                '중저위험',
                '중위험',
                '중고위험',
                '고위험'
            ],
            datasets: [{
                label: 'My First Dataset',
                // data: [300, 50, 100],
                data: [store.risk_port[0], store.risk_port[1], store.risk_port[2], store.risk_port[3], store.risk_port[4]],
                backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(153, 102, 255)'
                ],
                hoverOffset: 4
            }]
        }
    })
})

</script>

<style scoped>

</style>