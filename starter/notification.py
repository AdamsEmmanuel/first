from enum import Enum
class Priority(Enum):
    low ='low'
    medium = 'medium'
    urgent = 'urgent'
 
class Status(Enum):
    pending = 'pending'
    sent = 'sent'
    read = 'read'
    failed = 'failed'
    
class Channel(Enum):
    email = 'email'
    sms ='sms'
    in_app = 'in_app'
         
class Notification:
    def __init__(self, notificationId, recipentId, priority, channel, messageBody, status ,scheduledTime):
        self.notificationId = notificationId
        self.recipentId = recipentId
        self.priority = Priority(priority)
        self.channel = Channel(channel)
        self.messageBody = messageBody
        self.status = Status(status)
        self.scheduledTime = scheduledTime
        
    def send(self):
        pass   
    
    def mark_as_read(self):
        pass
    
    def retry(self):
        pass
    
    def format_message(self,template):
        pass    
    
    