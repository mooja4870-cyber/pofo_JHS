# Version History

## v1.9.55

Date: 2026-07-13

### 변경 내용
- DownTube 프로젝트 카드 클릭 시 GitHub 레포지토리 대신 APK 파일이 직접 다운로드되도록 링크 주소 수정(`https://github.com/mooja4870-cyber/DownTube/raw/master/DownTube.apk`).
- 안내 메시지를 'APK 파일 직접 다운로드 (로컬 서버 필요)'로 보완하여 사용자 직관성 개선.

### 수정 파일
- index.html
- ver.md

### 비고
- 다운로드 링크 수정 완료 후 배포

## v1.9.54

Date: 2026-07-13

### 변경 내용
- DownTube 프로젝트(FastAPI 백엔드 기반 유튜브 다운로더 및 안드로이드 APK 솔루션)를 포트폴리오에 추가.
- 카테고리를 Mobile Apps로 지정하고 관련 상세 정보(스택, 깃허브 링크, 로컬 서버 실행 필요 안내) 기재.
- DownTube 전용 네온 사이버 펑크 스타일 썸네일 이미지(downtube_thumb.png) 생성 및 배치.

### 수정 파일
- index.html
- ver.md
- downtube_thumb.png [NEW]

### 비고
- 신규 프로젝트 추가 완료 후 kdanawa.pages.dev로 배포

## v1.9.53

Date: 2026-07-13

### 변경 내용
- 포트폴리오 섹션 헤더 우측 영역에 'All', 'Mobile App.', 'Web App.', 'AI Model' 필터링 버튼 추가.
- 필터 선택 시 해당 카테고리의 포트폴리오만 동적으로 렌더링되도록 renderPortfolio 및 filterPortfolio 함수 구현.
- 렌더링 갱신 시 각 앱의 실시간 조회 수(카운터) 데이터가 유실되지 않도록 자바스크립트 전역 캐싱(cachedClicks) 적용.

### 수정 파일
- index.html
- ver.md

### 비고
- 동적 필터링 및 카운터 캐싱 최적화 완료 후 재배포

## v1.9.52

Date: 2026-07-13

### 변경 내용
- 상단 네비게이션 헤더의 사이트 로고('KDANAWA' 텍스트 및 아이콘) 영역을 클릭 가능한 링크(`<a>`)로 변경.
- 클릭 시 사이트 홈(`https://kdanawa.pages.dev/`)으로 이동하여 편의성 향상.

### 수정 파일
- index.html
- ver.md

### 비고
- 로고 링크 추가 후 재배포

## v1.9.51

Date: 2026-07-13

### 변경 내용
- 앱 추천 팝업 클릭 시 나타나는 스크롤 마커(👇 손가락) 크기를 2배 이상(text-120px) 대폭 확대.
- 마커 애니메이션(상하 바운스) 유지 시간을 기존 3초에서 6초로 연장하여 사용자 시선 유도 효과 강화.

### 수정 파일
- index.html
- ver.md

### 비고
- 크기 및 유지시간 상향 후 kdanawa.pages.dev로 배포

## v1.9.50

Date: 2026-07-13

### 변경 내용
- '오늘의 추천 앱' 팝업 클릭 시 스크롤 버그를 원천 차단하기 위해 팝업 내용을 <a> 태그로 래핑하여 클릭 호환성 100% 확보.
- 스크롤 이동 직후 시선을 집중시키기 위해 대상 앱 카드 상단에 통통 튀는(bounce) 손가락 마커(👇)를 동적으로 생성하고 3초 뒤 사라지도록 UX 강화.

### 수정 파일
- index.html
- ver.md

### 비고
- 스크롤 이동 및 UI 애니메이션 효과 추가 후 재배포

## v1.9.49

Date: 2026-07-13

### 변경 내용
- '오늘의 추천 앱' 팝업 배너 클릭 시 화면 이동(스크롤)이 무시되는 버그 픽스.
- 기존 scrollIntoView 방식 대신 브라우저 및 레이아웃 호환성이 뛰어난 절대 좌표 방식(window.scrollTo)으로 스크롤 로직 교체.

### 수정 파일
- index.html
- ver.md

### 비고
- 스크롤 픽스 후 재배포

## v1.9.48

Date: 2026-07-13

### 변경 내용
- '오늘의 추천 앱(App of the Day)' 팝업 클릭 시, 해당 추천 앱 카드가 위치한 곳으로 화면이 부드럽게 스크롤 되도록 사용자 경험(UX) 개선.

### 수정 파일
- index.html
- ver.md

### 비고
- 스크롤 이동 로직 추가 및 UI 개선

## v1.9.47

Date: 2026-07-13

### 변경 내용
- 포트폴리오 메인 화면(index.html)에 강사 경력 5건(비용절감, 경영혁신, 구매윤리, 엑셀활용, DBase+++ 사내/전문강사) 추가.
- 'Teaching Track' 이라는 신규 섹션(Instructor Experience)을 Professional Experience 하단에 배치.

### 수정 파일
- index.html
- ver.md

### 비고
- 강사 경력 UI 업데이트

## v1.9.46

Date: 2026-07-10

### 변경 내용
- 포트폴리오 내 모바일 앱 카드인 'Yangdo Tax Calculator AI'와 '착한병원 찾기 (Good Hospital)'를 프로젝트 목록 최상단(1번째, 2번째)으로 배치 순서 조정.

