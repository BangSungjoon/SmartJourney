<template>
    <div>
        <form @submit.prevent="createPortfolio">
            <div class="mb-3">
                <label for="termInput" class="form-label">목표를 언제까지 달성하고 싶으신가요? (단위: 년)</label>
                <input type="number" class="form-control" id="termInput" v-model="term">
                <div id="termHelp" class="form-text">단기 (1년 이내), 중기 (1~5년), 장기 (5년 이상), 1년 이내는 1년으로 작성해주세요.</div>
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
                    <option value="job-none">무직</option>
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
import { useFinStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useFinStore()
const router = useRouter()

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
    // riskPort()
    createAnswer()
    console.log(SaveInvTypeFunc())
    console.log(PortInvType())
    console.log(PortSaveType())
    store.risk_port = riskPort()
}

const createAnswer = function () {
    const token = store.token // 실제 사용자 토큰 값으로 대체
    const headers = {
    'Authorization': `Token ${token}`,
    };
    axios({
        method: 'post',
        url: `${store.API_URL}/financial_products/save_answer/`,
        data: {
            q1_expected_goal_amount: goalMoney.value,
            q2_goal_duration: term.value,
            q3_income_source: job.value,
            q4_emergency_fund_status: emerMoney.value,
            q5_investment_priority: important.value,
            q6_safety_or_liquidity: safeUtility.value,
            q7_household_status: family.value,
        },
        headers: headers // 헤더 추가
    }).then(() => {
        console.log('db 저장 성공')
        router.push({ name: 'home' })
    }).catch(err => console.log(err))
}

const riskPort = function () {
    let risk_low = 0      // 저위험
    let risk_m_low = 0    // 중저위험
    let risk_m = 0        // 중위험
    let risk_m_high = 0   // 중고위험
    let risk_high = 0     // 고위험
    // 목표 기간 - 가중치 0.4
    if (term.value <= 1) {
        risk_low += 0.4*80
        risk_m_low += 0.4*20
    }
    else if (1 < term.value < 5) {
        risk_low += 0.4*50
        risk_m_low += 0.4*30
        risk_m += 0.4*20
    }
    else if (5 <= term.value) {
        risk_low += 0.4*20
        risk_m_low += 0.4*20
        risk_m += 0.4*30
        risk_m_high += 0.4*20
        risk_high += 0.4*10
    }
    // 투자할 때 더 중요하게 여기는 것 - 가중치 0.3
    if (important.value === 'loss_min') {
        risk_low += 0.3*80
        risk_m_low += 0.3*20
    }
    else if (important.value === 'balance') {
        risk_low += 0.3*30
        risk_m_low += 0.3*30
        risk_m += 0.3*20
        risk_m_high += 0.3*10
        risk_high += 0.3*10
    }
    else if (important.value === 'risk') {
        risk_m_low += 0.3*20
        risk_m += 0.3*20
        risk_m_high += 0.3*30
        risk_high += 0.3*30
    }
    // 비상자금 여부 - 가중치 0.2
    if (emerMoney.value === '119-zero') {
        risk_low += 0.2*80
        risk_m_low += 0.2*20
    }
    else if (emerMoney.value === '119-few') {
        risk_low += 0.2*50
        risk_m_low += 0.2*30
        risk_m += 0.2*20
    }
    else if (emerMoney.value === '119-rich') {
        risk_low += 0.2*30
        risk_m_low += 0.2*20
        risk_m += 0.2*20
        risk_m_high += 0.2*20
        risk_high += 0.2*10
    }
    // 안전성과 유동성 중 중요한 부분 - 가중치 0.1
    if (safeUtility.value === 'SafeOrUtility-safe') {
        risk_low += 0.1*80
        risk_m_low += 0.1*20
    }
    else if (safeUtility.value === 'SafeOrUtility-util') {
        risk_low += 0.1*40
        risk_m_low += 0.1*30
        risk_m += 0.1*20
        risk_m_high += 0.1*10
    }
    else if (safeUtility.value === 'SafeOrUtility-balance') {
        risk_low += 0.1*50
        risk_m_low += 0.1*30
        risk_m += 0.1*20
    }
    // 목표를 달성하기 위해 필요한 애상 금액
    if (goalMoney.value <= 1000) {
        risk_low += 5
    }
    else if (5000 <= goalMoney.value) {
        risk_high += 5
    }
    // 현재 소득을 얻는 형태
    if (job.value === 'job-fulltime') {
        risk_m_high += 3
        risk_high += 2
    }
    else if (job.value === 'job-parttime') {
        risk_low += 3
        risk_m_low += 2
    }
    else if (job.value === 'job-invest') {
        risk_high += 5
    }
    else if (job.value === 'job-none') {
        risk_low += 5
    }
    // 가계 상황 (피부양자 여부 등)
    if (family.value === 'family-solo-dependent') {
        risk_low += 3
        risk_m_low += 2
    }
    else if (family.value === 'family-solo') {
        risk_low += 2
        risk_m_low += 1
    }
    else if (family.value === 'family-couple-dependent') {
        risk_m_low += 3
        risk_m += 2
    }
    else if (family.value === 'family-couple') {
        risk_m += 3
        risk_high += 2
    }
    console.log(risk_low)
    const total = risk_low + risk_m_low + risk_m + risk_m_high + risk_high
    let riskArray = [risk_low, risk_m_low, risk_m, risk_m_high, risk_high]
    riskArray.forEach((risk, index) => {
        riskArray[index] = (risk/total)*100
    });
    [risk_low, risk_m_low, risk_m, risk_m_high, risk_high] = riskArray
    console.log([risk_low, risk_m_low, risk_m, risk_m_high, risk_high])
    return riskArray
}

