<template>
  <div class="subsidy-list">
    <div v-for="subsidy in subsidies" :key="subsidy.service_id" class="subsidy-item" @click="$emit('select-subsidy', subsidy)">
      <h3>{{ subsidy.service_nm }}</h3>
      <div class="subsidy-summary">
        <p class="type">{{ subsidy.support_type }}</p>
        <p class="purpose">{{ subsidy.service_pur }}</p>
      </div>
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
.subsidy-item {
  padding: 15px;
  border: 1px solid #ddd;
  margin-bottom: 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.subsidy-item:hover {
  background-color: #f5f5f5;
}

.subsidy-summary {
  margin-top: 10px;
}

.type {
  color: #666;
  font-size: 0.9em;
}

.purpose {
  margin-top: 5px;
  color: #333;
}
</style>