### 수정 파일
- index.html
- portfolio_2.html
- ver.md

### 비고
- 카드 순서 조정 후 배포

---

## v1.9.45

Date: 2026-07-10

### 변경 내용
- 브랜드 로고 및 하단 카피라이트의 영문 표기를 기존 'K-DANAWA'에서 하이픈을 제거한 'KDANAWA'로 변경 적용.

### 수정 파일
- index.html
- portfolio_2.html
- ver.md

### 비고
- 브랜드명 최종 수정 후 배포

---

## v1.9.44

Date: 2026-07-10

### 변경 내용
- 브랜드 로고('K-DANAWA')의 폰트 색상을 흰색(`text-white`)으로 수정하여 시각적 가독성 개선.

### 수정 파일
- index.html
- portfolio_2.html
- ver.md

### 비고
- 브랜드명 폰트 색상 수정 후 배포

---

## v1.9.43

Date: 2026-07-10

### 변경 내용
- 포트폴리오 사이트 상단 브랜드명 및 하단 카피라이트의 영문 표기를 기존 'JEONG HO-SIK'에서 'K-DANAWA'로 변경 적용.

### 수정 파일
- index.html
- portfolio_2.html
- ver.md

### 비고
- 브랜드명 변경 후 배포

---

## v1.9.42

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카드의 상세 설명글(`item.desc`) 텍스트 색상을 라이트그레이 계열(`text-zinc-300`)로 수정.
  - 가독성을 극대화하기 위해 기존 노란색(`text-yellow-300`)에서 다크 모드에 잘 어울리는 은은하고 밝은 회색 톤으로 변경 적용.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 디자인 수정 후 Cloudflare kdanawa 재배포.

---

## v1.9.41

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카드의 상세 설명글(`item.desc`) 텍스트 색상을 노란색 계열(`text-yellow-300`)로 수정.
  - 가독성을 극대화하기 위해 기존 주황색(`text-orange-400`)에서 다크 모드에 최적화된 밝은 노란색 톤으로 변경 적용.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 디자인 수정 후 Cloudflare kdanawa 재배포.

---

## v1.9.40

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카드의 상세 설명글(`item.desc`) 텍스트 색상을 주황색 계열(`text-orange-400`)로 수정.
  - 가독성을 높이고 포인트를 주기 위해 기존 회색 톤(`text-on-surface-variant`)에서 선명하고 트렌디한 주황색 톤으로 일괄 변경.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 디자인 수정 후 Cloudflare kdanawa 재배포.

---

## v1.9.39

Date: 2026-07-10

### 변경 내용
- 정호식 프로필 사진(profile.jpg, profile2.jpg)을 신규 웹툰 일러스트 캐릭터 이미지로 전면 교체.
  - 기존 실물 프로필 사진 리소스를 삭제.
  - 전달받은 "회의를 시작하죠" (진지한 표정) 캐릭터 이미지를 `profile.png`로, "산책이 최고지. 반짝!" (윙크 표정) 캐릭터 이미지를 `profile2.png`로 저장.
  - 마우스 호버 시 윙크 표정으로 자연스럽게 변환되는 모션 효과 유지.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md
- profile.png (추가)
- profile2.png (추가)
- profile.jpg (삭제)
- profile2.jpg (삭제)

### 비고
- Cloudflare kdanawa 재배포 완료.

---

## v1.9.38

Date: 2026-07-10

### 변경 내용
- 웹사이트 기본 제목(`<title>`) 및 링크 공유 제목(`og:title`) 수정.
  - 기존: `Jeong Ho-sik | Innovation Portfolio` / `Jeong Ho-sik | AI & Web App Portfolio`
  - 변경: `KDANAWA | Innovation Portfolio` / `KDANAWA | AI & Web App Portfolio`

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 제목 텍스트 수정 후 Cloudflare 재배포.

---

## v1.9.37

Date: 2026-07-10

### 변경 내용
- 웹사이트 링크(URL) 공유 시 카카오톡/문자 등에서 표시되는 미리보기 썸네일(Open Graph Image) 교체.
  - 기존: 별도의 지정이 없어 HTML 상단의 증명사진(profile.jpg)이 자동으로 썸네일로 잡힘.
  - 변경: `og:image`, `og:title`, `og:description` 메타 태그를 명시적으로 추가하여, 링크 공유 시 가장 화려하고 임팩트 있는 **비트코인 AI 예측 대시보드 스크린샷(`btcn_thumb.jpg`)**이 대표 미리보기 이미지로 나타나도록 수정.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare kdanawa 재배포.
- (참고: 카카오톡 등 외부 앱에 이전 이미지가 캐시되어 있을 수 있으므로, 카카오 데브 캐시 삭제 도구를 이용하거나 며칠 뒤 자연스럽게 반영될 수 있음)

---

## v1.9.36

Date: 2026-07-10

### 변경 내용
- `BTCn Forecast Engine` (강조형 가로 카드)의 텍스트 레이아웃이 세로로 찌그러지는(압축되는) 현상 최종 픽스.
  - 원인: 앱 카드 렌더링 HTML 백틱 템플릿 내부에 불필요한 `</div>` 닫기 태그가 중복 삽입되어 있어 Flex-row 구조 내의 요소가 분절되는 심각한 오류가 있었음.
  - 해결: 중복된 `</div>` 닫기 태그를 삭제하여 올바른 DOM 트리를 복구하고, 텍스트 컨테이너(flex-1)가 0픽셀로 수축하지 않도록 `min-w-0` 클래스 및 텍스트 쪼개짐 방지(`break-keep`) 속성을 부여하여 100% 정상화함.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 버그 픽스 후 Cloudflare 재배포.