// 저축 vs 투자
const SaveInvTypeFunc = function () {
    let saving_score = 0; // 저축 상품 점수
    let inv_score = 0   // 투자 상품 점수

    //q1
    if (term.value <= 1) {
        saving_score += 80 * 0.4
        inv_score += 20 * 0.4
    } else if (term.value > 1 && term.value < 5) {
        saving_score += 50 * 0.4
        inv_score += 50 * 0.4
    } else if (term.value >= 5) {
        saving_score += 20 * 0.4
        inv_score += 80 * 0.4
    } 
    //q2
    if (important.value === 'loss_min') {
        saving_score += 80 * 0.3
        inv_score += 20 * 0.3
    } else if (important.value === 'balance') {
        saving_score += 50 * 0.3
        inv_score += 50 * 0.3
    } else if (important.value === 'risk') {
        saving_score += 20 * 0.3
        inv_score += 80 * 0.3
    }
    // q3
    if (emerMoney.value === '119-zero') {
        saving_score += 80 * 0.2
        inv_score += 20 * 0.2
    } else if (emerMoney.value === '119-few') {
        saving_score += 50 * 0.2
        inv_score += 50 * 0.2
    } else if (emerMoney.value === '119-rich') {
        saving_score += 20 * 0.2
        inv_score += 80 * 0.2
    }
    // q4
    if (safeUtility.value === 'SafeOrUtility-safe') {
        saving_score += 80 * 0.1
        inv_score += 20 * 0.1
    } else if (safeUtility.value === 'SafeOrUtility-balance') {
        saving_score += 50 * 0.1
        inv_score += 50 * 0.1
    } else if (safeUtility.value === 'SafeOrUtility-util') {
        saving_score += 50 * 0.1
        inv_score += 50 * 0.1
    }
    // q5
    if (goalMoney.value <= 1000) {
        saving_score += 5
    } else if (goalMoney.value >= 5000) {
        inv_score += 5
    }
    // q6
    if (job.value === 'job-fulltime') {
        inv_score += 3
    } else if (job.value === 'job-parttime') {
        saving_score += 3
    } else if (job.value === 'job-invest') {
        inv_score += 5
    } else if (job.value === 'job-none') {
        saving_score += 5
    }
    // q7
    if (family.value === 'family-solo-dependent') {
        saving_score += 5
        inv_score -= 5
    } else if (family.value === 'family-solo') {
        saving_score += 3
        inv_score -= 3
    } else if (family.value === 'family-couple-dependent') {
        saving_score += 3
        inv_score += 3
    } else if (family.value === 'family-couple') {
        saving_score -= 5
        inv_score += 5
    }

    const temp_saving_score = saving_score
    saving_score = saving_score/(saving_score + inv_score)
    inv_score = inv_score/(temp_saving_score + inv_score)

        return{saving_score, inv_score}
}


