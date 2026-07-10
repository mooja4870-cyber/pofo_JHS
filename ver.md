# Version History

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