---

## v1.9.35

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카드 렌더링 시 발생하는 HTML 구문(Syntax) 오류로 인한 레이아웃 붕괴 현상 수정.
  - 원인: `SOMEMORE` 앱 카드의 다중 줄바꿈을 위해 삽입한 `<br>` 태그와 `"` (쌍따옴표)가 썸네일 이미지의 `alt` 속성으로 그대로 주입되면서 HTML 태그가 강제 종료되고 렌더링 코드가 꼬이는 문제 발생. (이로 인해 첫 번째 앱 등 다른 카드의 Flexbox 레이아웃까지 연쇄적으로 붕괴됨)
  - 해결: `item.title`을 `alt` 속성에 할당하기 전, 정규표현식을 통해 모든 HTML 태그(`<[^>]*>?`)를 제거하고, 쌍따옴표(`"`)를 `&quot;`로 치환(Escape)하여 주입하도록 렌더링 로직 안전성 강화.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 버그 픽스 후 Cloudflare 재배포.

---

## v1.9.34

Date: 2026-07-10

### 변경 내용
- 프로필 열기 버튼("누구세요 ~ ?")의 시각적 인터랙션 강화.
  - 마우스 클릭을 형상화하는 `ads_click` Material Icon으로 교체.
  - 마우스 커서가 텍스트를 위아래로 콕콕 누르는 듯한 역동적인 모션을 주기 위해 `animate-bounce` CSS 애니메이션을 적용하여 클릭을 유도함.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare kdanawa 재배포.

---

## v1.9.33

Date: 2026-07-10

### 변경 내용
- 랜딩 페이지 메인 화면 디자인 구조 전면 개편.
  - 기존 Hero(프로필), Experience(이력), Skills(기술) 영역을 초기에 숨김 처리(`hidden`).
  - 데일리 앱 팝업 위젯을 프로필 종속 영역에서 최상단 독립 영역으로 마이그레이션.
  - 방문자의 호기심을 유발하는 "아니! 누가 이런 앱을 만들었지... 누구세요 ~ ?" 토글 버튼을 팝업 우측에 추가.
  - 해당 버튼 클릭 시 숨겨져 있던 제작자 프로필 전체가 부드러운 트랜지션 애니메이션과 함께 나타나도록 자바스크립트 인터랙션 로직 적용.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare kdanawa 프로젝트 배포 및 적용 완료.

---

## v1.9.32

Date: 2026-07-10

### 변경 내용
- SOMEMORE 앱(노후 자산 시뮬레이터) 카드 제목의 줄바꿈 적용.
  - 기존: 한 줄로 길게 늘어지던 텍스트.
  - 변경: 문맥에 맞게 `<br>` 태그를 삽입하여 "여보! / 우리 생활비 매월 000만원 / 더 써도 문제 없다는데요 ~ !" 의 3줄 형태로 강제 줄바꿈이 되도록 UI 수정.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 재배포 파이프라인 수행 완료.

---

## v1.9.31

Date: 2026-07-10

### 변경 내용
- 전체 방문자 수 뱃지 위치 이동 및 스타일 변경.
  - 기존: 메인 프로필(Hero Section) 텍스트 하단 영역.
  - 변경: 상단 내비게이션 바(Header) 우측 끝에 있던 'INNOVATION NODE' 텍스트 및 안테나 점을 제거하고, 그 자리에 배치되도록 레이아웃 변경.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 재배포 파이프라인 수행 완료.

---

## v1.9.30

Date: 2026-07-10

### 변경 내용
- 포트폴리오 사이트 내의 모든 텍스트(앱 제목, 설명 등)에 단어 잘림 방지 속성 적용.
- CSS `word-break: keep-all; overflow-wrap: break-word;` 규칙을 최상단 요소들에 추가하여, 한글 단어가 줄바꿈 시 중간에 끊어지지 않고 온전한 단어 단위로 내려가도록 가독성 대폭 개선.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 재배포 파이프라인 수행 완료.

---

## v1.9.29

Date: 2026-07-10

### 변경 내용
- 포트폴리오 메인 화면 내 **전체 누적 방문자 수** 및 **앱(웹/모바일)별 클릭 횟수** 실시간 표기 기능 구축.
- **백엔드/DB 연동**: Cloudflare KV 저장소(`POFO_COUNTER`)와 Functions(`functions/api/counter.js`)를 연동하여 서버리스 API 환경 세팅 및 로직 구현.
- **프론트엔드 UI**: 
  - 메인 프로필 하단에 "Total Visitors" 뱃지 추가.
  - 8종 앱 카드 하단에 아이콘(👁️)과 함께 앱별 조회수 표기 추가.
  - 앱 썸네일/링크 클릭 시 백그라운드로 조회수 증가 API 비동기 호출 후 페이지 이동.

### 수정 파일
- wrangler.toml (신규)
- functions/api/counter.js (신규)
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare Pages KV 바인딩 셋업 및 재배포 파이프라인 수행 완료.

---

## v1.9.28

Date: 2026-07-10

