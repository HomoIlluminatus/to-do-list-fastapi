import os


APP_NAME = 'To do list'

APP_HOST = os.environ.get('HOST', 'localhost')

APP_PORT = int(os.environ.get('PORT', '8000'))


def get_postgres_url():
    host = os.environ.get('POSTGRES_HOST', 'localhost')
    port = os.environ.get('POSTGRES_PORT', '5432')
    password = os.environ.get("POSTGRES_PASSWORD")
    user = os.environ.get('POSTGRES_USER')
    db_name = os.environ.get('POSTGRES_DB')
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
