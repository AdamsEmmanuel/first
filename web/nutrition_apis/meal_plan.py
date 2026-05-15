from datetime import datetime
from uuid import uuid4,UUID
from typing import Optional


from starlette.responses import Response
from starlette import status
from fastapi import APIRouter, HTTPException , Request

from services.exceptions import MealPlanNotFoundError
from services.services.nutrition_services import MealPlansService
from repository.nutrition_repository import MealPlansRepository
from repository.unit_of_work import UnitOfWork

from ..schemas import (
    CreateMealPlanSchema,
    GetMealPlanSchema,
    GetMealPlansSchema   
)
router = APIRouter(prefix="/mealplans", tags=["MealPlans"])


@router.get("/", response_model=Schema)
def get_practitioners(created: Optional[datetime] = None, limit: Optional[int] = None):
    with UnitOfWork() as unit_of_work:
        repo = PractitionersRepository(unit_of_work.session)
        diary_service = PractitionersService(repo)
        results = diary_service.list_practitioners(limit=limit, created=created)      

    return { "practitioners": [result.dict() for result in results]}
