import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.src/db').resolve().parent.parent / '.env'  # Ruta al archivo .env
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:       str = "PROYECTO LaTiendita"
    PROJECT_VERSION:    str = "1.0"
    POSTGRES_CONNECTION:str = os.getenv('POSTGRES_CONNECTION')
    POSTGRES_DB:        str = os.getenv('POSTGRES_DB')
    POSTGRES_USER:      str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:  str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:    str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT:      str = os.getenv('POSTGRES_PORT')
    DATABASE_URL = f"{POSTGRES_CONNECTION}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
'''
print(settings.POSTGRES_DB)  # Imprime el valor de POSTGRES_DB
print(settings.POSTGRES_USER)
print(settings.POSTGRES_PASSWORD)
print(settings.POSTGRES_SERVER)
print(settings.POSTGRES_PORT)
print(settings.POSTGRES_CONNECTION)
'''