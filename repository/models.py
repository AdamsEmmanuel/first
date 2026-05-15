import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Boolean, String, ForeignKey, DateTime, TIMESTAMP, Table, Dialect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import Base


def generate_uuid():
    return str(uuid.uuid4()) 


class UserModel(Base):
    __tablename__ = 'users'
    user_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    fullname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    role = Column(String, nullable=False)
    contact_info = Column(String(15), nullable=False)       
    created = Column(DateTime, default=datetime.utcnow)
    
    def dict(self):
        return {
            'user_id': self.user_id,
            'fullname': self.fullname,
            'email': self.email,            
            'role': self.role,
            'contact_info': self.contact_info,
            'created': self.created          
             
        }

patient_enrolled_services = Table(
    "patient_ordered_services",
    Base.metadata,
    Column("patient_id", String(50), ForeignKey("patients.patient_id")),
    Column("service_id", String(50), ForeignKey("services.service_id")),
    Column('assigned_practitioner',String(50), ForeignKey("practitioners.practitioner_id")),
    Column('sessions_done', Integer, nullable=False , default= 0),
    Column('health_metric',String(50), ForeignKey("health_metrics.metric_id"), unique = True),
    Column('status',String(50), nullable=False, default='unactive'),
    Column('paid',Boolean(50), nullable=False, default=True)
    
)

patient_notifications = Table(
    "patient_notifications",
    Base.metadata,
    Column("patient_id", String(50), ForeignKey("patients.patient_id")),
    Column("notification_id", String(50), ForeignKey("notifications.notification_id"))
)               
class PatientModel(Base):
    __tablename__ = 'patients'
    user_id = Column(String(50), ForeignKey("users.user_id"), unique=True)
    patient_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    DOB = Column(DateTime, nullable=False)
    gender = Column(String(50), nullable=False)
    medical_history  = Column(String(50), nullable=False , default='None')
    allergies = Column(String(50), nullable=False, default='None')       
    consent_id = Column(String(50), ForeignKey("consents.consent_id"), unique=True)
    enrolled_services =  relationship(
        "ServiceModel",
        secondary=patient_enrolled_services
        )
    notifications = relationship(
        "NotificationModel",
        secondary=patient_notifications
        )  
    created = Column(DateTime, default=datetime.utcnow)
    def dict(self):
        return {
            'user_id': self.user_id,
            'patient_id': self.patient_id,
            'DOB': self.DOB,
            'gender': self.gender,
            'medical_history': self.medical_history,            
            'allergies': self.allergies,
            'consent_id': self.consent_id,
            'created': self.created          
             
        }



practitioner_schedules = Table(
    "practitioner_schedules",
    Base.metadata,
    Column("practitioner_id", String(50), ForeignKey("practitioners.practitioner_id")),
    Column("session_id", String(50), ForeignKey("therapy_sessions.session_id"))
)
practitioner_assigned_patients = Table(
    "practitioner_assigned_patients",
    Base.metadata,
    Column("practitioner_id", String(50), ForeignKey("practitioners.practitioner_id")),
    Column("patient_id", String(50), ForeignKey("patients.patient_id"))
)

practitioner_notifications = Table(
    "practitioner_notifications",
    Base.metadata,
    Column("practitioner_id", String(50), ForeignKey("practitioners.practitioner_id")),
    Column("notification_id", String(50), ForeignKey("notifications.notification_id"))
)
class PractitionerModel(Base):
    __tablename__ = 'practitioners'
    user_id = Column(String(50), ForeignKey("users.user_id"), unique=True)
    practitioner_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    DOB = Column(DateTime, nullable=False)
    gender = Column(String(50), nullable=False)
    specialization = Column(String(50), nullable=False)
    certification_number = Column(String(50), nullable=False,unique=True)
    verificationStatus = Column(String(50), nullable=False, default='pending')
    schedules = relationship(
        "TherapySessionModel",
        secondary=practitioner_schedules
        )
    assigned_patients = relationship(
        "PatientModel",
        secondary=practitioner_assigned_patients
        )
    notifications = relationship(
        "NotificationModel",
        secondary=practitioner_notifications
        )     
    created = Column(DateTime, default=datetime.utcnow)
    
    
    def dict(self):
        return {
            'user_id': self.user_id,
            'practitioner_id': self.practitioner_id,
            'DOB': self.DOB,
            'gender': self.gender,
            'specialization': self.specialization,            
            'certification_number': self.certification_number,
            'verificationStatus': self.verificationStatus,
            'created': self.created          
             
        }



