import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

export const useFinStore = defineStore('finance', () => {
    const token = ref(localStorage.getItem('token') || null);
    // const user = ref(null) // user 정보 추가
    const API_URL = 'http://127.0.0.1:8000'
    const router = useRouter()
    const route = useRoute()
    const myPortfolios = ref([]) // 내가 작성한 포트폴리오 DB에서 꺼내와서 담을 변수
    const headers = ref({
        'Authorization': `Token ${token.value}`
    })

	const signUp = function (payload) {
		const username = payload.username
        const password1 = payload.password1
        const password2 = payload.password2
        console.log(username)

        axios({
            method: 'post',
            url: `${API_URL}/accounts/signup/`,
            data: { 
                username, password1, password2
            }
        })
            .then(res => {
                console.log('회원가입이 완료되었습니다.')
                const password = password1
                logIn({ username, password })
            })
            .catch(err => console.log(err))
	}
    const logIn = function (payload) {
        const username = payload.username
        const password = payload.password
        axios({
            method: 'post',
            url: `${API_URL}/accounts/login/`,
            data: {
                username, password
            }
        })
            .then(res => {
                console.log('로그인이 완료되었습니다.')
                token.value = res.data.key
                // console.log(res.data)
                // user.value = res.data.user
                localStorage.setItem('token', token.value)
                router.push({ name: 'home' })
            })
            .catch(err => console.log(err))
    }



	return { signUp, API_URL, logIn, token }
}, { persist: true })