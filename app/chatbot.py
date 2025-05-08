import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from fastapi import FastAPI, HTTPException
from models import ChatRequest, ChatResponse
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")
# print("api_key", my_api_key)

client = OpenAI(api_key=my_api_key)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/")
def chat_prompt(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": request.prompt
                }
            ]
        )
        gpt_response = completion.choices[0].message.content
        return ChatResponse(response=gpt_response)

    except OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI api error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
