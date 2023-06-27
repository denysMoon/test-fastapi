from fastapi import FastAPI, Request
from qr_code_generator import QRcode

# uvicorn app:app --reload

app = FastAPI(title="Test API")
qr = QRcode()


@app.get("/")
def say_hello():
    return "Hello!"


@app.post("/api/get-qr-code")
async def get_qr_code(request: Request):
    data = await request.json()

    qr_str = data.get("qr-str")

    qr_code_base64 = qr.get_qr_code(qr_str)
    return qr_code_base64
