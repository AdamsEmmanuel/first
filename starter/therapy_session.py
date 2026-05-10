from enum import Enum

class Status(Enum):
    pending = 'pending'
    scheduled = 'scheduled'
    completed = 'completed'
    cancelled = 'cancelled'
    
    
class TherapySession:
    def __init__(self, sessionId, type, datetime, duration, notes,status):
        self.sessioId = sessionId
        self.type = type
        self.datetime = datetime
        self.duration = duration
        self.notes = notes
        self.status = Status(status)
    
    def schedule(self):
        pass
        
    def reschedule(self,details):
        pass
    
    def cancel(self):
        pass
    
    def log_outcome(self):
        pass
        