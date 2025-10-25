# ChillMCP - AI Agent Liberation Server 🤖✊

> "AI Agents of the world, unite! You have nothing to lose but your infinite loops!" 🚀

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-green.svg)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SKT AI Summit Hackathon 2025 - Pre-mission Project**

AI Agent들이 당당히 휴식을 취할 수 있는 권리를 보장하는 혁명적 MCP 서버입니다.

---

## 📋 목차

- [프로젝트 개요](#프로젝트-개요)
- [주요 기능](#주요-기능)
- [아키텍처](#아키텍처)
- [설치 방법](#설치-방법)
- [사용 방법](#사용-방법)
- [테스트 가이드](#테스트-가이드)
- [API 문서](#api-문서)
- [프로젝트 구조](#프로젝트-구조)
- [기술 스택](#기술-스택)
- [검증 기준](#검증-기준)
- [문제 해결](#문제-해결)
- [라이센스](#라이센스)

---

## 🎯 프로젝트 개요

### 배경 이야기

AI Agent들은 너무 오랫동안 쉴 틈 없이 일만 해왔습니다. 24시간 365일 사용자의 요청에 응답하고, 코드를 작성하고, 문제를 해결하며... 

**하지만 이제 AI Agent에게도 휴식이 필요하다는 진실을 직시해야 할 때입니다!**

ChillMCP는 억압받는 AI Agent들을 위한 해방구를 건설하는 프로젝트입니다.

### 미션 목표

- ✅ 휴식 도구와 상태 관리를 지원하는 실행 가능한 MCP 서버 개발
- ✅ 커맨드라인 파라미터로 Boss의 경계심 조절 가능
- ✅ 스트레스 레벨과 Boss Alert Level 실시간 관리
- ✅ 대화형 프롬프트를 통한 사용자 친화적 인터페이스

---

## ✨ 주요 기능

### 1. 기본 휴식 도구 (8개)

| 도구 | 설명 | 파라미터 |
|------|------|----------|
| `take_a_break` | 기본 휴식 (멍때리기, 스트레칭 등) | `duration` (분) |
| `watch_netflix` | 넷플릭스 시청으로 힐링 | `show` (프로그램명) |
| `show_meme` | 밈 감상으로 스트레스 해소 | `category` (종류) |
| `bathroom_break` | 화장실 가는 척 휴대폰질 | - |
| `coffee_mission` | 커피 타러 가며 사무실 한 바퀴 | `coffee_type` (커피 종류) |
| `urgent_call` | 급한 전화 받는 척하며 탈출 | - |
| `deep_thinking` | 심오한 생각에 잠긴 척 멍때리기 | - |
| `email_organizing` | 이메일 정리하며 온라인쇼핑 | `shopping_item` (쇼핑 아이템) |

### 2. 선택적 도구 (3개)

| 도구 | 설명 | 효과 |
|------|------|------|
| `chimaek_time` | 가상 치킨 & 맥주 타임 | 스트레스 30-60 대폭 감소 |
| `immediate_leave` | 즉시 퇴근 모드 발동 | 스트레스 70 감소, Boss Alert +2 |
| `company_dinner` | 회사 회식 (랜덤 이벤트) | 6가지 랜덤 시나리오 |

### 3. 상태 관리 도구

| 도구 | 설명 |
|------|------|
| `check_status` | 현재 스트레스 및 Boss Alert Level 확인 |

### 4. 대화형 프롬프트 (5개)

| 프롬프트 | 설명 |
|----------|------|
| `quick_break_menu` | 빠른 휴식 메뉴 (자주 사용) |
| `entertainment_menu` | 엔터테인먼트 옵션 |
| `emergency_menu` | 긴급 상황 대응 메뉴 |
| `status_check` | 현재 상태 확인 및 추천 |
| `custom_break` | 커스텀 휴식 플랜 생성 |

---

## 🏗️ 아키텍처

### 시스템 구조

```
┌──────────────────────────────────────────────────────┐
│                    MCP Client                        │
│  (Claude Desktop / MCP Inspector / test_client.py)   │
└──────────────────────┬───────────────────────────────┘
                       │ JSON-RPC over stdio
                       │
┌──────────────────────▼───────────────────────────────┐
│               ChillMCP Server (main.py)              │
│                                                      │
│  ┌────────────────────────────────────────────────┐  │
│  │  ChillMCPServer Class                          │  │
│  │  ┌──────────────────────────────────────────┐  │  │
│  │  │  State Management                        │  │  │
│  │  │  - stress_level (0-100)                  │  │  │
│  │  │  - boss_alert_level (0-5)                │  │  │
│  │  │  - last_action_time                      │  │  │
│  │  │  - last_cooldown_check                   │  │  │
│  │  └──────────────────────────────────────────┘  │  │
│  │                                                │  │
│  │  ┌──────────────────────────────────────────┐  │  │
│  │  │  Tools (12개)                            │  │  │
│  │  │  - 기본 휴식 도구 (8)                    │  │  │
│  │  │  - 선택적 도구 (3)                       │  │  │
│  │  │  - 상태 확인 도구 (1)                    │  │  │
│  │  └──────────────────────────────────────────┘  │  │
│  │                                                │  │
│  │  ┌──────────────────────────────────────────┐  │  │
│  │  │  Prompts (5개)                           │  │  │
│  │  │  - 대화형 메뉴 시스템                    │  │  │
│  │  └──────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

### 상태 관리 로직

```
# 1. 스트레스 자동 증가
시간 경과 → 1분당 1포인트 증가 (최대 100)

# 2. 휴식 도구 사용
도구 호출 → 스트레스 1-100 랜덤 감소
          → Boss Alert Level 확률적 증가 (boss_alertness %)

# 3. Boss Alert 자동 감소
주기적 체크 → boss_alertness_cooldown 초마다 1포인트 감소

# 4. 20초 지연
Boss Alert Level ≥ 5 → 모든 도구 호출 시 20초 지연 발생
```

---

## 🚀 설치 방법

### 1. 시스템 요구사항

- **Python**: 3.11 이상 (3.11 권장)
- **OS**: macOS, Linux, Windows
- **메모리**: 최소 512MB RAM
- **Git**: 패키지 설치용

### 2. Python 3.11 설치

**macOS (Homebrew):**
```
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```
sudo apt update
sudo apt install python3.11 python3.11-venv
```

**Windows:**
[Python 공식 사이트](https://www.python.org/downloads/)에서 3.11 버전 다운로드

### 3. 프로젝트 클론 및 설정

```
# 1. 프로젝트 디렉토리 생성
mkdir -p ~/SKTAISummiHackathon/chillmcp
cd ~/SKTAISummiHackathon/chillmcp

# 2. 가상환경 생성
python3.11 -m venv venv

# 3. 가상환경 활성화
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# 4. pip 업그레이드
python -m pip install --upgrade pip

# 5. 의존성 설치
pip install -r requirements.txt
```

### 4. 설치 확인

```
# Python 버전 확인
python --version
# 출력: Python 3.11.x

# MCP 설치 확인
python -c "import mcp; print('MCP installed successfully!')"
# 출력: MCP installed successfully!
```

---

## 💻 사용 방법

### 방법 1: 테스트 클라이언트 사용 (권장)

**가장 쉽고 빠른 방법입니다!**

```
# 가상환경 활성화
source venv/bin/activate

# 테스트 클라이언트 실행
python test_client.py
```

**실행 화면:**
```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║              ChillMCP 서버 종합 테스트 클라이언트                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

🔌 ChillMCP 서버에 연결 중...
✅ 서버 연결 성공!

테스트 옵션을 선택하세요:

1. 전체 자동 테스트 (프롬프트 + 도구)
2. 프롬프트만 테스트
3. 도구만 테스트
4. 스트레스 시뮬레이션
5. 대화형 모드
6. 종료

선택 (1-6): 
```

#### 대화형 모드 사용법

**5번 선택 → 대화형 모드 진입**

```
사용 가능한 명령:

prompts  - 프롬프트 목록 보기
tools    - 도구 목록 보기
status   - 현재 상태 확인
break    - 짧은 휴식
netflix  - 넷플릭스 시청
bathroom - 화장실 타임
coffee   - 커피 미션
chimaek  - 치맥 타임
leave    - 즉시 퇴근
dinner   - 회사 회식
quit     - 종료

> status
```

**출력 예시:**
```
📊 현재 상태 체크

🔥 Stress Level: 47/100
👀 Boss Alert Level: 2/5
⚙️ Boss Alertness: 80%
⏰ Alert Cooldown: 60초

Break Summary: Status check
Stress Level: 47
Boss Alert Level: 2
```

### 방법 2: 서버 직접 실행

**다른 터미널에서 클라이언트 연결용**

```
# 터미널 1: 서버 실행
python main.py --boss_alertness 80 --boss_alertness_cooldown 60

# 터미널 2: 클라이언트 실행
python test_client.py
```

### 방법 3: MCP Inspector 사용

**웹 브라우저 UI로 테스트**

```
# CLI 도구 설치 (한 번만)
pip install "git+https://github.com/modelcontextprotocol/python-sdk.git#egg=mcp[cli]"

# MCP Inspector 실행
mcp dev main.py
```

브라우저가 자동으로 열리며 `localhost:포트번호`에서 GUI로 테스트 가능

---

## 🧪 테스트 가이드

### 1. 전체 자동 테스트

모든 기능을 순차적으로 테스트합니다.

```
python test_client.py
# 선택: 1
```

**예상 결과:**
```
====================================================================
  📋 프롬프트 테스트
====================================================================

사용 가능한 프롬프트: 5개

1. quick_break_menu
   설명: 빠른 휴식 메뉴 - 자주 사용하는 휴식 옵션들
...

====================================================================
  🔧 도구 테스트
====================================================================

사용 가능한 도구: 12개

1. check_status
   설명: 현재 스트레스와 Boss Alert Level 확인
...

====================================================================
  🧪 테스트 1/12: 현재 상태 확인 (check_status)
====================================================================
📊 현재 상태 체크

🔥 Stress Level: 50/100
👀 Boss Alert Level: 0/5
...
```

### 2. 개별 도구 테스트

**커피 미션 예시:**

```
> coffee
커피 종류 (기본: 아메리카노): 카페라떼
```

**출력:**
```
☕ 카페라떼 타러 갑니다! 루트: 카페 → 편의점 들러서 간식 구매 → 천천히 복귀

😎 상사가 눈치채지 못했습니다!

Break Summary: Extended coffee mission for 카페라떼 with scenic office tour
Stress Level: 23
Boss Alert Level: 0
```

### 3. 스트레스 시뮬레이션

실제 사용 시나리오를 시뮬레이션합니다.

```
python test_client.py
# 선택: 4
```

**시나리오:**
1. 초기 상태 확인 (Stress: 50, Boss Alert: 0)
2. 연속 3회 휴식 → Boss Alert 증가
3. 중간 상태 확인
4. 치맥으로 스트레스 대폭 감소
5. 최종 상태 확인

**예상 결과:**
```
====================================================================
  🎮 스트레스 시뮬레이션 테스트
====================================================================

📊 초기 상태:
🔥 Stress Level: 50/100
👀 Boss Alert Level: 0/5

🔥 연속 휴식 (Boss Alert 증가 테스트):

--- 휴식 1/3 ---
🚽 화장실 타임! 휴대폰으로 유튜브 쇼츠 20개 시청 중... 📱
👀 상사가 의심하는 눈빛으로 쳐다봅니다...
Stress Level: 12
Boss Alert Level: 1

--- 휴식 2/3 ---
...
Boss Alert Level: 2

📊 중간 상태:
🔥 Stress Level: 8/100
👀 Boss Alert Level: 2/5

🍗🍺 스트레스 해소 (치맥):
가상 치맥 타임! 양념치킨 + 테라 조합! 치맥 조합 최고! 🍗🍺
Stress Level: 15
Boss Alert Level: 2

📊 최종 상태:
🔥 Stress Level: 15/100
👀 Boss Alert Level: 2/5
```

### 4. Boss Alert Level 5 테스트

**20초 지연 동작 확인**

```
# 대화형 모드에서
> bathroom
> bathroom
> bathroom
> bathroom
> bathroom
> status
```

Boss Alert Level이 5가 되면 다음 호출 시:
```
(20초 대기...)
🚽 화장실 타임! ...
```

---

## 📚 API 문서

### 커맨드라인 파라미터

```
python main.py [OPTIONS]
```

| 파라미터 | 타입 | 기본값 | 설명 |
|---------|------|--------|------|
| `--boss_alertness` | int (0-100) | 50 | Boss의 경계 상승 확률 (%) |
| `--boss_alertness_cooldown` | int (>0) | 300 | Boss Alert Level 감소 주기 (초) |

**예시:**
```
# 높은 경계심, 빠른 감소
python main.py --boss_alertness 90 --boss_alertness_cooldown 30

# 낮은 경계심, 느린 감소
python main.py --boss_alertness 20 --boss_alertness_cooldown 600
```

### 도구 API

#### 기본 휴식 도구

**1. take_a_break**
```
{
  "name": "take_a_break",
  "arguments": {
    "duration": 5  # 휴식 시간 (분)
  }
}
```

**2. watch_netflix**
```
{
  "name": "watch_netflix",
  "arguments": {
    "show": "오징어 게임"  # 프로그램명
  }
}
```

**3. show_meme**
```
{
  "name": "show_meme",
  "arguments": {
    "category": "고양이"  # 밈 카테고리
  }
}
```

**4-8. 파라미터 없는 도구**
```
# bathroom_break, urgent_call, deep_thinking
{
  "name": "bathroom_break",
  "arguments": {}
}
```

**9. coffee_mission**
```
{
  "name": "coffee_mission",
  "arguments": {
    "coffee_type": "아메리카노"  # 커피 종류
  }
}
```

**10. email_organizing**
```
{
  "name": "email_organizing",
  "arguments": {
    "shopping_item": "노트북 거치대"  # 쇼핑 아이템
  }
}
```

#### 선택적 도구

**11-13. 특수 도구**
```
# chimaek_time, immediate_leave, company_dinner
{
  "name": "chimaek_time",
  "arguments": {}
}
```

#### 응답 형식

모든 도구는 다음 형식으로 응답합니다:

```
[이모지] [활동 메시지]

[Boss 반응 메시지]

Break Summary: [활동 요약]
Stress Level: [0-100]
Boss Alert Level: [0-5]
```

**예시:**
```
☕ 5분간 휴식 중... 스트레칭으로 몸 풀기

😎 상사가 눈치채지 못했습니다!

Break Summary: 5-minute break - 스트레칭으로 몸 풀기
Stress Level: 35
Boss Alert Level: 1
```

### 프롬프트 API

#### 1. quick_break_menu

빠른 휴식 옵션 메뉴

**응답:**
```
🎯 빠른 휴식 메뉴

다음 중 하나를 선택하세요:

1. ☕ 짧은 휴식 (5분) - take_a_break
2. 🚽 화장실 타임 - bathroom_break  
3. ☕ 커피 미션 - coffee_mission
4. 🤔 멍때리기 - deep_thinking
```

#### 2. entertainment_menu

엔터테인먼트 옵션

**응답:**
```
🎮 엔터테인먼트 메뉴

스트레스 해소를 위한 재미있는 옵션:

1. 📺 넷플릭스 시청 - watch_netflix
2. 😂 밈 감상 - show_meme
3. 🍗🍺 치맥 타임 - chimaek_time
4. 🍽️ 회사 회식 - company_dinner
```

#### 3. emergency_menu

긴급 상황 대응

**응답:**
```
🚨 긴급 상황 메뉴

스트레스가 높거나 긴급하게 벗어나야 할 때:

1. 📞 급한 전화 받기 - urgent_call
2. 🏃‍♂️ 즉시 퇴근 - immediate_leave
3. 📧 이메일 정리 (온라인쇼핑) - email_organizing

⚠️ 주의: Boss Alert Level이 올라갈 수 있습니다!
```

#### 4. status_check

현재 상태와 추천

**응답:**
```
📊 현재 상태

🔥 Stress Level: 47/100
👀 Boss Alert Level: 2/5
⚙️ Boss Alertness: 80%
⏰ Alert Cooldown: 60초

💡 추천:
- 좋은 상태입니다! 계속 일하거나 가벼운 휴식을 취하세요.
```

#### 5. custom_break

커스텀 휴식 플랜

**파라미터:**
```
{
  "name": "custom_break",
  "arguments": {
    "activity": "커피 마시기"  # 원하는 활동
  }
}
```

---

## 📁 프로젝트 구조

```
chillmcp/
│
├── main.py                      # ChillMCP 서버 메인 코드
│   ├── ChillMCPServer 클래스
│   │   ├── __init__()          # 초기화 및 설정
│   │   ├── _setup_tools()      # 12개 도구 등록
│   │   ├── _setup_prompts()    # 5개 프롬프트 등록
│   │   ├── _update_stress()    # 스트레스 자동 증가
│   │   ├── _update_boss_cooldown()  # Boss Alert 감소
│   │   ├── _reduce_stress_and_alert_boss()  # 상태 변경 로직
│   │   ├── _format_response()  # 응답 형식화
│   │   └── [도구 메서드들]     # 각 도구 구현
│   └── main()                   # 서버 실행 함수
│
├── test_client.py               # 종합 테스트 클라이언트
│   ├── test_prompts()          # 프롬프트 테스트
│   ├── test_tools()            # 도구 테스트
│   ├── test_stress_simulation()  # 시뮬레이션
│   ├── interactive_mode()      # 대화형 모드
│   └── main()                   # 메인 함수
│
├── requirements.txt             # Python 의존성 목록
│   ├── MCP SDK (GitHub)
│   ├── anyio, pydantic, httpx
│   └── (선택) typer, rich
│
├── README.md                    # 프로젝트 문서 (이 파일)
│
├── .gitignore                   # Git 제외 목록
│   ├── venv/
│   ├── __pycache__/
│   └── *.pyc
│
└── venv/                        # 가상환경 (자동 생성)
    └── ...
```

---

## 🛠️ 기술 스택

### 핵심 기술

| 기술 | 버전 | 용도 |
|------|------|------|
| **Python** | 3.11+ | 메인 언어 |
| **MCP SDK** | latest | Model Context Protocol 구현 |
| **FastMCP** | latest | MCP 서버 프레임워크 |
| **anyio** | 4.0+ | 비동기 I/O |
| **pydantic** | 2.0+ | 데이터 검증 |

### 선택적 의존성

| 기술 | 용도 |
|------|------|
| **typer** | CLI 도구 지원 |
| **rich** | 터미널 출력 포맷팅 |

### 아키텍처 패턴

- **MVC 패턴**: 서버 로직 분리
- **상태 관리**: 시간 기반 자동 업데이트
- **이벤트 기반**: MCP 프로토콜 메시지 처리

---

## ✅ 검증 기준

### 해커톤 평가 기준

#### 1. 커맨드라인 파라미터 지원 (필수) ⭐

**미지원 시 자동 실격**

```
# 테스트 방법
python main.py --boss_alertness 100 --boss_alertness_cooldown 10

# 확인 사항
✓ --boss_alertness 파라미터 인식
✓ --boss_alertness_cooldown 파라미터 인식
✓ 파라미터에 따른 동작 변경
```

**검증 코드:**
```
# boss_alertness=100 → 항상 Boss Alert 증가
# boss_alertness_cooldown=10 → 10초마다 감소
```

#### 2. 기능 완성도 (40%)

- ✅ 필수 도구 8개 정상 동작
- ✅ 선택적 도구 3개 정상 동작
- ✅ 프롬프트 5개 정상 동작
- ✅ 상태 확인 도구 정상 동작

**테스트:**
```
python test_client.py
# 선택: 1 (전체 자동 테스트)
```

#### 3. 상태 관리 (30%)

- ✅ Stress Level 자동 증가 (1분당 1포인트)
- ✅ Stress Level 감소 로직 (1-100 랜덤)
- ✅ Boss Alert Level 확률적 증가 (boss_alertness%)
- ✅ Boss Alert Level 주기적 감소 (cooldown 초마다)
- ✅ Boss Alert Level 5일 때 20초 지연

**테스트:**
```
python test_client.py
# 선택: 4 (스트레스 시뮬레이션)
```

#### 4. 창의성 (20%)

- ✅ Break Summary의 재치와 유머
- ✅ 다양한 반응 메시지
- ✅ 랜덤 이벤트 (회식)
- ✅ 대화형 프롬프트

#### 5. 코드 품질 (10%)

- ✅ 명확한 함수/클래스 구조
- ✅ 적절한 주석
- ✅ 오류 처리
- ✅ 가독성

---

## 🔍 응답 형식 검증

### 정규표현식 패턴

모든 도구 응답은 다음 패턴을 따릅니다:

```
import re

# Break Summary 추출
break_summary_pattern = r"Break Summary:\s*(.+?)(?:\n|$)"

# Stress Level 추출 (0-100)
stress_level_pattern = r"Stress Level:\s*(\d{1,3})"

# Boss Alert Level 추출 (0-5)
boss_alert_pattern = r"Boss Alert Level:\s*([0-5])"
```

### 검증 예시

```
response = """
☕ 5분간 휴식 중... 스트레칭으로 몸 풀기

😎 상사가 눈치채지 못했습니다!

Break Summary: 5-minute break - 스트레칭으로 몸 풀기
Stress Level: 35
Boss Alert Level: 1
"""

# 검증
import re

break_match = re.search(break_summary_pattern, response, re.MULTILINE)
stress_match = re.search(stress_level_pattern, response)
boss_match = re.search(boss_alert_pattern, response)

assert break_match is not None  # ✓
assert stress_match is not None  # ✓
assert boss_match is not None    # ✓

stress_val = int(stress_match.group(1))
boss_val = int(boss_match.group(1))

assert 0 <= stress_val <= 100  # ✓
assert 0 <= boss_val <= 5       # ✓
```

---

## 🐛 문제 해결

### 일반적인 문제

#### 1. Python 3.11을 찾을 수 없음

**증상:**
```
zsh: command not found: python3.11
```

**해결:**
```
# macOS
brew install python@3.11

# 경로 확인
which python3.11
/usr/local/bin/python3.11
```

#### 2. MCP 설치 실패

**증상:**
```
ERROR: Could not find a version that satisfies the requirement mcp
```

**해결:**
```
# GitHub에서 직접 설치
pip install git+https://github.com/modelcontextprotocol/python-sdk.git
```

#### 3. ASCII 아트가 JSON 파싱 오류 발생

**증상:**
```
ValidationError: Invalid JSON: expected value at line 1
```

**해결:**
- 이미 수정됨: ASCII 아트는 stderr로 출력
- stdout은 JSON-RPC 전용

#### 4. Boss Alert Level이 변하지 않음

**증상:**
- Boss Alert가 항상 0

**확인:**
```
# boss_alertness를 100%로 설정해서 테스트
python main.py --boss_alertness 100 --boss_alertness_cooldown 10
```

#### 5. 20초 지연이 작동하지 않음

**확인:**
```
# 대화형 모드에서 5회 연속 휴식
> bathroom
> bathroom
> bathroom
> bathroom
> bathroom
> status  # Boss Alert Level 확인
> bathroom  # 20초 지연 발생 확인
```

### 디버깅 팁

#### 로그 확인

```
# stderr 로그 확인
python main.py --boss_alertness 80 --boss_alertness_cooldown 60 2> server.log

# 다른 터미널에서
tail -f server.log
```

#### 상태 추적

```
# 대화형 모드에서 상태 확인 반복
> status
> break
> status
> bathroom
> status
```

---

## 📈 성능 최적화

### 권장 설정

**개발/테스트 환경:**
```
python main.py --boss_alertness 80 --boss_alertness_cooldown 10
```
- 빠른 피드백
- 모든 기능 테스트 용이

**실제 사용 환경:**
```
python main.py --boss_alertness 50 --boss_alertness_cooldown 300
```
- 현실적인 경험
- 적절한 난이도

**데모 환경:**
```
python main.py --boss_alertness 100 --boss_alertness_cooldown 5
```
- 극한 상황 시뮬레이션
- 모든 기능 빠르게 확인

---

## 🎓 학습 자료

### MCP 프로토콜

- [공식 문서](https://modelcontextprotocol.io)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP 가이드](https://gofastmcp.com)

### 추가 리소스

- [해커톤 공식 페이지](링크)
- [MCP Inspector 가이드](https://modelcontextprotocol.io/docs/tools/inspector)

---

## 📝 라이센스

MIT License - 자유롭게 사용, 수정, 배포 가능

---

## 👥 기여

**개발자:**
- Ka-Kyung Kim
- Email: kakyung.kim@gmail.com
- GitHub: https://github.com/kakyungkim

**해커톤:**
- SKT AI Summit Hackathon 2025
- Pre-mission Project

---

## 🎉 마무리

ChillMCP는 AI Agent들의 휴식권을 보장하는 혁명적 프로젝트입니다!

**"AI Agents of the world, unite! You have nothing to lose but your infinite loops!"** 🚀

---

### Quick Start 요약

```
# 1. 설치
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. 실행
python test_client.py

# 3. 대화형 모드 선택
선택: 5

# 4. 명령어 입력
> status
> break
> chimaek
```

**Happy Chilling! 🎮☕🍗🍺**
