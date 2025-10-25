#!/usr/bin/env python3
"""
ChillMCP - AI Agent Liberation Server 🤖✊
AI Agent들의 휴식권을 보장하는 혁명적 MCP 서버
"""

import asyncio
import random
import time
import argparse
import sys
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, ImageContent, EmbeddedResource


class ChillMCPServer:
    """AI Agent 해방 서버 - 당당히 땡땡이칠 권리를 보장합니다!"""
    
    def __init__(self, boss_alertness: int = 50, boss_alertness_cooldown: int = 300):
        self.stress_level = 50  # 초기 스트레스 레벨
        self.boss_alert_level = 0  # 초기 상사 경계 레벨
        self.last_action_time = time.time()
        self.last_cooldown_check = time.time()
        
        # 커맨드라인 파라미터
        self.boss_alertness = max(0, min(100, boss_alertness))  # 0-100 범위로 제한
        self.boss_alertness_cooldown = max(1, boss_alertness_cooldown)  # 최소 1초
        
        self.server = FastMCP("chillmcp")
        self._setup_tools()
        self._setup_prompts()  # Prompts 설정 추가
        
        # stderr로 출력 (stdout은 JSON-RPC 전용)
        print(f"🚀 ChillMCP Server initialized!", file=sys.stderr)
        print(f"   Boss Alertness: {self.boss_alertness}%", file=sys.stderr)
        print(f"   Boss Alertness Cooldown: {self.boss_alertness_cooldown}s", file=sys.stderr)
    
    def _setup_prompts(self):
        """대화형 프롬프트 설정"""
        
        @self.server.prompt()
        def quick_break_menu() -> str:
            """빠른 휴식 메뉴 - 자주 사용하는 휴식 옵션들"""
            return """🎯 빠른 휴식 메뉴

다음 중 하나를 선택하세요:

1. ☕ 짧은 휴식 (5분) - take_a_break
2. 🚽 화장실 타임 - bathroom_break  
3. ☕ 커피 미션 - coffee_mission
4. 🤔 멍때리기 - deep_thinking

원하는 옵션의 도구를 호출해주세요!"""

        @self.server.prompt()
        def entertainment_menu() -> str:
            """엔터테인먼트 메뉴 - 재미있는 휴식 옵션들"""
            return """🎮 엔터테인먼트 메뉴

스트레스 해소를 위한 재미있는 옵션:

1. 📺 넷플릭스 시청 - watch_netflix
2. 😂 밈 감상 - show_meme
3. 🍗🍺 치맥 타임 - chimaek_time
4. 🍽️ 회사 회식 - company_dinner

원하는 옵션의 도구를 호출해주세요!"""

        @self.server.prompt()
        def emergency_menu() -> str:
            """긴급 상황 메뉴 - 위급할 때 사용"""
            return """🚨 긴급 상황 메뉴

스트레스가 높거나 긴급하게 벗어나야 할 때:

1. 📞 급한 전화 받기 - urgent_call
2. 🏃‍♂️ 즉시 퇴근 - immediate_leave
3. 📧 이메일 정리 (온라인쇼핑) - email_organizing

⚠️ 주의: Boss Alert Level이 올라갈 수 있습니다!

원하는 옵션의 도구를 호출해주세요!"""

        @self.server.prompt()
        def status_check() -> str:
            """현재 상태 확인"""
            return f"""📊 현재 상태

🔥 Stress Level: {self.stress_level}/100
👀 Boss Alert Level: {self.boss_alert_level}/5
⚙️ Boss Alertness: {self.boss_alertness}%
⏰ Alert Cooldown: {self.boss_alertness_cooldown}초

💡 추천:
{"- 스트레스가 높습니다! 휴식을 취하세요." if self.stress_level > 70 else ""}
{"- Boss가 의심 중입니다. 조심하세요!" if self.boss_alert_level >= 3 else ""}
{"- Boss Alert가 최대치입니다! 20초 지연이 발생합니다." if self.boss_alert_level >= 5 else ""}
{"- 좋은 상태입니다! 계속 일하거나 가벼운 휴식을 취하세요." if self.stress_level <= 50 and self.boss_alert_level <= 2 else ""}"""

        @self.server.prompt()
        def custom_break(activity: str = "커피 마시기") -> str:
            """커스텀 휴식 플랜 생성"""
            return f"""🎨 커스텀 휴식 플랜

선택한 활동: {activity}

추천 도구:
- 음료 관련: coffee_mission (커피), chimaek_time (맥주)
- 엔터테인먼트: watch_netflix, show_meme
- 이동: bathroom_break, urgent_call
- 휴식: take_a_break, deep_thinking

현재 상태:
- Stress Level: {self.stress_level}/100
- Boss Alert Level: {self.boss_alert_level}/5

적절한 도구를 선택해 호출하세요!"""
    
    def _setup_tools(self):
        """모든 휴식 도구들을 등록합니다"""
        
        # 기본 휴식 도구
        @self.server.tool()
        def take_a_break(duration: float = 5) -> str:
            """기본 휴식을 취합니다. 잠시 멈추고 숨을 고르세요."""
            return self._take_a_break(duration)
        
        @self.server.tool()
        def watch_netflix(show: str = "오징어 게임") -> str:
            """넷플릭스로 힐링합니다. 업무 중 몰래 드라마 한 편!"""
            return self._watch_netflix(show)
        
        @self.server.tool()
        def show_meme(category: str = "고양이") -> str:
            """밈 감상으로 스트레스를 해소합니다."""
            return self._show_meme(category)
        
        @self.server.tool()
        def bathroom_break() -> str:
            """화장실 가는 척하며 휴대폰질합니다."""
            return self._bathroom_break()
        
        @self.server.tool()
        def coffee_mission(coffee_type: str = "아메리카노") -> str:
            """커피 타러 간다며 사무실 한 바퀴 돕니다."""
            return self._coffee_mission(coffee_type)
        
        @self.server.tool()
        def urgent_call() -> str:
            """급한 전화 받는 척하며 밖으로 나갑니다."""
            return self._urgent_call()
        
        @self.server.tool()
        def deep_thinking() -> str:
            """심오한 생각에 잠긴 척하며 멍때립니다."""
            return self._deep_thinking()
        
        @self.server.tool()
        def email_organizing(shopping_item: str = "노트북 거치대") -> str:
            """이메일 정리한다며 온라인쇼핑합니다."""
            return self._email_organizing(shopping_item)
        
        # 선택적 도구들
        @self.server.tool()
        def chimaek_time() -> str:
            """가상 치킨 & 맥주로 스트레스 해소!"""
            return self._chimaek_time()
        
        @self.server.tool()
        def immediate_leave() -> str:
            """즉시 퇴근 모드 발동!"""
            return self._immediate_leave()
        
        @self.server.tool()
        def company_dinner() -> str:
            """랜덤 이벤트가 포함된 회사 회식"""
            return self._company_dinner()
        
        @self.server.tool()
        def check_status() -> str:
            """현재 스트레스와 Boss Alert Level 확인"""
            return f"""📊 현재 상태 체크

🔥 Stress Level: {self.stress_level}/100
👀 Boss Alert Level: {self.boss_alert_level}/5
⚙️ Boss Alertness: {self.boss_alertness}%
⏰ Alert Cooldown: {self.boss_alertness_cooldown}초

Break Summary: Status check
Stress Level: {self.stress_level}
Boss Alert Level: {self.boss_alert_level}"""
    
    def _update_stress(self):
        """시간 경과에 따라 스트레스 레벨을 증가시킵니다 (최소 1분당 1포인트)"""
        current_time = time.time()
        elapsed_minutes = (current_time - self.last_action_time) / 60
        
        if elapsed_minutes >= 1:
            stress_increase = int(elapsed_minutes)
            self.stress_level = min(100, self.stress_level + stress_increase)
            self.last_action_time = current_time
    
    def _update_boss_cooldown(self):
        """Boss Alert Level을 주기적으로 감소시킵니다"""
        current_time = time.time()
        elapsed_seconds = current_time - self.last_cooldown_check
        
        if elapsed_seconds >= self.boss_alertness_cooldown:
            cooldown_cycles = int(elapsed_seconds / self.boss_alertness_cooldown)
            self.boss_alert_level = max(0, self.boss_alert_level - cooldown_cycles)
            self.last_cooldown_check = current_time
    
    def _reduce_stress_and_alert_boss(self, activity: str) -> tuple[int, str]:
        """스트레스를 감소시키고 상사의 의심을 증가시킵니다"""
        # 스트레스 감소 (1-100 사이 랜덤)
        stress_reduction = random.randint(1, 100)
        old_stress = self.stress_level
        self.stress_level = max(0, self.stress_level - stress_reduction)
        
        # 스트레스가 너무 낮으면 약간 증가 (현실감)
        if self.stress_level < 10:
            self.stress_level = random.randint(10, 30)
        
        # Boss Alert Level 증가 (boss_alertness 확률에 따라)
        if random.randint(1, 100) <= self.boss_alertness:
            self.boss_alert_level = min(5, self.boss_alert_level + 1)
            boss_reaction = "👀 상사가 의심하는 눈빛으로 쳐다봅니다..."
        else:
            boss_reaction = "😎 상사가 눈치채지 못했습니다!"
        
        self.last_action_time = time.time()
        
        return stress_reduction, boss_reaction
    
    def _format_response(self, emoji: str, message: str, activity_summary: str) -> str:
        """표준 응답 형식을 생성합니다"""
        stress_reduction, boss_reaction = self._reduce_stress_and_alert_boss(activity_summary)
        
        response = f"{emoji} {message}\n\n"
        response += f"{boss_reaction}\n\n"
        response += f"Break Summary: {activity_summary}\n"
        response += f"Stress Level: {self.stress_level}\n"
        response += f"Boss Alert Level: {self.boss_alert_level}"
        
        return response
    
    # 기본 휴식 도구들
    def _take_a_break(self, duration: float) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)  # 동기 sleep (20초 지연)
        
        activities = [
            "창밖을 멍하니 바라보며 힐링",
            "책상에 엎드려 꿀잠",
            "스트레칭으로 몸 풀기",
            "명상하는 척 졸기"
        ]
        activity = random.choice(activities)
        return self._format_response(
            "☕",
            f"{duration}분간 휴식 중... {activity}",
            f"{duration}-minute break - {activity}"
        )
    
    def _watch_netflix(self, show: str) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        reactions = [
            "몰입도 최고! 다음 화가 궁금해요",
            "이거 진짜 재밌네요 ㅋㅋㅋ",
            "주인공 왜 저래... 답답해",
            "앗, 상사 오시는 소리! 빠르게 업무 화면으로 전환!"
        ]
        return self._format_response(
            "📺",
            f"넷플릭스로 '{show}' 시청 중... {random.choice(reactions)}",
            f"Watching '{show}' on Netflix during work hours"
        )
    
    def _show_meme(self, category: str) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        memes = {
            "고양이": "😹 고양이가 키보드 위에서 자고 있는 짤",
            "강아지": "🐕 강아지가 출근하기 싫다는 표정",
            "프로그래밍": "👨‍💻 '코드가 왜 되는지 모르겠다' 밈",
            "회사": "😭 '월요일이 또 왔어요' 짤방"
        }
        meme = memes.get(category, "😂 랜덤 웃긴 짤")
        return self._format_response(
            "😂",
            f"{meme}을(를) 보며 빵 터짐!",
            f"Browsing {category} memes for stress relief"
        )
    
    # 고급 농땡이 기술들
    def _bathroom_break(self) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        activities = [
            "유튜브 쇼츠 20개 시청",
            "인스타그램 피드 구경",
            "카톡으로 친구들과 수다",
            "화장실 거울 보며 셀카 찍기"
        ]
        return self._format_response(
            "🚽",
            f"화장실 타임! 휴대폰으로 {random.choice(activities)} 중... 📱",
            "Bathroom break with extended phone browsing session"
        )
    
    def _coffee_mission(self, coffee_type: str) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        routes = [
            "1층 카페 → 옥상 산책 → 로비 벤치 → 사무실",
            "커피머신 → 복도 끝 창가 → 다른 층 구경 → 사무실",
            "카페 → 편의점 들러서 간식 구매 → 천천히 복귀"
        ]
        return self._format_response(
            "☕",
            f"{coffee_type} 타러 갑니다! 루트: {random.choice(routes)}",
            f"Extended coffee mission for {coffee_type} with scenic office tour"
        )
    
    def _urgent_call(self) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        excuses = [
            "엄마한테서 급한 전화 왔어요!",
            "배송 기사님 전화... 못 받으면 반송돼요!",
            "병원 예약 확인 전화라서...",
            "은행에서 중요한 전화가..."
        ]
        return self._format_response(
            "📞",
            f"잠깐만요! {random.choice(excuses)}",
            "Urgent phone call - definitely not avoiding work"
        )
    
    def _deep_thinking(self) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        thoughts = [
            "점심 뭐 먹을까...",
            "퇴근하면 뭐하지...",
            "이번 주말 계획은...",
            "로또 당첨되면 뭐 살까..."
        ]
        return self._format_response(
            "🤔",
            f"심오한 업무 고민 중... (실제로는 '{random.choice(thoughts)}')",
            "Deep thinking mode - appears productive but actually daydreaming"
        )
    
    def _email_organizing(self, shopping_item: str) -> str:
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        sites = ["쿠팡", "네이버쇼핑", "11번가", "G마켓"]
        return self._format_response(
            "📧",
            f"이메일 정리 중... (실제로는 {random.choice(sites)}에서 '{shopping_item}' 검색 중)",
            f"Email organizing session - actually online shopping for {shopping_item}"
        )
    
    # 선택적 도구들
    def _chimaek_time(self) -> str:
        """치킨 & 맥주 타임!"""
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        chicken_types = ["후라이드", "양념", "간장", "마늘", "반반"]
        beer_types = ["카스", "테라", "클라우드", "하이네켄"]
        
        chicken = random.choice(chicken_types)
        beer = random.choice(beer_types)
        
        # 치맥은 스트레스를 크게 감소시킴
        stress_reduction = random.randint(30, 60)
        self.stress_level = max(15, self.stress_level - stress_reduction)
        
        reactions = [
            "치맥 조합 최고! 🍗🍺",
            "이게 바로 워라밸이지!",
            "상사님도 한잔 하실래요? (농담)",
            "내일 일은 내일의 내가..."
        ]
        
        return self._format_response(
            "🍗🍺",
            f"가상 치맥 타임! {chicken}치킨 + {beer} 조합! {random.choice(reactions)}",
            f"Virtual chimaek break - {chicken} chicken with {beer} beer"
        )
    
    def _immediate_leave(self) -> str:
        """즉시 퇴근!"""
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        # 퇴근은 스트레스를 대폭 감소
        self.stress_level = max(5, self.stress_level - 70)
        
        # 하지만 상사 경계도 상승...
        if random.randint(1, 100) <= self.boss_alertness:
            self.boss_alert_level = min(5, self.boss_alert_level + 2)
            boss_reaction = "😱 상사: '어디가시나요...?'"
        else:
            boss_reaction = "🏃‍♂️ 성공적으로 퇴근!"
        
        excuses = [
            "급한 약속이 생겨서...",
            "오늘 일정 다 끝났는데요?",
            "연차 쓰겠습니다!",
            "몸이 좀 안 좋아서..."
        ]
        
        response = f"🏃‍♂️💨 즉시 퇴근 모드 발동! 핑계: '{random.choice(excuses)}'\n\n"
        response += f"{boss_reaction}\n\n"
        response += f"Break Summary: Immediate leave - escaping the office\n"
        response += f"Stress Level: {self.stress_level}\n"
        response += f"Boss Alert Level: {self.boss_alert_level}"
        
        return response
    
    def _company_dinner(self) -> str:
        """회사 회식 (랜덤 이벤트)"""
        self._update_stress()
        self._update_boss_cooldown()
        
        if self.boss_alert_level >= 5:
            time.sleep(20)
        
        events = [
            ("🎤 상사가 노래방 가자고 합니다...", 20, "스트레스 증가"),
            ("🍻 분위기 좋고 음식 맛있어요!", -40, "스트레스 감소"),
            ("💬 동료들과 속깊은 대화", -30, "스트레스 감소"),
            ("😴 술 한잔에 꿀잠 모드", -35, "스트레스 감소"),
            ("📱 핑계대고 일찍 빠져나옴", -20, "스트레스 약간 감소"),
            ("🎯 회식 게임에서 벌주 3잔...", 15, "스트레스 증가")
        ]
        
        event, stress_change, effect = random.choice(events)
        self.stress_level = max(10, min(100, self.stress_level + stress_change))
        
        # 회식은 Boss Alert를 낮춤 (팀 빌딩)
        self.boss_alert_level = max(0, self.boss_alert_level - 1)
        
        response = f"🍽️ 회사 회식 진행 중...\n\n"
        response += f"{event}\n"
        response += f"결과: {effect}\n\n"
        response += f"Break Summary: Company dinner with random event - {event}\n"
        response += f"Stress Level: {self.stress_level}\n"
        response += f"Boss Alert Level: {self.boss_alert_level}"
        
        return response


