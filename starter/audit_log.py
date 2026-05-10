class AuditLog:
    def __init__(self, logId, userId, actionType, resourceId, timestamp, ipAddress, changes):
        self.logId = logId
        self.userId = userId
        self.actionType = actionType
        self.resourceId = resourceId
        self.timestamp = timestamp
        self.ipAddress = ipAddress
        self.changes = {}
     
    def create_log(self):
        pass
    
    def filter_by_date(self,range):
        pass
    
    def export_to_csv(self):
        pass
    
    def get_history_for_resource(self):
        pass
        
        