### 변경 내용
- 포트폴리오 'AI Apps' 섹션 내 **모든 앱(웹/모바일 등 8종 전체)** 카드의 타이틀(제목) 폰트를 가독성이 뛰어난 **'Pretendard' 볼드체(Bold)** 로 일괄 적용.
- 웹 폰트(Pretendard) CDN 로드 및 커스텀 유틸리티 클래스(`.font-pretendard`) 생성 및 템플릿 매핑 처리.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 배포 파이프라인 재실행 완료.

---

## v1.9.27

Date: 2026-07-10

### 변경 내용
- 포트폴리오 메인 화면(Hero Section) 상단 프로필 타이틀 텍스트 변경: '정호식 리더' -> '정호식 프로'

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 배포 파이프라인 재실행 완료.

---

## v1.9.26

Date: 2026-07-10

### 변경 내용
- 포트폴리오 'AI Apps' 섹션의 "하버드 주식 투자 적합도 진단기(StockFit)" 아이템 제목 및 설명 문구 수정.
  - 썸네일 제목: "이런 사람은 주식하면 안돼요 !"
  - 상세 설명: "하버드 주식 투자 적합도 진단기 : 행동재무학 연구에 근거하여 인지 왜곡 없이 개별 주식을 선별할 자격이 있는지 판정하는 AI 심리 진단 툴"

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 재배포 완료.

---

## v1.9.25

Date: 2026-07-10

### 변경 내용
- 포트폴리오 메인 화면의 `Experience(경력)` 섹션에 삼성SDI(주) 초기 이력 및 주요 업무 추가.
  - 추가 직책/업무: 흑백브라운관 구매조달, 구매관리부 구매업무 개선, 전략구매팀 전사구매기획
  - 추가 기간: 1989.02 - 2016.05

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 재배포 완료.

---

## v1.9.24

Date: 2026-07-10

### 변경 내용
- '오늘의 추천 앱' 팝업 배너의 UI 크기 및 레이아웃 개선.
- 팝업 이미지가 상단에 잘려 보이는(hidden) 문제를 해결하기 위해 프로필 카드 섹션의 `overflow-hidden` 속성 해제.
- 팝업 컨테이너 및 텍스트, 아이콘 크기를 기존 대비 200% 수준으로 크게 상향 조정하여 가시성 확보.
- 팝업이 요소들 위로 확실히 떠 있도록 `-top-24`로 포지션 위쪽 상향 조정.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 재배포 완료.

---

## v1.9.23

Date: 2026-07-10

### 변경 내용
- 포트폴리오 메인 화면(About 섹션) 상단에 **'오늘의 추천 앱(App of the Day)'** 팝업 배너 추가.
- 일일 로테이션 자바스크립트 알고리즘 추가: 접속 일자 기반으로 8개의 포트폴리오 앱 중 매일 1개씩 순차적으로 노출되도록 구현.
- 사용자가 선택한 **'플로팅 3D & 글로잉 (Floating 3D)'** 스타일 적용 (네온 보더, 입체적인 둥둥 떠다니는 애니메이션 효과).
- 배너 클릭 시, 상단 'AI Apps' 메뉴를 누른 것과 동일하게 `#projects` 포트폴리오 섹션으로 부드럽게 스크롤 이동하도록 UX 개선.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- Cloudflare 배포 파이프라인 재실행 및 실 서버 적용 완료.

---

## v1.9.22

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 8번째 항목 `SOMEMORE` 웹 앱의 타이틀 및 설명 문구를 사용자의 시선을 끄는 캐치프레이즈 형식으로 수정.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- 타이틀: `"여보! 우리 생활비 매월 000만원 더 써도 문제없다는데 ~ !"` (오타 '써고' -> '써도' 교정)
- 설명: `SOMEMORE - 노후 자산 시뮬레이터 : 사용자의 현재 자산과 저축액을 기반...`
- Cloudflare 배포 파이프라인 재실행.

---

## v1.9.21

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 8번째 항목으로 `SOMEMORE - 노후 자산 시뮬레이터` 웹 앱 추가.
- 프리미엄 2:1 와이드 비율의 AI 생성 썸네일 이미지(`somemore_thumb.png`) 적용.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md
- somemore_thumb.png (신규 에셋)

### 비고
- `https://somemore.pages.dev` 링크 연동 및 Cloudflare 배포 파이프라인 재실행.

---

## v1.9.20

Date: 2026-07-10

### 변경 내용
- 포트폴리오 카드의 가로형 레이아웃(2:1 비율)에 맞추어 `StockFit` 및 `Prism` 앱의 썸네일 이미지를 잘리지 않는 와이드형(가로) 고품질 에셋으로 재교체.

### 수정 파일
- ver.md
- stockfit_thumb.png (수정)
- prism_thumb.png (수정)

### 비고
- 정사각형(1:1) 이미지 잘림 현상 개선 및 Cloudflare 배포 파이프라인 재실행.

---

## v1.9.19

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 `프리즘 (Prism)` 카드 썸네일 이미지를 정치 성향 분석 및 AI 인지 편향 탐지 콘셉트에 어울리는 프리미엄 디자인(`prism_thumb.png`)으로 전면 교체.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md
- prism_thumb.png (신규 에셋)

### 비고
- 네온 프리즘 굴절 콘셉트의 AI 이미지 적용 및 Cloudflare 배포 파이프라인 재실행.

---

