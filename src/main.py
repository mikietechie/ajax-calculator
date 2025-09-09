"""...."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import router


def get_app() -> FastAPI:
    """..."""
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,  # Allow cookies and authorization headers
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, ...)
        allow_headers=["*"],  # Allow all headers in the request
    )
    app.include_router(router=router)
    return app


def main():
    """..."""
    uvicorn.run(app=get_app(), port=8000)


if __name__ == "__main__":
    main()
