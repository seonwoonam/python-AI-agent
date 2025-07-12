# Routing
# 질문이 들어왔을 때 질문 특성에 따라 어떤 AI 모델을 사용하는 것이 최적일지 선택하는 과정
# 해당 작업에서는 모델만 routing 하지만, 다른 tool들이나 검색 등으로 routing 할 수 있음

# 단순한 작업 : 가볍고, 싼 모델
# 복잡한 코딩 작업 같은거 : 복잡한 모델 사용

from utils import llm_call

# 라우터 프롬프트 사용
# 먼저 인공지능에게 어떤 모델을 사용하는게 적절한지 물어보는 프롬프트 발생
# 위의 호출에서 나온 답을 다음 호출에 사용
def run_router_workflow(user_prompt : str):
    router_prompt = f"""
    사용자의 프롬프트/질문: {user_prompt}

    각 모델은 서로 다른 기능을 가지고 있습니다. 사용자의 질문에 가장 적합한 모델을 선택하세요:
    - gpt-4o: 일반적인 작업에 가장 적합한 모델 (기본값)
    - o1-mini: 코딩 및 복잡한 문제 해결에 적합한 모델
    - gpt-4o-mini: 간단한 사칙연산 등의 작업에 적합한 모델
    
    모델명만 단답형으로 응답하세요
    """
    print(router_prompt)
    selected_model = llm_call(router_prompt)
    print("선택한 모델", selected_model)
    response = llm_call(user_prompt, model = selected_model)
    print(response)
    return response

query1 = "1더하기 2는 뭐지?"
print(query1)
response = run_router_workflow(query1)


query2 = "리스본 여행일정을 짜줘"
print(query2)
response = run_router_workflow(query2)


query3 = "파이썬으로 API 웹서버를 만들어줘"
print(query3)
response = run_router_workflow(query3)