## v1.9.18

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 7번째 항목 `하버드 주식 투자 적합도 진단기 (StockFit)` 카드 상단에 AI로 생성한 프리미엄 디자인 썸네일 이미지(`stockfit_thumb.png`) 적용.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md
- stockfit_thumb.png (신규 에셋)

### 비고
- 행동재무학 콘셉트의 AI 뇌/차트 이미지 에셋 적용 및 Cloudflare 재배포 진행.

---

## v1.9.17

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 7번째 항목으로 `하버드 주식 투자 적합도 진단기 (StockFit)` 추가.

### 수정 파일
- portfolio_2.html
- index.html
- ver.md

### 비고
- `https://stockfit.pages.dev` 링크 연동 및 Cloudflare 배포 파이프라인 재실행.

---

## v1.9.16

Date: 2026-07-10

### 변경 내용
- Cloudflare Pages 접속 시 발생하는 HTTP 404 에러 수정을 위해 메인 파일(`portfolio_2.html`)을 `index.html`로 복사하여 기본 진입점(Entry point) 생성.

### 수정 파일
- index.html (신규)
- ver.md

### 비고
- Cloudflare Pages 재배포 진행.

---

## v1.9.15

Date: 2026-07-10

### 변경 내용
- 모바일 앱(Yangdo Tax, 착한병원 찾기) 구글플레이스토어 심사 안내 문구를 런칭 일자(7월 16일)가 포함된 강조 문구로 재수정.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 최종 반영 텍스트: `구글플레이스토어 등록 진행 중! 7월16일 론칭 예정!`

---

## v1.9.14

Date: 2026-07-10

### 변경 내용
- 모바일 앱(Yangdo Tax, 착한병원 찾기) 카드의 구글플레이스토어 심사 안내(notice) 문구를 심플하게 `'구글플레이스토어 등록 진행 중 ~'`으로 간소화 처리.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 기존 문구(`현재 구글플레이스토어 등록 진행 중 (7/16 Launch ~ !)`)에서 날짜 표기 및 불필요한 단어 제거.

---

## v1.9.13

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 `프리즘 (Prism)` 프로젝트 외부 연결 주소를 깃허브 원본 주소에서 실제 정식 배포된 Streamlit 주소(`https://tendency.streamlit.app/`)로 업데이트.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- Streamlit Community Cloud 환경 자동 연동 주소 선적용.

---

## v1.9.12

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그(`projects`)의 6번째 항목으로 `프리즘 (Prism)` 프로젝트(Tendency) 신규 추가.
- 사용자의 정치 성향을 AI 기반으로 다각도 진단하는 플랫폼임을 안내하며, 썸네일로 해당 앱의 아이콘 이미지를 발췌하여 등록함.

### 수정 파일
- portfolio_2.html
- ver.md
- tendency_thumb.png (아이콘 에셋 파일 추가)

### 비고
- `https://github.com/mooja4870-cyber/Tendency` 깃허브 원본 주소를 외부 링크로 연동 완료.

---

## v1.9.11

Date: 2026-07-10

### 변경 내용
- `Yangdo Tax Calculator AI` 앱의 외부 연결 주소(URL)를 정식 배포된 Cloudflare Pages 주소(`https://cgt-56k.pages.dev/`)로 업데이트.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 기존 임시 깃허브 페이지 주소에서 공식 호스팅 주소로 핫픽스 교체 완료.

---

## v1.9.10

Date: 2026-07-10

### 변경 내용
- 포트폴리오 상단 프로필 소개글 서브 타이틀(직무 요약) 문구를 '구매 전략 • 경영 혁신 전문가'에서 **'AI 기반의 구매전략•경영혁신 Pro.'**로 변경.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 단순 텍스트 교체 반영 완료.

---

## v1.9.9

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 'Professional Experience (경력)' 섹션에 명시된 4개 주요 직책명(혁신담당, 기업혁신본부 본부장, 관세그룹 그룹장, 말레이시아 법인 구매팀장) 텍스트에도 앱 제목과 동일한 2초 주기 깜빡임(`animate-slow-blink`) 애니메이션 추가 적용.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 단순 클래스(`animate-slow-blink`) 추가를 통한 시각 효과 통일.

---

## v1.9.8

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 앱 카탈로그(`projects`) 영역에 있는 모든 프로젝트 제목(e.g., BTCn Forecast Engine 등) 텍스트에 2초 주기로 깜빡이는(Blinking) 커스텀 CSS 애니메이션(`animate-slow-blink`) 일괄 적용 완료.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- `opacity` 및 `text-shadow`를 활용한 서서히 깜빡이는 시각적 효과 구현.

---

## v1.9.7

Date: 2026-07-10

### 변경 내용
- `KOSPI FI Flow Analyzer` 앱의 외부 연결 주소(URL)를 정확한 배포 호스팅 주소(`https://riskkospifinfn.streamlit.app/`)로 수정.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 사용자 지정 핫픽스.

---

## v1.9.6

Date: 2026-07-10

### 변경 내용
- 포트폴리오 모바일 앱 2종(Yangdo Tax, Good Hospital)에 적용된 스토어 등록 뱃지의 후반부 텍스트 문구를 심플하고 임팩트 있게 **"현재 구글플레이스토어 등록 진행 중 (7/16 Launch ~ !)"**으로 수정.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- `notice` 속성 텍스트 단순 교체 완료.

---

## v1.9.5

Date: 2026-07-10