// 투자 상품 내
const PortInvType = function () {
    let dom_stock_score = 0; // 국내 주식형
    let int_stock_score = 0   // 해외 주식형
    let bond_score = 0   // 채권형
    let alt_invest_score = 0   // 대안투자
    

    //q1
    if (term.value <= 1) {
        dom_stock_score += 10 * 0.4
        int_stock_score += 10 * 0.4
        bond_score += 80 * 0.4
    } else if (term.value > 1 && term.value < 5) {
        dom_stock_score += 30 * 0.4
        int_stock_score += 20 * 0.4
        bond_score += 40 * 0.4
        alt_invest_score += 10 * 0.4
    } else if (term.value >= 5) {
        dom_stock_score += 30 * 0.4
        int_stock_score += 40 * 0.4
        bond_score += 10 * 0.4
        alt_invest_score += 20 * 0.4
    } 
    // q2
    if (important.value === 'loss_min') {
        dom_stock_score += 10 * 0.3
        int_stock_score += 10 * 0.3
        bond_score += 80 * 0.3
    } else if (important.value === 'balance') {
        dom_stock_score += 25 * 0.3
        int_stock_score += 25 * 0.3
        bond_score += 30 * 0.3
        alt_invest_score += 20 * 0.3
    } else if (important.value === 'risk') {
        dom_stock_score += 30 * 0.3
        int_stock_score += 40 * 0.3
        bond_score += 10 * 0.3
        alt_invest_score += 20 * 0.3
    }
    // q3
    if (emerMoney.value === '119-zero') {
        dom_stock_score += 10 * 0.3
        int_stock_score += 10 * 0.3
        bond_score += 80 * 0.3
    } else if (emerMoney.value === '119-few') {
        dom_stock_score += 30 * 0.3
        int_stock_score += 20 * 0.3
        bond_score += 40 * 0.3
        alt_invest_score += 10 * 0.3
    } else if (emerMoney.value === '119-rich') {
        dom_stock_score += 30 * 0.3
        int_stock_score += 40 * 0.3
        bond_score += 10 * 0.3
        alt_invest_score += 20 * 0.3
    }
    // q5
    if (goalMoney.value <= 1000) {
        bond_score += 5
    } else if (goalMoney.value >= 5000) {
        dom_stock_score += 3
        alt_invest_score += 3
    }
    // q6
    if (job.value === 'job-fulltime') {
        int_stock_score += 3
        alt_invest_score += 2
    } else if (job.value === 'job-parttime') {
        dom_stock_score += 3
        bond_score += 2
    } else if (job.value === 'job-invest') {
        alt_invest_score += 5
    } else if (job.value === 'job-none') {
        bond_score += 5
    }
    // q7
    if (family.value === 'family-solo-dependent') {
        dom_stock_score += 3
        bond_score += 5
    } else if (family.value === 'family-solo') {
        dom_stock_score += 2
        int_stock_score += 2
        bond_score += 3
    } else if (family.value === 'family-couple-dependent') {
        int_stock_score += 2
        bond_score += 2
        alt_invest_score += 3
    } else if (family.value === 'family-couple') {
        int_stock_score +=3
        alt_invest_score += 5
    }

    const temp_dom_stock_score = dom_stock_score
    const temp_int_stock_score = int_stock_score
    const temp_bond_score = bond_score
    const temp_alt_invest_score = alt_invest_score
    dom_stock_score = temp_dom_stock_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)
    int_stock_score = temp_int_stock_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)
    bond_score = temp_bond_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)
    alt_invest_score = temp_alt_invest_score/(temp_dom_stock_score + temp_int_stock_score + temp_bond_score + temp_alt_invest_score)

        return{dom_stock_score, int_stock_score, bond_score, alt_invest_score}
}

// 저축 상품 내
const PortSaveType = function () {
    let reg_save_score = 0   // 보통예금
    let inst_save_score = 0; // 적금/정기예금

    //q1
    if (term.value <= 1) {
        reg_save_score += 80 * 0.4
        inst_save_score += 20 * 0.4
    } else if (term.value > 1 && term.value < 5) {
        reg_save_score += 50 * 0.4
        inst_save_score += 50 * 0.4
    } else if (term.value >= 5) {
        reg_save_score += 20 * 0.4
        inst_save_score += 80 * 0.4
    } 
    // q3
    if (emerMoney.value === '119-zero') {
        reg_save_score += 80 * 0.2
        inst_save_score += 20 * 0.2
    } else if (emerMoney.value === '119-few') {
        reg_save_score += 50 * 0.2
        inst_save_score += 50 * 0.2
    } else if (emerMoney.value === '119-rich') {
        reg_save_score += 20 * 0.2
        inst_save_score += 80 * 0.2
    }
    // q4
    if (safeUtility.value === 'SafeOrUtility-safe') {
        reg_save_score += 20 * 0.3
        inst_save_score += 80 * 0.3
    } else if (safeUtility.value === 'SafeOrUtility-balance') {
        reg_save_score += 50 * 0.3
        inst_save_score += 50 * 0.3
    } else if (safeUtility.value === 'SafeOrUtility-util') {
        reg_save_score += 80 * 0.3
        inst_save_score += 20 * 0.3
    }
    // q5
    if (goalMoney.value <= 1000) {
        reg_save_score += 5
    } else if (goalMoney.value >= 5000) {
        inst_save_score += 5
    }
    // q6
    if (job.value === 'job-fulltime') {
        reg_save_score += 40 * 0.1
        inst_save_score += 60 * 0.1
    } else if (job.value === 'job-parttime') {
        reg_save_score += 60 * 0.1
        inst_save_score += 40 * 0.1
    } else if (job.value === 'job-invest') {
        reg_save_score += 50 * 0.1
        inst_save_score += 50 * 0.1
    } else if (job.value === 'job-none') {
        reg_save_score += 70 * 0.1
        inst_save_score += 30 * 0.1
    }
    // q7
    if (family.value === 'family-solo-dependent') {
        reg_save_score -= 3
        inst_save_score += 3
    } else if (family.value === 'family-solo') {
        reg_save_score -= 2
        inst_save_score += 2
    } else if (family.value === 'family-couple-dependent') {
        inst_save_score += 2
    } else if (family.value === 'family-couple') {
        reg_save_score += 2
        inst_save_score -= 2
    }

    const temp_reg_save_score = reg_save_score
    reg_save_score = reg_save_score/(reg_save_score + inst_save_score)
    inst_save_score = inst_save_score/(temp_reg_save_score + inst_save_score)

        return{reg_save_score, inst_save_score}
}

</script>

<style scoped>

</style>