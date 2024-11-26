<template>
  <div class="subsidy-results">
    <h2>맞춤 보조금 검색 결과</h2>
    
    <div v-if="loading" class="loading">
      검색 중...
    </div>

    <div v-else-if="matchedSubsidies.length" class="mt-4">
      <div class="search-container">
        <input 
          type="text" 
          v-model="searchKeyword"
          placeholder="보조금 이름으로 검색"
          class="search-input"
        >
      </div>

      <SubsidyList 
        v-if="!selectedSubsidy"
        :subsidies="paginatedSubsidies"
        @select-subsidy="showDetail"
      />
      <SubsidyDetail
        v-else
        :subsidy="selectedSubsidy"
        @close="selectedSubsidy = null"
      />

      <div class="pagination" v-if="!selectedSubsidy">
        <button 
          :disabled="currentPage === 1"
          @click="currentPage--"
          class="page-btn"
        >
          이전
        </button>
        <span class="page-info">{{ currentPage }} / {{ totalPages }}</span>
        <button 
          :disabled="currentPage === totalPages"
          @click="currentPage++"
          class="page-btn"
        >
          다음
        </button>
      </div>
    </div>

    <div v-else class="no-results">
      <p>죄송합니다. 조건에 맞는 보조금을 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useFinStore } from '@/stores/counter'
import axios from 'axios'
import SubsidyList from '@/components/SubsidyList.vue'
import SubsidyDetail from '@/components/SubsidyDetail.vue'

const store = useFinStore()
const matchedSubsidies = ref([])
const loading = ref(true)
const selectedSubsidy = ref(null)
const searchKeyword = ref('')
const currentPage = ref(1)
const itemsPerPage = 10

const filteredSubsidies = computed(() => {
  if (!searchKeyword.value) return matchedSubsidies.value
  
  return matchedSubsidies.value.filter(subsidy => 
    subsidy.service_nm.toLowerCase().includes(searchKeyword.value.toLowerCase())
  )
})

const paginatedSubsidies = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage
  return filteredSubsidies.value.slice(startIndex, startIndex + itemsPerPage)
})

const totalPages = computed(() => {
  return Math.ceil(filteredSubsidies.value.length / itemsPerPage)
})

watch(searchKeyword, () => {
  currentPage.value = 1
})

const showDetail = (subsidy) => {
  selectedSubsidy.value = subsidy
}

const fetchMatchedSubsidies = function () {
  const token = store.token
  const headers = {
    'Authorization': `Token ${token}`,
  };
  console.log('matching 시작')
  axios({
    method: 'get',
    url: `${store.API_URL}/financial_products/matching_subsidies/`,
    headers: headers
  })
  .then((response) => {
    matchedSubsidies.value = response.data
    console.log(matchedSubsidies.value)
  })
  .catch((error) => {
    console.error('보조금 매칭 결과 조회 실패:', error)
  })
  .finally(() => {
    loading.value = false
  })
}

onMounted(() => {
  fetchMatchedSubsidies()
})
</script>

<style scoped>
.subsidy-results {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Noto Sans KR', sans-serif;
}

.loading {
  text-align: center;
  padding: 20px;
}

.no-results {
  text-align: center;
  padding: 20px;
  color: #666;
}

.search-container {
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.search-input:focus {
  outline: none;
  border-color: #4CAF50;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  gap: 10px;
}

.page-btn {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background-color: white;
  border-radius: 4px;
  cursor: pointer;
}

.page-btn:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.page-info {
  padding: 8px 16px;
}
</style>