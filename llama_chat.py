
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "You can help men learn python ?",
        "stream": False
    }
)

print(response.json()["response"])
