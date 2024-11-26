<template>
  <div class="subsidy-detail">
    <button class="back-btn" @click="$emit('close')">목록으로 돌아가기</button>
    <h3>{{ subsidy.service_nm }}</h3>
    <div class="subsidy-info">
      <p class="type">{{ subsidy.support_type }}</p>
      <p class="purpose">{{ subsidy.service_pur }}</p>
      <div class="details">
        <h4>지원 대상</h4>
        <p>{{ subsidy.eligibility }}</p>
        <h4>지원 내용</h4>
        <p>{{ subsidy.support_details }}</p>
        <h4>신청 방법</h4>
        <p>{{ subsidy.application_method }}</p>
        <p class="deadline" v-if="subsidy.application_deadline">
          신청 기한: {{ subsidy.application_deadline }}
        </p>
      </div>
      <div class="agency-info">
        <p>담당 기관: {{ subsidy.agency_name }}</p>
        <p v-if="subsidy.contact_number">문의: {{ subsidy.contact_number }}</p>
      </div>
      <a :href="subsidy.detail_url" target="_blank" class="more-info-btn">
        자세히 보기
      </a>
    </div>
  </div>
</template>

<script setup>
defineProps({
  subsidy: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.subsidy-detail {
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.back-btn {
  margin-bottom: 20px;
  padding: 8px 16px;
  border: none;
  background-color: #f0f0f0;
  border-radius: 4px;
  cursor: pointer;
}

.details h4 {
  margin-top: 20px;
  margin-bottom: 10px;
  color: #333;
}

.more-info-btn {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}
</style>