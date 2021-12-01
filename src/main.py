from fastapi import FastAPI

from infra.web.routers import router


app = FastAPI()
app.include_router(router)
