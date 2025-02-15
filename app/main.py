from fastapi import FastAPI

from core.config import APP_HOST, APP_PORT, APP_NAME


app = FastAPI(title=APP_NAME)


app.include_router(
    
)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
    