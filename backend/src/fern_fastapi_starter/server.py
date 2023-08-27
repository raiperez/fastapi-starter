import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.generated.register import register
from .hero_sim_service import HeroSimService

app = FastAPI()

register(app, hero_sim=HeroSimService())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start() -> None:
    uvicorn.run(
        "src.fern_fastapi_starter.server:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )


if __name__ == "__main__":
    start()
