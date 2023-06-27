import uvicorn
from os import environ

if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
