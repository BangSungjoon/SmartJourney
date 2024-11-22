<template>
    <div>
        <p>{{ user.username }}의 마이페이지 입니다.</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useFinStore } from '@/stores/counter'

const route = useRoute()
const store = useFinStore()
const token = store.token
const headers = {
    'Authorization': `Token ${token}`,
};
const user = ref('')

onMounted(() => {
    console.log(`params id는 ${route.params.id}`)
	axios({
		method: 'get',
		url: `${store.API_URL}/accounts/user/`,
        headers: headers
	})
		.then((res) => {
			console.log(res.data.username)
            user.value = res.data
            console.log(user.value)
            // portfolios.value = res.data
            // console.log(portfolios.value)
		})
		.catch(err => console.log(err))
})
</script>

<style lang="scss" scoped>

</style>