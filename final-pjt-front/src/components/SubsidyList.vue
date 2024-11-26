<template>
  <div class="subsidy-list px-0">
    <div v-for="subsidy in subsidies" :key="subsidy.service_id" class="subsidy-item" @click="$emit('select-subsidy', subsidy)">
      <div class="subsidy-content">
        <h3 class="title">{{ subsidy.service_nm }}</h3>
        <div class="subsidy-summary">
          <span class="type">{{ subsidy.support_type }}</span>
          <p class="purpose">{{ subsidy.service_pur }}</p>
        </div>
      </div>
      <div class="arrow">›</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  subsidies: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.subsidy-list {
  padding: 10px;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
}

.subsidy-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 12px;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  cursor: pointer;
  border: 1px solid #eee;
}

.subsidy-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: #4CAF50;
}

.subsidy-content {
  flex: 1;
}

.title {
  font-size: 1.2rem;
  color: #333;
  margin: 0 0 10px 0;
  font-weight: 600;
}

.subsidy-summary {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.type {
  display: inline-block;
  padding: 4px 12px;
  background-color: #E8F5E9;
  color: #4CAF50;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  align-self: flex-start;
}

.purpose {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.arrow {
  font-size: 1.5rem;
  color: #4CAF50;
  margin-left: 15px;
  font-weight: 300;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .subsidy-item {
    padding: 15px;
  }

  .title {
    font-size: 1.1rem;
  }

  .purpose {
    font-size: 0.9rem;
  }
}
</style>