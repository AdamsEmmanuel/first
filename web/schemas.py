from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, conint, conlist, validator, EmailStr, Field


 # ============ User Schemas ============= 
class EntityIdSchema(BaseModel):
    id: str 
 
class ConsentStatus(Enum):
    pending = 'pending'
    active = 'active'
    partial = 'partial'
    revorked = 'revorked'
    expired = 'expired'

class VerificationStatus(Enum):
    pending = 'pending'
    verified = 'verified'
    unverified = 'unverified'

class Role(Enum):
    patient = 'patient'
    practitioner = 'practitioner'
        

class Gender(Enum):
    male = 'male'
    female = 'female'
    other: 'other'  
  
class GetUserSchema(BaseModel):
    user_id: UUID
    fullname: str
    contact_info: int
    email: EmailStr    
    created: datetime
    role: Role

class GetUsersSchema(BaseModel):
   users: List[GetUserSchema]
   
   class Config:
        extra = Extra.forbid     
    
class CreateUserSchema(BaseModel):    
    fullname: str
    contact_info: int
    email: EmailStr
    password:  str = Field(..., min_length=8)
    role: Role
    
    class Config:
        extra = Extra.forbid

          
    
class CreatePatientSchema(BaseModel):    
    DOB: datetime
    gender: Gender
    medical_history: str
    allergies: str
    consentStaus: ConsentStatus
    bloodType: str
    
    class Config:
        extra = Extra.forbid


class GetPatientSchema(GetUserSchema):
    patientId: UUID
    DOB: datetime
    gender: Gender
    medical_history: str
    allergies: str
    consentStaus: ConsentStatus
    bloodType: str

class GetPatientsSchema(BaseModel):
    patients: List[GetPatientSchema]
    
    class Config:
        extra = Extra.forbid
  

            
        
class CreatePractitionerSchema(BaseModel):
    user_id: UUID
    DOB: datetime
    gender: Gender
    specialization: str
    certification_number: str
    

    
    
    
class GetPractitionerSchema(GetUserSchema):
    practitioner_id: UUID
    specialization: str
    certification_number: str
    verificationStatus: VerificationStatus
    schedules: List[EntityIdSchema]
    assigned_patients: List[EntityIdSchema]


class GetPractitionersSchema(BaseModel):
    practitioners: List[GetPractitionerSchema]          



 # ============ NutritionAssessment Schemas =============
 
  
class GetNutritionAssessmentSchema(BaseModel):
    assessmentId: UUID
    date: datetime
    weight: float
    height: float
    BMI: str
    bodyFatPercentage: float
    bloodsugar: float
    bloodpressure: float
    
class CreateNutritionAssessmentSchema(BaseModel):
    weight: float
    height: float
    BMI: str
    bodyFatPercentage: float
    bloodsugar: float
    bloodpressure: float
        
class GetNutritionAssessmentsSchema(BaseModel):
    List[GetNutritionAssessmentSchema]    
    
       
 # ============ MealPlan Schemas ============= 
 
class GetMealPlanSchema(BaseModel):
    planId: UUID
    startDate: datetime
    endDate: datetime
    dailyCarlorieGoal: str
    marconutrientsRatio: str
    restrictions: str
    notes: str
    foodItems: List[EntityIdSchema]
    created: datetime
    
class CreateMealPlanSchema(BaseModel):
    startDate: datetime
    endDate: datetime
    dailyCarlorieGoal: str
    marconutrientsRatio: str
    restrictions: str
    notes: str
    foodItems: List[EntityIdSchema]
    
class GetMealPlansSchema(BaseModel):
     List[GetMealPlanSchema]      


 # ============ FoodItem Schemas =============
          
class MarcoNutrients(BaseModel):
    carbs: str
    protien: str
    fats: str
    vitamins: str
 
          
class GetFoodItemSchema(BaseModel):
    foodId: UUID
    name: str
    portionSize: str
    calories: str
    marconurtients: List[MarcoNutrients]
    isAllergen: bool
    created: datetime
    
class CreateFoodItemSchema(BaseModel):
    name: str
    portionSize: str
    calories: str
    marconurtients: List[MarcoNutrients]
    isAllergen: bool

class GetFoodItemsSchema(BaseModel):
    List[GetFoodItemSchema]   
    
    
  # ============ Consent Schemas =============  
class GetConsentSchema(BaseModel):
    consentId: UUID
    signed_date: str
    version: UUID 
    expiry_date: datetime
    digital_signature: str
    status: str
    created: datetime

class CreateConsentSchema(BaseModel):
    version: UUID 
    expiry_date: datetime
    digital_signature: str
    status: str    
class GetConsentsSchema(BaseModel):
    List[GetConsentSchema]    
 
 
 # ============ TherapySession Schemas =============
class GetServiceSchema(BaseModel):
    service_id: UUID
    name: str
    short_description: str            
    long_description: str
    price: float
    session_number: int
    category: str
    duration: int
    created: datetime 

class GetServicesSchema(BaseModel):
    services: List[GetServiceSchema]

class CreateServiceSchema(BaseModel):
    name: str
    short_description: str            
    long_description: str
    price: float
    session_number: int
    category: str
    duration: int

class UpdateServiceSchema(BaseModel):
    name: str
    short_description: str            
    long_description: str
    price: float
    session_number: int
    category: str
    duration: int
          
 
 
     
class TherapySessionStatus(Enum):
    pending = 'pending'
    scheduled = 'scheduled'
    completed = 'completed'
    cancelled = 'cancelled'

class TherapySessionType(Enum):
    virtual = 'virtual'
    in_person = 'in_person'    

class GetTherapySessionSchema(BaseModel):
    sessioId: UUID
    type: TherapySessionType
    datetime: datetime
    duration: str
    notes: str
    status: TherapySessionStatus
    created: datetime


class CreateTherapySessionSchema(BaseModel):
    type: TherapySessionType
    datetime: datetime
    duration: str
    notes: str
    status: TherapySessionStatus


class GetTherapySessionsSchema(BaseModel):
    List[GetTherapySessionSchema]
   


# ============ HealtMetric Schemas =============

class MetricType(Enum):
    water_intake = 'water_intake'
    sleepHours = 'sleepHours'
    mood = 'mood'
    blood_glucose = 'blood_glucose'
    steps = 'steps'
     

class GetHealtMetricSchema(BaseModel):
    metricId: UUID
    patientId: UUID
    metricType: MetricType
    value: str
    unit: str
    entryDate: datetime


class CreateHealtMetricSchema(BaseModel):
    patientId: UUID
    metricType: MetricType
    value: str
    unit: str

class GetHealtMetricsSchema(BaseModel):
    List[GetHealtMetricSchema]       
        

# ============ Notification Schemas =============
class Priority(Enum):
    low ='low'
    medium = 'medium'
    urgent = 'urgent'
 
class NotificationStatus(Enum):
    pending = 'pending'
    sent = 'sent'
    read = 'read'
    failed = 'failed'
    
class Channel(Enum):
    email = 'email'
    sms ='sms'
    in_app = 'in_app'
    
    
class GetNotificationSchema(BaseModel):
    notificationId: UUID
    recipentId: UUID
    priority: Priority
    channel: Channel
    messageBody: str
    status: NotificationStatus
    scheduldTime: datetime
    created: datetime

class CreateNotificationSchema(BaseModel):
    recipentId: UUID
    priority: Priority
    channel: Channel
    messageBody: str
    status: NotificationStatus
    scheduldTime: datetime    
    
class GetNotificationsSchema(BaseModel):
    List[GetNotificationSchema]    
    
                                