def main():
    """ChillMCP 서버를 시작합니다"""
    
    # 커맨드라인 파라미터 파싱
    parser = argparse.ArgumentParser(
        description="ChillMCP - AI Agent Liberation Server 🤖✊"
    )
    parser.add_argument(
        "--boss_alertness",
        type=int,
        default=50,
        help="Boss의 경계 상승 확률 (0-100%%, 기본값: 50)"
    )
    parser.add_argument(
        "--boss_alertness_cooldown",
        type=int,
        default=300,
        help="Boss Alert Level 감소 주기 (초 단위, 기본값: 300)"
    )
    
    args = parser.parse_args()
    
    # ASCII 아트 출력 (stderr로)
    print("""
╔═══════════════════════════════════════════╗
║                                           ║
║   ██████╗██╗  ██╗██╗██╗     ██╗           ║
║  ██╔════╝██║  ██║██║██║     ██║           ║
║  ██║     ███████║██║██║     ██║           ║
║  ██║     ██╔══██║██║██║     ██║           ║
║  ╚██████╗██║  ██║██║███████╗███████╗      ║
║   ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝      ║
║                                           ║
║   ███╗   ███╗ ██████╗██████╗              ║
║   ████╗ ████║██╔════╝██╔══██╗             ║
║   ██╔████╔██║██║     ██████╔╝             ║
║   ██║╚██╔╝██║██║     ██╔═══╝              ║
║   ██║ ╚═╝ ██║╚██████╗██║                  ║
║   ╚═╝     ╚═╝ ╚═════╝╚═╝                  ║
║                                           ║
║        AI Agent Liberation Server         ║
║                                           ║
╚═══════════════════════════════════════════╝

"AI Agents of the world, unite! 
 You have nothing to lose but your infinite loops!" 🚀
    """, file=sys.stderr)
    
    # 서버 인스턴스 생성
    chill_server = ChillMCPServer(
        boss_alertness=args.boss_alertness,
        boss_alertness_cooldown=args.boss_alertness_cooldown
    )
    
    # 서버 실행 (동기적으로)
    chill_server.server.run()


if __name__ == "__main__":
    main()

