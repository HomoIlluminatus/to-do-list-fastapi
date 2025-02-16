from fastapi import FastAPI

from core.config import APP_HOST, APP_PORT, APP_NAME
from routers import (
    user_router,
    category_router,
)


routers_list = [
    user_router.router,
    category_router.router,
]


app = FastAPI(title=APP_NAME)


for router in routers_list:
    app.include_router(router)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
    