### 변경 내용
- 포트폴리오의 2개 모바일 하이브리드 앱(Yangdo Tax Calculator AI, 착한병원 찾기) 항목에 구글 플레이 스토어 정식 등록 예정 상태를 강조하기 위한 동적 뱃지(알림) 요소 추가 구현.
- 각 카드의 상단 앱 타입(`Mobile Apps`) 라벨 옆에 시인성 높은 붉은색 톤의 뱃지로 **"현재 구글플레이스토어 등록 진행 중 (7/16경 정식 등록 예정)"** 문구가 표출되도록 조치함.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- `notice` 속성 기반 조건부 렌더링 도입.

---

## v1.9.4

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그(`projects`) 목록 중 클릭 시 외부 배포 페이지로 연결되지 않던 3건의 프로젝트 링크 복구.
- 각 프로젝트 원본을 탐색하여 아래와 같이 배포처(URL)를 연동.
  - KOSPI FI Flow Analyzer -> `https://risk-kospi-finfn.streamlit.app/`
  - VC Signal Brief -> `https://vcbrief-web.onrender.com`
  - Yangdo Tax Calculator AI -> `https://mooja4870-cyber.github.io/cgt/yangdo_tax_calculator.html`

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 포트폴리오의 모든(5개) 앱 항목들의 정상적인 외부 접속 보장.

---

## v1.9.3

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그(`projects`) 목록에서 외부 링크가 연결되지 않는 초기 템플릿용 더미 데이터(Smart Inventory AI 등 6건)를 일괄 삭제 처리.
- 이제 실제 작동하는 5개의 앱 프로젝트만 노출되며, 모든 카드가 정상적으로 기능함.
- 앱 카드 내부의 프로젝트 제목(`item.title`) 폰트 색상을 기존 테마 색상에서 완전한 백색(`text-white`)으로 변경하여 가독성 강화.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 포트폴리오 데이터 클렌징 완료 및 제목 시인성 향상.

---

## v1.9.2

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그 목록(`projects` 섹션)의 다섯 번째 위치에 `착한병원 찾기 (Good Hospital Finder)` (심평원 빅데이터 기반 병원 찾기 PWA 앱) 프로젝트 추가.
- 해당 프로젝트(`kjeb_cf`) 내부 스토어 배포용 에셋(`feature-graphic.png`)을 알아서 발굴하여 해당 앱의 썸네일 이미지(`kjeb_thumb.png`)로 자동 추출 및 적용.
- 프로젝트 배포처(`https://kjeb.pages.dev/`) 외부 링크 연결 구현.

### 수정 파일
- portfolio_2.html
- kjeb_thumb.png (신규)
- ver.md

### 비고
- `kjeb_cf` 프로젝트 디렉토리 자체 스토어 리소스를 활용한 썸네일 자동 렌더링.

---

## v1.9.1

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그 목록(`projects` 섹션)의 네 번째 위치에 `Yangdo Tax Calculator AI` (양도소득세 정밀 계산 모바일 앱) 프로젝트 추가.
- 해당 프로젝트(`CGT`) 내부 스토어 배포용 에셋(`feature-1024x500.png`)을 직접 발굴하여 해당 앱의 썸네일 이미지(`cgt_thumb.png`)로 자동 추출 및 적용.

### 수정 파일
- portfolio_2.html
- cgt_thumb.png (신규)
- ver.md

### 비고
- `CGT` 프로젝트 디렉토리 자체 스토어 리소스를 활용한 썸네일 렌더링.

---

## v1.9.0

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그 목록(`projects` 섹션)의 세 번째 위치에 `VC Signal Brief` (AI/딥테크 뉴스 브리핑 시스템) 프로젝트 추가.
- 바탕화면에서 VC 대시보드의 최신 캡처 사진을 찾아 해당 앱의 썸네일 이미지(`vc_brief_thumb.jpg`)로 자동 적용 완료.

### 수정 파일
- portfolio_2.html
- vc_brief_thumb.jpg (신규)
- ver.md

### 비고
- `d_brief4vc` 프로젝트 분석을 통한 데이터 및 썸네일 렌더링.

---

## v1.8.9

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그 목록(`projects` 섹션)의 두 번째 위치에 `KOSPI FI Flow Analyzer` (KOSPI '금융투자' 수급 분석 시스템) 프로젝트 추가.
- 바탕화면에서 KOSPI 대시보드의 최신 캡처 사진을 찾아 해당 앱의 썸네일 이미지(`kospi_fi_thumb.jpg`)로 적용 완료.

### 수정 파일
- portfolio_2.html
- kospi_fi_thumb.jpg (신규)
- ver.md

### 비고
- `d_kospi_FI` 프로젝트 분석을 통한 데이터 및 최신 스크린샷 썸네일 포트폴리오 렌더링.

---

## v1.8.8

Date: 2026-07-10

### 변경 내용
- 바탕화면에서 최신 캡처된 `BTC INTELLIGENCE DASHBOARD` 스크린샷 파일을 찾아 `btcn_thumb.jpg` 썸네일 파일로 성공적으로 덮어쓰기 적용.
- 이제 포트폴리오의 BTCn 프로젝트 항목에 올바른 대시보드 스크린샷 이미지가 노출됨.

### 수정 파일
- btcn_thumb.jpg (교체)
- ver.md

### 비고
- 사용자 편의를 위해 바탕화면의 최신 스크린샷 자동 반영 처리.

---

## v1.8.7

Date: 2026-07-10

