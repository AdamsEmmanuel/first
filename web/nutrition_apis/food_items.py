from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import PractitionerNotFoundError
from services.services.identity_services import PractitionersService
from repository.identity_repository import PractitionersRepository
from repository.unit_of_work import UnitOfWork

from ..schemas import (
    CreateFoodItemSchema,
    GetFoodItemSchema,
    GetFoodItemsSchema   
)
router = APIRouter(prefix="/foodItems", tags=["FoodItems"])


@router.get("/", response_model=GetPractitionerSchema)
def get_foodItems(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = FoodItemsRepository(unit_of_work.session)
        fooditems_service = PractitionersService(repo)
        results = diary_service.list_practitioners(limit=limit, created=created)      

    return { "practitioners": [result.dict() for result in results]}
