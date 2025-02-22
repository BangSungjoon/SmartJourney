<template>
    <div class="chatbot-container">
      <div class="chat-messages" ref="chatContainer">
        <div v-for="(message, index) in messages" :key="index" 
             :class="['message', message.role === 'user' ? 'user-message' : 'bot-message']">
          {{ message.content }}
        </div>
      </div>
      <div class="chat-input">
        <input type="text" v-model="userInput" @keyup.enter="sendMessage" placeholder="질문을 입력하세요...">
        <button @click="sendMessage">전송</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, nextTick, watch } from 'vue'
  import { useFinStore } from '@/stores/counter'
  import axios from 'axios'
  
  const store = useFinStore()
  const messages = ref([
    {
      role: 'assistant',
      content: '안녕하세요! 저는 당신의 금융 상담사입니다. 어떤 도움이 필요하신가요?'
    }
  ])
  const userInput = ref('')
  const chatContainer = ref(null)
  
  const scrollToBottom = async () => {
    await nextTick()
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
  
  const formatBotResponse = (text) => {
    if (!text) return '';
    
    // 문장 단위로 분리하고 줄바꿈 추가
    const sentences = text.split(/(?<=[.!?])\s+/);
    return sentences
      .filter(sentence => sentence.trim())
      .join('\n');
  }
  
  const sendMessage = async () => {
    if (!userInput.value.trim()) return
  
    messages.value.push({
      role: 'user',
      content: userInput.value
    })
  
    const userMessage = userInput.value
    userInput.value = ''
    
    try {
      // 사용자 관련 모든 데이터 수집
      const userData = await axios.get(`${store.API_URL}/accounts/user/`, {
        headers: { Authorization: `Token ${store.token}` }
      })
  
      // 포트폴리오 데이터 수집
      const portfolioData = await axios.get(`${store.API_URL}/financial_products/my_portfolios/${userData.data.pk}/`, {
        headers: { Authorization: `Token ${store.token}` }
      })
  
      // 금융 상품 데이터 수집
      const [depositResponse, savingResponse] = await Promise.all([
        axios.get(`${store.API_URL}/financial_products/save_deposit/`),
        axios.get(`${store.API_URL}/financial_products/save_saving/`)
      ])
  
      // ChatGPT API 호출을 위한 프롬프트 구성
      const prompt = `
        당신은 금융 전문 AI 상담사입니다. 다음 정보를 바탕으로 사용자의 질문에 답변해주세요:

        1. 사용자 기본 정보:
        - 이름: ${userData.data.username}
        - ID: ${userData.data.pk}

        2. 사용자 포트폴리오 정보:
        - 투자 성향: ${portfolioData.data.investment_style}
        - 위험 선호도: ${portfolioData.data.risk_tolerance}
        - 투자 목표: ${portfolioData.data.investment_goal}

        3. 추천 가능한 금융 상품:
        - 예금 상품 수: ${depositResponse.data.result.baseList.length}개
        - 적금 상품 수: ${savingResponse.data.result.baseList.length}개

        사용자 질문: ${userMessage}

        위 정보를 바탕으로 맞춤형 금융 조언을 제공해주세요.
        답변은 친근하고 이해하기 쉬운 말투로 작성해주세요.
      `
  
      const response = await axios.post(`${store.API_URL}/financial_products/api/chatbot/`, {
        prompt: prompt
      }, {
        headers: {
          'Authorization': `Token ${store.token}`
        }
      })
  
      messages.value.push({
        role: 'assistant',
        content: formatBotResponse(response.data.message)
      })
  
      scrollToBottom()
    } catch (error) {
      console.error('ChatGPT API 호출 중 오류:', error)
      messages.value.push({
        role: 'assistant',
        content: '죄송합니다. 오류가 발생했습니다. 잠시 후 다시 시도해주세요.'
      })
    }
  }
  
  onMounted(() => {
    scrollToBottom()
  })
  
  watch(messages, () => {
    scrollToBottom()
  }, { deep: true })
  </script>
  
  <style scoped>
  .chatbot-container {
    height: 70vh;
    display: flex;
    flex-direction: column;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
  }
  
  .message {
    margin: 10px 0;
    padding: 12px 16px;
    border-radius: 15px;
    max-width: 70%;
    word-wrap: break-word;
    display: inline-block;
    white-space: pre-line;
  }
  
  .user-message {
    background-color: #007bff;
    color: white;
    margin-left: auto;
    border-top-right-radius: 5px;
    text-align: right;
  }
  
  .bot-message {
    background-color: #f0f0f0;
    color: #333;
    margin-right: auto;
    border-top-left-radius: 5px;
    text-align: left;
    white-space: pre-line;
  }
  
  .chat-input {
    display: flex;
    padding: 20px;
    gap: 10px;
    border-top: 1px solid #eee;
  }
  
  .chat-input input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
  }
  
  .chat-input button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .chat-input button:hover {
    background-color: #0056b3;
  }
  
  .message-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    margin: 5px 0;
  }
  
  .message-time {
    font-size: 0.75rem;
    color: #888;
    margin: 2px 5px;
    text-align: center;
  }
  
  .message {
    animation: fadeIn 0.3s ease-in-out;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .button-group button {
    padding: 8px 16px;
    margin: 5px;
    border: 1px solid #ddd;
    border-radius: 20px;
    background-color: white;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .button-group button.selected {
    background-color: #1a73e8;  /* Google Blue 색상 */
    color: white;
    border-color: #1a73e8;
    box-shadow: 0 2px 4px rgba(26, 115, 232, 0.2);  /* 부드러운 그림자 효과 */
  }
  
  .button-group button:hover {
    background-color: #f8f9fa;
  }
  
  .button-group button.selected:hover {
    background-color: #1557b0;  /* 더 진한 파란색 */
    border-color: #1557b0;
  }
  </style>