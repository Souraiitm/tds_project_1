# ///   script
#   requires-python = ">=3.13"
#   dependencies = [
#       "fastapi",
#       "uvicorn",
#       "requests",
# ]
# ///


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

@app.get ("/")
def home ():
    return {"yep this is running"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run (app, host="0.0.0.0", port=8000)