class FoodItemModel(Base):
    __tablename__ = 'fooditems'
    food_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    portionSize = Column(String(50), nullable=False)
    calories = Column(Float(50), nullable=False)
    protein = Column(Float(50), nullable=False) 
    carbs = Column(Float(50), nullable=False) 
    fats = Column(Float(50), nullable=False) 
    vitamins = Column(Float(50), nullable=False)
    image_url = Column(String(50), nullable=True)       
    created = Column(DateTime, default=datetime.utcnow)
    
    def dict(self):
        return {
            'food_id': self.food_id,
            'name': self.name,
            'portionSize': self.portionSize,            
            'protein': self.protein,
            'carbs': self.carbs,
            'fats': self.fats,
            'vitamins': self.vitamins,
            'image_url': self.image_url,
            'created': self.created                      
        }

class DataModel(Base):
    __tablename__ = 'data'
    data_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    mealplan_id = Column(String(50), ForeignKey("mealplans.mealplan_id"), unique=False)
    day = Column(String(50), nullable=False)
    breakfast = Column(String(50), nullable=True)
    snack1 = Column(String(50), nullable=True)
    lunch = Column(String(50), nullable=True)
    snack2 = Column(String(50), nullable=True)
    dinner = Column(String(50), nullable=True)
    snack3 = Column(String(50), nullable=True)      
    created = Column(DateTime, default=datetime.utcnow)
    
    def dict(self):
        return {
            'data_id': self.data_id,
            'mealplan_id': self.mealplan_id,
            'day': self.day,            
            'breakfast': self.breakfast,
            'snack1': self.snack1,
            'lunch': self.lunch,
            'snack2': self.snack2,
            'dinner': self.dinner,
            'snack3': self.snack3,
            'created': self.created          
             
        }
mealplan_data = Table(
    "mealplan_data",
    Base.metadata,
    Column("mealplan_id", String(50), ForeignKey("mealplans.mealplan_id")),
    Column("data_id", String(50), ForeignKey("data.data_id"))
)         
class MealPlanModel(Base):
    __tablename__ = 'mealplans'
    mealplan_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(50), nullable=False)
    start_date =  Column(DateTime, nullable=False)
    end_date =  Column(DateTime, nullable=False)
    restrictions = Column(String(50), nullable=True)
    notes = Column(String(50), nullable=True)
    data = relationship(
        "DataModel",
        secondary=mealplan_data
        )       
    created = Column(DateTime, default=datetime.utcnow)
    
    def dict(self):
        return {
            'mealplan_id': self.mealplan_id,
            'title': self.title,
            'start_date': self.start_date,            
            'end_date': self.end_date,
            'restrictions': self.restrictions,
            'notes': self.notes,
            'created': self.created          
             
        }        


available_practitioner = Table(
    "service_available_specialist",
    Base.metadata,
    Column("service_id", String(50), ForeignKey("services.service_id")),
    Column("practitioner_id", String(50), ForeignKey("practitioners.practitioner_id"))
)
class ServiceModel(Base):
    __tablename__ = 'services'
    service_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    short_description = Column(String(100), nullable=False)
    long_description = Column(String(255), nullable=True)
    price = Column(Float(15), nullable=False)
    session_number = Column(Integer, nullable=False, default=1)
    category = Column(String(255), nullable=False)
    duration = Column(Integer, nullable=False, default=1)
    specialists = relationship(
        "PractitionerModel",
        secondary= available_practitioner
        )
    created = Column(DateTime, default=datetime.utcnow)
    
    def dict(self):
        return {
            'service_id': self.service_id,
            'name': self.name,
            'short_description': self.short_description,            
            'long_description': self.long_description,
            'price': self.price,
            'session_number': self.session_number,
            'category': self.category,
            'duration': self.duration,
            'created': self.created          
             
        }
        
        
