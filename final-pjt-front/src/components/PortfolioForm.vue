<template>
    <div>
        <form @submit.prevent="createPortfolio">
            <div class="mb-3">
                <label for="termInput" class="form-label">목표를 언제까지 달성하고 싶으신가요? (단위: 년)</label>
                <input type="number" class="form-control" id="termInput" v-model="term">
                <div id="termHelp" class="form-text">단기 (1년 이내), 중기 (1~5년), 장기 (5년 이상)</div>
            </div>
            <div class="mb-3">
                <label for="important" class="form-label">투자할 때 더 중요하게 여기는 것은 무엇인가요?</label>
                <select class="form-select" id="important" v-model="important">
                    <option value="loss_min">손실 최소화</option>
                    <option value="balance">균형</option>
                    <option value="risk">수익 극대화</option>
                </select>
                <div class="form-text">사용자가 손실 최소화와 수익 극대화 중 무엇을 우선 시 하는지에 따라 금융 상품의 위험도를 결정해요.</div>
            </div>
            <div class="mb-3">
                <label for="119money" class="form-label">예기치 않은 상황에 대비한 비상 자금이 마련되어 있나요?</label>
                <select class="form-select" id="119money" v-model="emerMoney">
                    <option value="119-zero">없다.</option>
                    <option value="119-few">약간 있다. (3~6개월 생활비)</option>
                    <option value="119-rich">충분히 있다. (6개월 이상 생활비)</option>
                </select>
                <div class="form-text">비상 자금은 사용자가 감수할 수 있는 투자 손실의 범위를 결정해요. 비상 자금이 충분하다면 고위험 자산 비중을 늘릴 수 있어요.</div>
            </div>
            <div class="mb-3">
                <label for="SafeOrUtility" class="form-label">안정성과 유동성 중 중요하게 여기시는 건 어떤 것 인가요?</label>
                <select class="form-select" id="SafeOrUtility" v-model="safeUtility">
                    <option value="SafeOrUtility-safe">안정성</option>
                    <option value="SafeOrUtility-balance">균형</option>
                    <option value="SafeOrUtility-util">유동성</option>
                </select>
            </div>
            <hr>
            <div class="mb-3">
                <label for="goalMoney" class="form-label">목표 금액이 얼마인가요? (단위: 만원)</label>
                <input type="number" class="form-control" id="goalMoney" v-model="goalMoney">
            </div>
            <div class="mb-3">
                <label for="job" class="form-label">현재 소득은 어떻게 얻고 계신가요?</label>
                <select class="form-select" id="job" v-model="job">
                    <option value="job-fulltime">정규직</option>
                    <option value="job-parttime">계약직/프리랜서</option>
                    <option value="job-invest">투자 소득</option>
                    <option value="job-none">투자 소득</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="family" class="form-label">가계 상황은 어떠신가요?</label>
                <select class="form-select" id="family" v-model="family">
                    <option value="family-solo-dependent">외벌이, 피부양자 있음</option>
                    <option value="family-solo">외벌이, 피부양자 없음</option>
                    <option value="family-couple-dependent">맞벌이, 피부양자 있음</option>
                    <option value="family-couple">맞벌이, 피부양자 없음</option>
                </select>
            </div>
            
            <button type="submit" class="btn btn-primary">나를 위한 포트폴리오 만들기</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const term = ref(null)
const important = ref('loss_min')
const emerMoney = ref('119-zero')
const safeUtility = ref('SafeOrUtility-safe')
const goalMoney = ref(null)
const job = ref('job-fulltime')
const family = ref('family-solo-dependent')

const createPortfolio = function () {
    if (!term.value || !goalMoney.value) {
        alert('필수 입력 항목을 채워주세요.');
        return;
    }
    console.log(term.value)
    console.log(important.value)
    console.log(emerMoney.value)
    console.log(safeUtility.value)
    console.log(goalMoney.value)
    console.log(job.value)
    console.log(family.value)
}
</script>

<style scoped>

</style>