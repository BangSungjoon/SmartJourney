<template>
    <div>
        <h1>포트폴리오 페이지</h1>
        <p>포트폴리오 소개가 들어갈 예정</p>
        <RouterLink v-if="userId" :to="{ name:'portlist', params: { id: userId } }">
            포트폴리오 리스트 보러가기
        </RouterLink>
        <PortfolioForm />
    </div>
</template>

<script setup>
import PortfolioForm from '@/components/PortfolioForm.vue';
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const userId = ref(null);

onMounted(() => {
  const token = localStorage.getItem('token');
  if (token) {
    axios.get('http://127.0.0.1:8000/accounts/user/', {
      headers: {
        'Authorization': `Token ${token}`,
      }
    })
      .then(response => {
        console.log(response.data.pk)
        userId.value = response.data.pk;
      })
      .catch(error => {
        console.error('Failed to fetch user information:', error);
      });
  }
});

</script>

<style lang="scss" scoped>

</style>