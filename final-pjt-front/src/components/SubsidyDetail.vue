<template>
  <div class="subsidy-detail">
    <div class="header">
      <button class="back-btn" @click="$emit('close')">
        <span class="back-arrow">←</span> 목록으로 돌아가기
      </button>
    </div>

    <div class="content-wrapper">
      <div class="title-section">
        <h2>{{ subsidy.service_nm }}</h2>
        <span class="type-badge">{{ subsidy.support_type }}</span>
      </div>

      <div class="purpose-section">
        <p>{{ subsidy.service_pur }}</p>
      </div>

      <div class="details-section">
        <div class="detail-item">
          <h3>지원 대상</h3>
          <p>{{ subsidy.eligibility }}</p>
        </div>

        <div class="detail-item">
          <h3>지원 내용</h3>
          <p>{{ subsidy.support_details }}</p>
        </div>

        <div class="detail-item">
          <h3>신청 방법</h3>
          <p>{{ subsidy.application_method }}</p>
          <p v-if="subsidy.application_deadline" class="deadline">
            <span class="deadline-label">신청 기한:</span> 
            {{ subsidy.application_deadline }}
          </p>
        </div>

        <div class="contact-section">
          <div class="agency-info">
            <h3>문의처</h3>
            <p><strong>담당 기관:</strong> {{ subsidy.agency_name }}</p>
            <p v-if="subsidy.contact_number">
              <strong>문의 전화:</strong> {{ subsidy.contact_number }}
            </p>
          </div>
        </div>
      </div>

      <div class="action-section">
        <a :href="subsidy.detail_url" 
           target="_blank" 
           class="more-info-btn">
          자세히 보기
          <span class="arrow">→</span>
        </a>
      </div>
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
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  max-width: 800px;
  margin: 0 auto;
  overflow: hidden;
  font-family: 'Noto Sans KR', sans-serif;
}

.header {
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: none;
  background-color: #f5f5f5;
  border-radius: 8px;
  color: #555;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-btn:hover {
  background-color: #ebebeb;
}

.back-arrow {
  font-size: 1.2em;
}

.content-wrapper {
  padding: 32px;
}

.title-section {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.title-section h2 {
  margin: 0;
  font-size: 1.8rem;
  color: #333;
  font-weight: 600;
}

.type-badge {
  padding: 6px 16px;
  background-color: #E8F5E9;
  color: #4CAF50;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
}

.purpose-section {
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 12px;
  margin-bottom: 32px;
}

.purpose-section p {
  margin: 0;
  color: #555;
  line-height: 1.6;
}

.details-section {
  display: flex;
  flex-direction: column;
  gap: 32px;
  text-align: left;
}

.detail-item {
  border-bottom: 1px solid #eee;
  padding-bottom: 24px;
  text-align: left;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-item h3 {
  color: #2E7D32;
  font-size: 1.2rem;
  margin-bottom: 12px;
  font-weight: 600;
  text-align: left;
}

.detail-item p {
  color: #444;
  line-height: 1.7;
  margin: 0;
  text-align: left;
}

.deadline {
  margin-top: 12px;
  color: #d32f2f;
  font-weight: 500;
}

.deadline-label {
  color: #666;
  font-weight: normal;
}

.contact-section {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 12px;
  margin-top: 16px;
  text-align: left;
}

.agency-info h3 {
  color: #333;
  font-size: 1.1rem;
  margin-bottom: 12px;
}

.agency-info p {
  margin: 8px 0;
  color: #555;
  text-align: left;
}

.action-section {
  margin-top: 32px;
  text-align: center;
}

.more-info-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.more-info-btn:hover {
  background-color: #388E3C;
  transform: translateY(-2px);
}

.arrow {
  font-size: 1.2em;
}

@media (max-width: 768px) {
  .content-wrapper {
    padding: 20px;
  }

  .title-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .title-section h2 {
    font-size: 1.5rem;
  }
}
</style>