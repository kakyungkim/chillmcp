#!/usr/bin/env python3
"""ChillMCP 전체 도구 테스트"""

import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def test_all_tools():
    """모든 도구 테스트"""
    
    server_params = StdioServerParameters(
        command="python",
        args=["main.py", "--boss_alertness", "80", "--boss_alertness_cooldown", "60"],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("✅ 서버 초기화 완료\n")
            
            # 모든 도구 테스트
            tests = [
                ("take_a_break", {"duration": 5}),
                ("watch_netflix", {"show": "오징어 게임"}),
                ("show_meme", {"category": "고양이"}),
                ("bathroom_break", {}),
                ("coffee_mission", {"coffee_type": "아메리카노"}),
                ("urgent_call", {}),
                ("deep_thinking", {}),
                ("email_organizing", {"shopping_item": "노트북 거치대"}),
                ("chimaek_time", {}),  # 새로 추가
                ("immediate_leave", {}),  # 새로 추가
                ("company_dinner", {}),  # 새로 추가
            ]
            
            for i, (tool_name, args) in enumerate(tests, 1):
                print(f"{'='*60}")
                print(f"🧪 테스트 {i}/{len(tests)}: {tool_name}")
                print(f"{'='*60}")
                result = await session.call_tool(tool_name, arguments=args)
                print(f"{result.content[0].text}\n")
                await asyncio.sleep(0.5)  # 약간의 지연
            
            print(f"{'='*60}")
            print("✅ 모든 테스트 완료!")
            print(f"{'='*60}")

if __name__ == "__main__":
    asyncio.run(test_all_tools())

