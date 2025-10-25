#!/usr/bin/env python3
"""
ChillMCP 서버 종합 테스트 클라이언트
모든 도구와 프롬프트를 테스트합니다.
"""

import asyncio
import sys
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


def print_separator(title=""):
    """구분선 출력"""
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)
    else:
        print()


async def test_prompts(session):
    """프롬프트 테스트"""
    print_separator("📋 프롬프트 테스트")
    
    try:
        # 사용 가능한 프롬프트 목록
        prompts = await session.list_prompts()
        print(f"\n사용 가능한 프롬프트: {len(prompts.prompts)}개\n")
        
        for i, prompt in enumerate(prompts.prompts, 1):
            print(f"{i}. {prompt.name}")
            print(f"   설명: {prompt.description}")
        
        # 각 프롬프트 실행
        prompt_names = [
            "quick_break_menu",
            "entertainment_menu", 
            "emergency_menu",
            "status_check",
        ]
        
        for prompt_name in prompt_names:
            print_separator(f"🎯 프롬프트: {prompt_name}")
            try:
                result = await session.get_prompt(prompt_name)
                for msg in result.messages:
                    if hasattr(msg.content, 'text'):
                        print(msg.content.text)
                    else:
                        print(msg.content)
            except Exception as e:
                print(f"❌ 오류: {e}")
            
            await asyncio.sleep(0.5)
        
        print("\n✅ 프롬프트 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 프롬프트 테스트 실패: {e}")


async def test_tools(session):
    """도구 테스트"""
    print_separator("🔧 도구 테스트")
    
    try:
        # 사용 가능한 도구 목록
        tools = await session.list_tools()
        print(f"\n사용 가능한 도구: {len(tools.tools)}개\n")
        
        for i, tool in enumerate(tools.tools, 1):
            print(f"{i}. {tool.name}")
            print(f"   설명: {tool.description}")
        
        # 각 도구 테스트
        test_cases = [
            ("check_status", {}, "현재 상태 확인"),
            ("take_a_break", {"duration": 5}, "5분 휴식"),
            ("watch_netflix", {"show": "오징어 게임"}, "넷플릭스 시청"),
            ("show_meme", {"category": "고양이"}, "밈 감상"),
            ("bathroom_break", {}, "화장실 타임"),
            ("coffee_mission", {"coffee_type": "아메리카노"}, "커피 미션"),
            ("urgent_call", {}, "급한 전화"),
            ("deep_thinking", {}, "멍때리기"),
            ("email_organizing", {"shopping_item": "무선 마우스"}, "이메일 정리"),
            ("chimaek_time", {}, "치맥 타임"),
            ("immediate_leave", {}, "즉시 퇴근"),
            ("company_dinner", {}, "회사 회식"),
        ]
        
        for i, (tool_name, args, description) in enumerate(test_cases, 1):
            print_separator(f"🧪 테스트 {i}/{len(test_cases)}: {description} ({tool_name})")
            
            try:
                result = await session.call_tool(tool_name, arguments=args)
                
                # 결과 출력
                if hasattr(result, 'content') and len(result.content) > 0:
                    content = result.content[0]
                    if hasattr(content, 'text'):
                        print(content.text)
                    else:
                        print(content)
                else:
                    print(result)
                
            except Exception as e:
                print(f"❌ 오류: {e}")
            
            # 약간의 지연 (서버 부하 방지)
            await asyncio.sleep(1)
        
        print("\n✅ 도구 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 도구 테스트 실패: {e}")


async def test_stress_simulation(session):
    """스트레스 시뮬레이션 테스트"""
    print_separator("🎮 스트레스 시뮬레이션 테스트")
    
    try:
        # 1. 초기 상태 확인
        print("\n📊 초기 상태:")
        result = await session.call_tool("check_status", arguments={})
        print(result.content[0].text)
        
        await asyncio.sleep(1)
        
        # 2. 여러 휴식 연속 실행 (Boss Alert 증가 유도)
        print("\n🔥 연속 휴식 (Boss Alert 증가 테스트):")
        for i in range(3):
            print(f"\n--- 휴식 {i+1}/3 ---")
            result = await session.call_tool("bathroom_break", arguments={})
            print(result.content[0].text)
            await asyncio.sleep(0.5)
        
        # 3. 중간 상태 확인
        print("\n📊 중간 상태:")
        result = await session.call_tool("check_status", arguments={})
        print(result.content[0].text)
        
        await asyncio.sleep(1)
        
        # 4. 스트레스 해소 (치맥)
        print("\n🍗🍺 스트레스 해소 (치맥):")
        result = await session.call_tool("chimaek_time", arguments={})
        print(result.content[0].text)
        
        await asyncio.sleep(1)
        
        # 5. 최종 상태 확인
        print("\n📊 최종 상태:")
        result = await session.call_tool("check_status", arguments={})
        print(result.content[0].text)
        
        print("\n✅ 시뮬레이션 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 시뮬레이션 테스트 실패: {e}")


