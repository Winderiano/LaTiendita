from fastapi import FastAPI
from starlette.responses import RedirectResponse
from .routes.routes import pro
from .config.config import engine
from .models import models
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

description = '''
La Tiedita

Developer Back-End 
Winder Ricardo Delgado Pereira.
'''

app = FastAPI(
    title="La Tiendita",
    description=description,
    version=1.0,
    openapi_tags=[{
        "name": "products",
        "description": "products routes"
    }]
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(pro,prefix="/Products",tags=["Product"])


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
