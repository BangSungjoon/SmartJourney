import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

export const useFinStore = defineStore('finance', () => {
    const token = ref(localStorage.getItem('token') || null);
    const userId = ref(localStorage.getItem('userId') || null); // user 정보 추가
    const API_URL = 'http://127.0.0.1:8000'
    const router = useRouter()
    const route = useRoute()
    const myPortfolios = ref([]) // 내가 작성한 포트폴리오 DB에서 꺼내와서 담을 변수
    const headers = ref({
        'Authorization': `Token ${token.value}`
    })
    const depositFavorites = ref([])
    const savingFavorites = ref([])

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
    // const logIn = function (payload) {
    //     const username = payload.username
    //     const password = payload.password
    //     axios({
    //         method: 'post',
    //         url: `${API_URL}/accounts/login/`,
    //         data: {
    //             username, password
    //         }
    //     })
    //         .then(res => {
    //             console.log('로그인이 완료되었습니다.')
    //             token.value = res.data.key
    //             // console.log(res.data)
    //             // user.value = res.data.user
    //             localStorage.setItem('token', token.value)
    //             router.push({ name: 'home' })
    //             // window.location.reload()
    //         })
    //         .catch(err => console.log(err))
    // }
    // 로그인
    const logIn = function (payload) {
        const username = payload.username
        const password = payload.password
        axios({
            method: 'post',
            url: `${API_URL}/accounts/login/`,
            data: { username, password }
        })
            .then(res => {
                token.value = res.data.key
                localStorage.setItem('token', token.value)

                // 로그인 후, user 정보를 가져오는 API 호출
                axios({
                    method: 'get',
                    url: `${API_URL}/accounts/user/`,  // 유저 정보를 가져오는 엔드포인트
                    headers: {
                        'Authorization': `Token ${token.value}`
                    }
                })
                    .then(response => {
                        userId.value = response.data.pk
                        localStorage.setItem('userId', userId.value)
                        router.push({ name: 'home' })
                    })
                    .catch(err => {
                        console.error('Failed to fetch user information:', err)
                    })
            })
            .catch(err => console.log(err))
    }

    // 로그아웃
    const logOut = () => {
        token.value = null
        userId.value = null  // 로그아웃 시 userId 초기화
        localStorage.removeItem('token')
        localStorage.removeItem('userId')
        router.push({ name: 'home' })
    }

    // 로그인 상태 확인
    const isLoggedIn = computed(() => !!token.value)  // 토큰이 있으면 로그인 상태

    // 로그인된 사용자의 id
    const currentUserId = computed(() => userId.value)

    const toggleDepositFavorite = (productId) => {
        const index = depositFavorites.value.indexOf(productId);
        if (index === -1) {
            depositFavorites.value.push(productId);
        } else {
            depositFavorites.value.splice(index, 1);
        }
    }

    const toggleSavingFavorite = (productId) => {
        const index = savingFavorites.value.indexOf(productId);
        if (index === -1) {
            savingFavorites.value.push(productId);
        } else {
            savingFavorites.value.splice(index, 1);
        }
    }

    const isDepositFavorite = (productId) => {
        return depositFavorites.value.includes(productId);
    }

    const isSavingFavorite = (productId) => {
        return savingFavorites.value.includes(productId);
    }

    return { signUp, API_URL, logIn, logOut, token, isLoggedIn, currentUserId, toggleDepositFavorite, toggleSavingFavorite, isDepositFavorite, isSavingFavorite, depositFavorites, savingFavorites }
}, { persist: true })