class TherapySessionModel(Base):
    __tablename__ = 'therapy_sessions'
    
    session_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    service_id = Column(String(50), ForeignKey("services.service_id"), unique=True)
    title = Column(String(50), nullable=False)
    practitioner_id = Column(String(50), ForeignKey("practitioners.practitioner_id"))
    patient_id = Column(String(50), ForeignKey("patients.patient_id"),unique=True)
    session_datetime = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False) 
    status = Column(String(50), nullable=False, default='pending')
    clinical_notes = Column(String(50), nullable=True)
    created = Column(DateTime, default=datetime.utcnow)
    
    def dict(self):
        return {
            'session_id': self.session_id,
            'service_id': self.service_id,
            'title': self.title,
            'patient_id': self.patient_id,
            'practitioner_id': self.practitioner_id,
            'session_datetime': self.session_datetime,
            'duration': self.duration,            
            'status': self.status,
            'clinical_notes': self.clinical_notes,
            'created': self.created              
        }
        
                              
class NutritionAssessment(Base):
    __tablename__ = 'nutrition_assessments'
    assessment_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    service_id = Column(String(50), ForeignKey("services.service_id"))
    patient_id = Column(String(50), ForeignKey("patients.patient_id"))
    entry_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    weight =  Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    BMI  = Column(Float, nullable=True)
    bodyFatPercentage = Column(Float, nullable=True)
    bloodsugar = Column(Float, nullable=True)
    bloodpressure = Column(Float, nullable=True)      
    
    
    def dict(self):
        return {
            'assessment_id': self.assessment_id,
            'service_id': self.service_id,
            'patient_id': self.patient_id,            
            'entry_date': self.entry_date,
            'weight': self.weight,
            'height': self.height,
            'BMI': self.BMI,
            'bodyFatPercentage': self.bodyFatPercentage,
            'bloodsugar': self.bloodsugar,
            'bloodpressure': self.bloodpressure                      
        }
        

class HealtMetricModel(Base):
    __tablename__ = 'health_metrics'
    metric_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))    
    patient_id = Column(String(50), ForeignKey("patients.patient_id"))
    metricType = Column(String(50), nullable=False)
    value = Column(Integer, nullable=False)
    unit = Column(String(50), nullable=False)
    entry_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def dict(self):
        return {
            'metric_id': self.metric_id,
            'patient_id':self.patient_id, 
            'metricType':self.metricType, 
            'value':self.value, 
            'unit':self.unit, 
            'entry_date':self.entry_date, 
        }

class NotificationModel(Base):
    __tablename__ = 'notifications'
    notification_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    recipient_id = Column(String(50), ForeignKey("users.user_id"))
    priority = Column(String(50), nullable=False, default='low')
    channel = Column(String(50), nullable=False, default='in_app')
    messageBody =  Column(String(50), nullable=False)
    status =  Column(String(50), nullable=False, default='pending')
    scheduledTime = Column(Integer, nullable=False, default=10)
    created = Column(DateTime, default=datetime.utcnow)
    
    
    def dict(self):
        return {
            'notification_id': self.notification_id, 
            'recipient_id': self.recipient_id,
            'priority': self.priority,
            'channel': self.channel,
            'messageBody': self.messageBody,
            'status': self.status,
            'scheduledTime': self.scheduledTime,
            'created': self.created
        }

class ConsentModel(Base):
    __tablename__ = 'consents'
    consent_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    signed_date = Column(DateTime,  nullable=False, default=datetime.utcnow)
    version = Column(String(50), nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    digital_signature = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='pending')
    
    def dict(self):
        return {            
            'consent_id': self.consent_id,
            'signed_date': self.signed_date,
            'version': self.version,
            'expiry_date': self.expiry_date,
            'digital_signature': self.digital_signature,
            'status': self.status,            
        }
       

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    log_id =  Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(50), ForeignKey("users.user_id"), unique=True)
    actionType = Column(String(50), nullable=False)
    resource_id = Column(String(50), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False, default=datetime.timestamp)
    ipAddress = Column(String(50), nullable=False)
    changes = Column(String(50), nullable=False)
    
    def dict(self):
        return {            
            'log_id': self.log_id, 
            'user_id': self.user_id,
            'actionType': self.actionType,
            'resource_id': self.resource_id,
            'timestamp': self.timestamp,
            'ipAddress': self.ipAddress,                       
        }
   
    
        
        
          
        
        
