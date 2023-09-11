from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from qr_code_generator import QRcode

# uvicorn app:app --reload

app = FastAPI(title="Test API")
qr = QRcode()


# Temporary solution for CORS policy
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://ui-qr-git-develop-denysmoon.vercel.app",
    "https://ui-qr-denysmoon.vercel.app",
    "https://ui-qr.vercel.app",
    "https://qr-code-ui-six.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def say_hello():
    return "Hello!"


@app.post("/api/get-qr-code")
async def get_qr_code(request: Request):
    data = await request.json()

    qr_str = data.get("qr-str")

    qr_code_base64 = qr.get_qr_code(qr_str)
    return qr_code_base64
