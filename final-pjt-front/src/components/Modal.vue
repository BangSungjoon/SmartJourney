<template>
    <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content fade-in-fwd">
        <slot></slot>
        <button class="close-btn" @click="closeModal">닫기</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from "vue";
  
  const props = defineProps({
    isVisible: Boolean,
  });
  
  const emit = defineEmits(["close"]);
  
  const closeModal = () => {
    emit("close");
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    /* width: 100vw;
    height: 100vh; */
    width: 100%;
    height: 100%;
    /* background: rgba(0, 0, 0, 0); 불투명 배경 */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 100%;
    /* height: 100%; */
    max-width: 90%;
    animation: slide-in 0.3s ease-in-out; /* 애니메이션 추가 */
  }
  
  .close-btn {
    margin-top: 10px;
    padding: 10px 20px;
    background: #ff5e57;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .close-btn:hover {
    background: #e74c3c;
  }
  
  @keyframes slide-in {
    from {
      transform: translateY(-30px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  </style>
  