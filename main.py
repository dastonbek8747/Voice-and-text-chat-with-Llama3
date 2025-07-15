from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/home")
async def get_home():
    response = {
        "text": "Welkome Your home !"
    }
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