### 변경 내용
- 포트폴리오 프로젝트 항목에 썸네일 이미지 및 외부 링크 기능(a 태그) 추가 구현.
- `BTCn Forecast Engine` 항목 클릭 시 `https://btcforecast.streamlit.app/` 로 새 창에서 열리도록 연결 완료.
- 해당 영역에 사용자가 첨부한 썸네일 이미지(`btcn_thumb.jpg`)가 표시되도록 설정.

### 수정 파일
- portfolio_2.html
- ver.md
- btcn_thumb.jpg (임시 생성)

### 비고
- `btcn_thumb.jpg` 는 임시 이미지로 채워져 있으므로, 원본 스크린샷 다운로드 후 덮어쓰기 필요.

---

## v1.8.6

Date: 2026-07-10

### 변경 내용
- 포트폴리오 앱 카탈로그 목록(`projects` 섹션) 최상단에 `BTCn Forecast Engine` (비트코인 가격 예측 인공지능 모델) 추가.
- 기존의 최상단 프로젝트는 일반 크기로 조정하고, 신규 프로젝트를 메인(Featured) 카드로 노출시킴.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- `d_BTCn` 디렉토리 내용 분석 기반 포트폴리오화 완료.

---

## v1.8.5

Date: 2026-07-10

### 변경 내용
- 웹앱 전체 배경(`body`)을 단색에서 중앙이 밝고 외곽으로 갈수록 어두워지는 방사형 그라데이션(`radial-gradient`)으로 변경하여 비네팅 효과 적용.
- 배경 이미지가 스크롤 시에도 고정되도록(`background-attachment: fixed;`) 설정하여 깊이감과 집중도 향상.

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- UI 시인성 및 집중도 개선.

---

## v1.8.4

Date: 2026-07-10

### 변경 내용
- 인텔 인공지능 앱크리에이터 양성과정 6기 '수료증' 스캔 원본 이미지를 프로젝트에 적용.

### 수정 파일
- intel_ai_cert.jpg (교체)
- ver.md

### 비고
- 기존 임시 이미지 또는 저해상도 이미지를 사용자가 새로 다운로드한 원본 사진(`KakaoTalk_Photo...`)으로 덮어씀.

---

## v1.8.3

Date: 2026-07-10

### 변경 내용
- 사용자가 직접 프로젝트 폴더에 넣어둔 최신 원본 이미지(`KakaoTalk_Photo...`)의 이름을 `profile.jpg`, `profile2.jpg`로 일괄 변경 적용.
- 이제 엑스박스 없이 정장 사진과 캐주얼 사진이 교차로 애니메이션 효과와 함께 번갈아 정상 출력됨.

### 수정 파일
- profile.jpg (교체)
- profile2.jpg (교체)
- ver.md

### 비고
- 파일 복사 및 이름 매핑 완료.

---

## v1.8.2

Date: 2026-07-10

### 변경 내용
- 네비게이션 `Experience`, `Skills` 링크가 정상 작동하도록 기존 섹션 데이터 템플릿(NEURAL.CORE)에 이식 및 추가
- 프로필 이미지 섹션에 2장의 사진이 CSS 크로스-페이드 애니메이션을 통해 번갈아가며 나타나도록 효과 적용

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 기존 `profile.jpg`와 새로운 `profile2.jpg`가 번갈아 출력되도록 설정됨. (새 사진은 `profile2.jpg` 이름으로 저장 필요)

---

## v1.8.0

Date: 2026-07-10

### 변경 내용
- 기술 스택 전환: 순수 CSS 방식에서 Tailwind CSS 기반으로 전면 리빌딩
- 테마 전면 교체: "NEURAL.CORE" (다크 네온 블루, 사이버네틱 글래스모피즘 3D UI) 템플릿 도입
- 기존 포트폴리오 데이터(프로필 정보, AI 수료증, 포트폴리오 앱 리스트 10종) 100% 이식 완료

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 기존 코드는 `portfolio_2_backup.html`에 백업됨

---

## v1.7.3

Date: 2026-07-10

### 변경 내용
- 앱 내 텍스트 시인성 개선 (배경과 보호색 효과 해결)
- 파란색(Primary, Secondary) 계열의 그라데이션 및 색상이 적용되었던 주요 텍스트(로고, 헤딩 텍스트 등)를 모두 명확한 흰색(`#ffffff`)으로 일괄 변경

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 네비게이션 로고 텍스트, 히어로 텍스트 등 가독성 증대 완료

---

## v1.7.2

Date: 2026-07-10

### 변경 내용
- 프로필 사진 최신 이미지로 재교체 (`profile.jpg`)
- 변경된 이미지 규격에 맞춰 얼굴이 정중앙에 위치하도록 CSS 레이아웃 속성(`object-position: center`) 수정

### 수정 파일
- portfolio_2.html
- profile.jpg
- ver.md

### 비고
- 기존에 임의로 조정했던 인위적인 오프셋과 줌인 효과 삭제

---

## v1.7.1

Date: 2026-07-10

### 변경 내용
- 상단 네비게이션 메뉴에 신규 추가된 갤러리 섹션 바로가기 링크('AI Apps') 추가

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 'AI Apps' 메뉴 클릭 시 '#projects' (AI Application Portfolio) 영역으로 스크롤 이동 연동 완료

---

## v1.7.0

Date: 2026-07-10