async def interactive_mode(session):
    """대화형 모드"""
    print_separator("🎯 대화형 모드")
    
    print("""
사용 가능한 명령:

1. prompts - 프롬프트 목록 보기
2. tools - 도구 목록 보기
3. status - 현재 상태 확인
4. break - 짧은 휴식
5. netflix - 넷플릭스 시청
6. bathroom - 화장실 타임
7. coffee - 커피 미션
8. chimaek - 치맥 타임
9. leave - 즉시 퇴근
10. dinner - 회사 회식
11. quit - 종료

명령을 입력하세요:
    """)
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command == "quit":
                print("👋 종료합니다.")
                break
            
            elif command == "prompts":
                prompts = await session.list_prompts()
                for i, prompt in enumerate(prompts.prompts, 1):
                    print(f"{i}. {prompt.name}: {prompt.description}")
            
            elif command == "tools":
                tools = await session.list_tools()
                for i, tool in enumerate(tools.tools, 1):
                    print(f"{i}. {tool.name}: {tool.description}")
            
            elif command == "status":
                result = await session.call_tool("check_status", arguments={})
                print(result.content[0].text)
            
            elif command == "break":
                result = await session.call_tool("take_a_break", arguments={"duration": 5})
                print(result.content[0].text)
            
            elif command == "netflix":
                show = input("프로그램 이름 (기본: 오징어 게임): ").strip() or "오징어 게임"
                result = await session.call_tool("watch_netflix", arguments={"show": show})
                print(result.content[0].text)
            
            elif command == "bathroom":
                result = await session.call_tool("bathroom_break", arguments={})
                print(result.content[0].text)
            
            elif command == "coffee":
                coffee_type = input("커피 종류 (기본: 아메리카노): ").strip() or "아메리카노"
                result = await session.call_tool("coffee_mission", arguments={"coffee_type": coffee_type})
                print(result.content[0].text)
            
            elif command == "chimaek":
                result = await session.call_tool("chimaek_time", arguments={})
                print(result.content[0].text)
            
            elif command == "leave":
                result = await session.call_tool("immediate_leave", arguments={})
                print(result.content[0].text)
            
            elif command == "dinner":
                result = await session.call_tool("company_dinner", arguments={})
                print(result.content[0].text)
            
            else:
                print("❌ 알 수 없는 명령입니다. 다시 입력해주세요.")
        
        except KeyboardInterrupt:
            print("\n\n👋 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류: {e}")


async def main():
    """메인 테스트 함수"""
    
    # 서버 파라미터 설정
    server_params = StdioServerParameters(
        command="python",
        args=["main.py", "--boss_alertness", "80", "--boss_alertness_cooldown", "60"],
        env=None
    )
    
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║              ChillMCP 서버 종합 테스트 클라이언트                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    print("🔌 ChillMCP 서버에 연결 중...")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # 서버 초기화
                await session.initialize()
                print("✅ 서버 연결 성공!\n")
                
                # 테스트 메뉴
                print("""
테스트 옵션을 선택하세요:

1. 전체 자동 테스트 (프롬프트 + 도구)
2. 프롬프트만 테스트
3. 도구만 테스트
4. 스트레스 시뮬레이션
5. 대화형 모드
6. 종료

선택 (1-6):""", end=" ")
                
                choice = input().strip()
                
                if choice == "1":
                    await test_prompts(session)
                    await asyncio.sleep(2)
                    await test_tools(session)
                    await asyncio.sleep(2)
                    await test_stress_simulation(session)
                
                elif choice == "2":
                    await test_prompts(session)
                
                elif choice == "3":
                    await test_tools(session)
                
                elif choice == "4":
                    await test_stress_simulation(session)
                
                elif choice == "5":
                    await interactive_mode(session)
                
                elif choice == "6":
                    print("👋 종료합니다.")
                
                else:
                    print("❌ 잘못된 선택입니다.")
                
                print_separator("🎉 테스트 완료")
                
    except KeyboardInterrupt:
        print("\n\n⚠️ 사용자가 중단했습니다.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 프로그램을 종료합니다.")
        sys.exit(0)

