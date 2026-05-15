from fastapi import FastAPI
import uvicorn
from web.identity_apis import (
    users,
    patients,
    practitioners
)
from web.nutrition_apis import(
    meal_plan,
    food_items
)

from web.core_apis import (
    therapy_sessions,
    services
)

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#import table_creator


app.include_router(users.router, prefix="/api/v1")
app.include_router(patients.router, prefix="/api/v1")
app.include_router(practitioners.router, prefix="/api/v1")
app.include_router(meal_plan.router, prefix="/api/v1")
app.include_router(food_items.router, prefix="/api/v1")
app.include_router(therapy_sessions.router, prefix="/api/v1")
app.include_router(services.router, prefix="/api/v1")


    
if __name__ == "__main__" :
    uvicorn.run("main:app", host = "127.0.0.1", port= 8000,reload=True)    