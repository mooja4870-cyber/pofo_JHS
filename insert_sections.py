import re

filepath = '/Users/l/project/pofo_JHS/portfolio_2.html'
with open(filepath, 'r') as f:
    content = f.read()

# 삽입할 Experience & Skills HTML (Tailwind / NEURAL.CORE 스타일 적용)
new_html = """
<!-- Experience Section -->
<section id="experience" class="mb-24">
<div class="flex items-center gap-4 mb-4">
<span class="h-[1px] w-12 bg-primary-fixed-dim"></span>
<span class="font-label-mono text-label-mono text-primary-fixed-dim uppercase tracking-[0.2em]">Career Track</span>
</div>
<h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-background mb-8">
                Professional <span class="text-primary-fixed-dim cyber-glow">Experience</span>
</h2>

<div class="space-y-6">
    <!-- Exp 1 -->
    <div class="glass-card rounded-xl p-6 md:p-8 hover:border-primary-fixed-dim/50 transition-all">
        <div class="flex flex-col md:flex-row justify-between md:items-center mb-4 gap-4">
            <div>
                <h3 class="font-headline-sm text-2xl text-on-background">혁신담당</h3>
                <div class="font-label-mono text-sm text-secondary-fixed-dim mt-1">(주)한솔서플라이</div>
            </div>
            <span class="px-3 py-1 bg-surface-container-highest rounded-full text-sm font-label-mono text-on-surface-variant whitespace-nowrap">2020.04 - 2022.07</span>
        </div>
        <p class="text-on-surface-variant font-body-lg mb-4">기업 비용절감 및 효율화 사업 추진, 업무전산화를 통한 프로세스 혁신</p>
        <ul class="space-y-2">
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">정부지원 바우처사업으로 비용항목별 비용절감 분석 및 개선방안 보고서 작성</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">업무전산화 실행으로 수일 소요 작업을 1시간으로 단축 (90% 이상 업무시간 단축)</span>
            </li>
        </ul>
    </div>

    <!-- Exp 2 -->
    <div class="glass-card rounded-xl p-6 md:p-8 hover:border-primary-fixed-dim/50 transition-all">
        <div class="flex flex-col md:flex-row justify-between md:items-center mb-4 gap-4">
            <div>
                <h3 class="font-headline-sm text-2xl text-on-background">기업혁신본부 본부장</h3>
                <div class="font-label-mono text-sm text-secondary-fixed-dim mt-1">탭코리아㈜</div>
            </div>
            <span class="px-3 py-1 bg-surface-container-highest rounded-full text-sm font-label-mono text-on-surface-variant whitespace-nowrap">2016.06 - 2018.01</span>
        </div>
        <p class="text-on-surface-variant font-body-lg mb-4">경영혁신 추진 및 제반 업무개선 전담</p>
        <ul class="space-y-2">
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">작은혁신 실천 10대과제 운영을 통한 혁신인프라 구축</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">협력사 납입부품 품질향상으로 라인불량율 3.3% → 2.1% 개선</span>
            </li>
        </ul>
    </div>

    <!-- Exp 3 -->
    <div class="glass-card rounded-xl p-6 md:p-8 hover:border-primary-fixed-dim/50 transition-all">
        <div class="flex flex-col md:flex-row justify-between md:items-center mb-4 gap-4">
            <div>
                <h3 class="font-headline-sm text-2xl text-on-background">관세그룹 그룹장</h3>
                <div class="font-label-mono text-sm text-secondary-fixed-dim mt-1">삼성SDI㈜</div>
            </div>
            <span class="px-3 py-1 bg-surface-container-highest rounded-full text-sm font-label-mono text-on-surface-variant whitespace-nowrap">2011.01 - 2016.05</span>
        </div>
        <p class="text-on-surface-variant font-body-lg mb-4">삼성SDI 전사 관세관리 선진화 추진, AEO 인증 및 보세공장 도입 운영</p>
        <ul class="space-y-2">
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">보세공장 도입/운영으로 연 39억원 관세손실 방지</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">AEO(수출입안전관리우수기업) AAA 등급 획득</span>
            </li>
        </ul>
    </div>

    <!-- Exp 4 -->
    <div class="glass-card rounded-xl p-6 md:p-8 hover:border-primary-fixed-dim/50 transition-all">
        <div class="flex flex-col md:flex-row justify-between md:items-center mb-4 gap-4">
            <div>
                <h3 class="font-headline-sm text-2xl text-on-background">말레이지아 법인 구매팀장</h3>
                <div class="font-label-mono text-sm text-secondary-fixed-dim mt-1">삼성SDI㈜</div>
            </div>
            <span class="px-3 py-1 bg-surface-container-highest rounded-full text-sm font-label-mono text-on-surface-variant whitespace-nowrap">2003.10 - 2007.10</span>
        </div>
        <p class="text-on-surface-variant font-body-lg mb-4">법인 구매업무 총괄 수행, 구매가 인하 및 물량배분 관리</p>
        <ul class="space-y-2">
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">매년 구매가 인하율 평균 13% 달성</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="material-symbols-outlined text-primary-fixed-dim text-sm mt-1">check_circle</span>
                <span class="text-on-surface-variant font-body-md">전사 브라운관 이익율 15% 창출 기여</span>
            </li>
        </ul>
    </div>
</div>
</section>

<!-- Skills Section -->
<section id="skills" class="mb-24">
<div class="flex items-center gap-4 mb-4">
<span class="h-[1px] w-12 bg-primary-fixed-dim"></span>
<span class="font-label-mono text-label-mono text-primary-fixed-dim uppercase tracking-[0.2em]">Core Competencies</span>
</div>
<h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-background mb-8">
                Professional <span class="text-primary-fixed-dim cyber-glow">Skills</span>
</h2>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="glass-card rounded-xl p-6 border-t-2 border-t-primary-fixed-dim">
        <h3 class="font-headline-sm text-xl text-on-background mb-4">💼 Procurement</h3>
        <ul class="space-y-2">
            <li class="text-on-surface-variant font-label-mono text-sm"># 구매 전략 및 관리</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 공급사 평가/관리</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 원가절감 및 협상</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># Global 소싱</li>
        </ul>
    </div>

    <div class="glass-card rounded-xl p-6 border-t-2 border-t-secondary-fixed-dim">
        <h3 class="font-headline-sm text-xl text-on-background mb-4">📊 Planning</h3>
        <ul class="space-y-2">
            <li class="text-on-surface-variant font-label-mono text-sm"># 통관 및 환급 관리</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># Q-Cost 관리</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 구매 KPI 수립</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 데이터 분석</li>
        </ul>
    </div>

    <div class="glass-card rounded-xl p-6 border-t-2 border-t-primary-fixed-dim">
        <h3 class="font-headline-sm text-xl text-on-background mb-4">🚀 Innovation</h3>
        <ul class="space-y-2">
            <li class="text-on-surface-variant font-label-mono text-sm"># 프로세스 개선</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 업무 전산화</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 비용 최적화</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 6 Sigma 적용</li>
        </ul>
    </div>

    <div class="glass-card rounded-xl p-6 border-t-2 border-t-secondary-fixed-dim">
        <h3 class="font-headline-sm text-xl text-on-background mb-4">👥 Leadership</h3>
        <ul class="space-y-2">
            <li class="text-on-surface-variant font-label-mono text-sm"># 팀 성과 창출</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 조직원 코칭/개발</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 윤리 구매 정착</li>
            <li class="text-on-surface-variant font-label-mono text-sm"># 변혁적 리더십</li>
        </ul>
    </div>
</div>
</section>

"""

target = "<!-- Projects / Active Innovations Header -->"
if target in content:
    content = content.replace(target, new_html + target)
    with open(filepath, 'w') as f:
        f.write(content)
    print("Successfully inserted Experience and Skills sections.")
else:
    print("Error: Could not find the target comment to insert sections.")

