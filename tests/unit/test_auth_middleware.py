from __future__ import annotations

from fastapi import FastAPI

from server.auth_middleware import (
    AuthenticationMiddleware,
)


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        AuthenticationMiddleware,
    )