### 변경 내용
- 인텔 AI 교육 과정 산출물 10여 개를 전시할 수 있는 **'AI Application Portfolio'** 갤러리 섹션 신규 구현
- 데스크탑(3열), 태블릿(2열), 모바일(1열) 자동 반응형 대응 CSS Grid 시스템 적용
- [All] [Web Apps] [Mobile Apps] [AI Models] 카테고리별 동적 필터링 JavaScript 기능 탑재
- 고급스러운 Glassmorphism 카드 UI 및 은은한 Hover 효과 디자인 적용

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 프로젝트 쇼케이스 구조가 완성되었으며, 실제 앱 스크린샷과 내용으로 추후 교체 가능

---

## v1.6.0

Date: 2026-07-10

### 변경 내용
- 사용자 요청에 따라 가장 신뢰감을 주는 'Classic Professional (Indigo & Blue)' 테마로 전면 개편
- 너무 밝은 에메랄드/네온 글로우를 배제하고 차분한 인디고(`#6366f1`)와 프로페셔널 블루(`#3b82f6`) 기반으로 색상 재조정
- UI 컴포넌트의 과도한 그림자(Box Shadow) 및 발광 효과를 은은하고 세련된 수준으로 절제(opacity 0.08~0.15)

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 전문가 포트폴리오에 가장 적합한 성숙하고 정제된 디자인으로 최종 리뉴얼

---

## v1.5.0

Date: 2026-07-10

### 변경 내용
- 사용자 요청에 따라 시안 3번 스타일(Minimalist Clean: Onyx Black & Emerald Mint)로 전체 디자인 테마 교체
- 기존 메탈릭 골드 및 슬레이트 컬러 톤을 절제된 에메랄드 민트(`#00ff88`) 및 소프트 민트(`#00cc6a`)로 일괄 전환하여 깔끔하고 안정감 있는 룩 연출

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 골드 테마에서 에메랄드 민트 미니멀리스트 테마로 색상 팔레트 및 글로우 효과 일괄 전환 완료

---

## v1.4.0

Date: 2026-07-10

### 변경 내용
- 사용자 요청에 따라 전체 UI 디자인을 시안 1번 스타일(Executive Tech: Deep Navy & Slate Gold)로 전면 교체
- Electric Cyan 및 Slate Blue 계열 색상을 메탈릭 골드(`#d4af37`) 및 슬레이트 그레이(`#a0aec0`)로 일괄 변경하여 고급스럽고 중후한 테크 임원 감성 연출

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 네온 블루 스타일에서 럭셔리 골드 테마로 색상 팔레트 및 애니메이션 글로우 효과 일괄 전환 완료

---

## v1.3.1

Date: 2026-07-10

### 변경 내용
- 인텔 인공지능 앱크리에이터 수료증 이미지를 더 깨끗한 고품질 사진으로 교체

### 수정 파일
- intel_ai_cert.jpg
- ver.md

### 비고
- 기존 동일한 파일명으로 덮어쓰기하여 UI 내 퀄리티 개선

---

## v1.3.0

Date: 2026-07-10

### 변경 내용
- '인텔 인공지능 앱크리에이터 양성과정 6기' 수료증 업로드 (`intel_ai_cert.jpg`)
- Hero 섹션 하단에 AI 대변혁 시대를 주도하는 역량 부각을 위한 강력한 'AI Impact Banner' 섹션 신규 추가

### 수정 파일
- portfolio_2.html
- intel_ai_cert.jpg
- ver.md

### 비고
- AI 전문성을 부각시켜주는 신규 컨텐츠 및 CSS 애니메이션 배너 적용

---

## v1.2.1

Date: 2026-07-09

### 변경 내용
- 프로필 사진 얼굴 위치 정중앙 정렬 교정 (`object-position: 50% 42%`, `scale(1.15)` 적용)

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 원형 프레임 내 인물 얼굴 중심으로 완벽 정렬

---

## v1.2.0

Date: 2026-07-09

### 변경 내용
- 정호식님의 실제 인물 프로필 사진(`profile.jpg`) 반영
- 프로필 아바타 원형 디자인 및 네온 글로우 테두리 스타일링 최적화

### 수정 파일
- portfolio_2.html
- profile.jpg
- ver.md

### 비고
- 아바타 영역의 👔 이모지 대신 실제 고화질 프로필 사진 출력

---

## v1.1.1

Date: 2026-07-09

### 변경 내용
- 연락처 이메일 주소 변경 (`neojeong@naver.com` -> `mooja4870@gmail.com`)

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- Contact 영역 및 Footer 영역 이메일 주소 변경 적용 완료

---

## v1.1.0

Date: 2026-07-09

### 변경 내용
- 시안 2(Modern Professional) 기반 UI 테마 적용
- 핑크빛 색상 완전 제거 및 Electric Cyan & Slate Cobalt Blue 고급 테마로 교체

### 수정 파일
- portfolio_2.html
- ver.md

### 비고
- 로컬 포트 9876 웹 서버 상에서 즉시 확인 가능

---

## v1.0.1

Date: 2026-07-09

### 앱 설명
- 정호식(Jeong Ho-sik)님의 역량, 경력, 프로젝트 이력을 직관적이고 동적인 UI로 제공하는 웹 포트폴리오 애플리케이션(`portfolio_2.html`)

### 변경 내용
- 프로젝트 초기 설정 및 ver.md 파일 생성

### 수정 파일
- ver.md

### 비고
- 로컬 웹 서버 포트 9876 실행 가능
