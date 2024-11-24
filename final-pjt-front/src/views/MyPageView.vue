<template>
    <div>
        <p>{{ user.username }}의 마이페이지 입니다.</p>
        <div class="row">
            <div class="col-9">
                <RouterView />
            </div>
            <div class="col-3">
                <div>
                    <RouterLink :to="{ name: 'mypage-cart' }">
                        내가 찜한 예/적금 상품
                    </RouterLink>
                </div>
                <div>
                    <RouterLink :to="{ name: 'mypage-portlist' }">
                        내 포트폴리오
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useFinStore } from '@/stores/counter'
import axios from 'axios'
import { defineProps } from 'vue';

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

console.log(`props.id는 ${props.id}`); // id 값이 정상적으로 전달됨

const store = useFinStore()
const route = useRoute()
const user = ref('') // 사용자 데이터를 저장할 변수

onMounted(() => {
    const token = localStorage.getItem('token');
    if (token) {
        axios.get('http://127.0.0.1:8000/accounts/user/', {
            headers: { 'Authorization': `Token ${token}` }
        })
            .then((res) => {
                user.value = res.data;
                console.log(`userid는 ${user.value}`)
            })
            .catch((err) => console.log(err))
    }
})
</script>
