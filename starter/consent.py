class Consent:
    def __init__(self, consentId, signed_date, version, expiry_date, digital_signature, status):
        self.consentId = consentId
        self.signed_date = signed_date
        self.version = version
        self.expiry_date = expiry_date
        self.digital_signature = digital_signature
        self.status = status
     
    def isValid(self):
        pass
    
    def grant(self,version):
        pass
    
    def revoke(self):
        pass
    
    def renew(self):
        pass
    
    def getAuditTrail(self):
        pass    
        