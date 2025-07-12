# llm에게 요청을 보내는 함수들이 있는 파일

import re
from openai import AsyncOpenAI, OpenAI
from key import OPENAI_API_KEY

async_client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,  
)
sync_client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def llm_call(prompt: str,  model: str = "gpt-4o-mini") -> str:
    messages = []
    messages.append({"role": "user", "content": prompt})
    chat_completion = sync_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return chat_completion.choices[0].message.content

# 비동기 호출 사용하기 위해 만들어둔 함수
async def llm_call_async(prompt: str,  model: str = "gpt-4o-mini") -> str:
    messages = []
    messages.append({"role": "user", "content": prompt})
    chat_completion = await async_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    print(model,"완료")
    
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    test = llm_call("안녕")
    print(test)