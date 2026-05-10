from repository.database import engine
from repository.models import(
    UserModel,
    PatientModel,
    PractitionerModel,
    FoodItemModel,
    DataModel,
    MealPlanModel,
    ServiceModel,
    TherapySessionModel,
    NutritionAssessment,
    HealtMetricModel,
    NotificationModel,
    ConsentModel,
    AuditLog, 
    
)
from repository.database import Base

Base.metadata.create_all(bind=engine)