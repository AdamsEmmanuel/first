from uuid import UUID
import requests
import  datetime
from random import randrange
password = randrange(1, 90000000, 10000000)

prac1 = { 
    #'fullname': "Dr. Adaeze Obi",
    #'email': "chiamaka@email.com",  
    #'password': str(randrange(10000000, 90000000, 135562)),
    #'contact_info':"08098765432",
    #'role': 'practitioner',
    'DOB': "1991-05-01T10:00:00",
    'gender': 'female',
    'specialization' :"Herbal Medicine",
    'certification_number': str(randrange(10000000, 90000000, 135562))    
}


prac2 = { 
    #'fullname': "Funmi Adeyemi",
    #'password': str(randrange(10000000, 90000000, 135562)),
    #'contact_info':"08098765432",
    #'role': 'practitioner',
    'DOB': "1991-05-01T10:00:00",
    'gender': 'female',
    'specialization' :"Nutrition Therapist",
    'certification_number': str(randrange(10000000, 90000000, 135562)),
             
}

prac3 = { 
    #'fullname': "Ngozi Afolabi",
    #'password': str(randrange(10000000, 90000000, 135562)),
    #'contact_info':"08098765432",
    #'role': 'practitioner',
    'DOB': "1991-05-01T10:00:00",
    'gender': 'male',
    'specialization' :"Life Coach",
    'certification_number': str(randrange(10000000, 90000000, 135562)),
             
}

prac4 = { 
    #'fullname': "Emeka Nwosu",
    #'password': str(randrange(10000000, 90000000, 135562)),
    #'contact_info':"08098765432",
    #'role': 'practitioner',
    'DOB': "1991-05-01T10:00:00",
    'gender': 'male',
    'specialization' :"Wellness Coach",
    'certification_number': str(randrange(10000000, 90000000, 135562)),     
}

prac5 = { 
    #'fullname': "Shade Bello",
    #'password': str(randrange(10000000, 90000000, 135562)),
    #'contact_info':"08098765432",
    #'role': 'practitioner',
    'DOB': "1991-05-01T10:00:00",
    'gender': 'female',
    'specialization' :"Physiotherapist",
    'certification_number': str(randrange(10000000, 90000000, 135562)),    
}


request1 = requests.post(
   "http://localhost:8000/api/v1/practitioners", json=prac1)
request2 = requests.post(
  "http://localhost:8000/api/v1/practitioners", json= prac2)
request3 = requests.post(
  "http://localhost:8000/api/v1/practitioners", json= prac3)
request4 = requests.post(
  "http://localhost:8000/api/v1/practitioners", json= prac4)
request5 = requests.post(
   "http://localhost:8000/api/v1/practitioners", json= prac5)



#user1 = {
#  'fullname': 'john',
#  'email': 'john@coding.com',
#  'contact_info': '09110203204',
#  'password': str(randrange(10000000, 90000000, 135562)),
#  'role': 'patient',
#    
#}
#
#user2 = {
#    'fullname':"Chiamaka Osei",    
#    'contact_info':"08012345678",
#    'email': "chiamaka@email.com",  
#    'password': str(randrange(10000000, 90000000, 135562)),
#    'role': 'patient',
#    
#}
#user3 = { 
#    'fullname' :"Biodun Fashola",
#    'contact_info': "08023456789",
#    'email': "biodun@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#    'role': 'patient',
#      
#}
#
#user4 ={ 
#    'fullname' :"Temi Adebayo",
#    'contact_info': "08034567890",
#    'email': "temi@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#  'role': 'patient',
#      
#}
#
#user5 = { 
#    'fullname' :"Kunle Okafor",
#    'contact_info': "08045678901",
#    'email': "kunle@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#  'role': 'patient',
#      
#}
#
#user6 = { 
#    'fullname' :"Yeside Williams",
#    'contact_info': "08056789012",
#    'email': "yeside@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#  'role': 'patient',
#     
#}
#
#user7 = { 
#    'fullname' :"Rotimi Bello",
#    'contact_info': "08067890123",
#    'email': "rotimi@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#  'role': 'patient',
#         
#}
#
#user8 = { 
#    'fullname' :"Adunola Martins",
#    'contact_info': "08078901234",
#    'email': "adunola@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#    'role': 'patient'
#  
#}
#
# 
#user9 = {
#    'fullname' :"Segun Okonkwo",
#    'contact_info': "08089012345",
#    'email': "segun@email.com",
#    'password': str(randrange(10000000, 90000000, 135562)),
#  'role': 'patient'
#      
#}
#
#
#
#
#request1 = requests.post(
#   "http://localhost:8000/api/v1/users", json=user1)
#request2 = requests.post(
#  "http://localhost:8000/api/v1/users", json= user2)
#request3 = requests.post(
#  "http://localhost:8000/api/v1/users", json= user3)
#request4 = requests.post(
#  "http://localhost:8000/api/v1/users", json= user4)
#request5 = requests.post(
#   "http://localhost:8000/api/v1/users", json= user5)
#
#request6 = requests.post(f"http://localhost:8000/api/v1/users", json=user6)
#
##request7 = requests.get(f"http://localhost:8000/api/v1/users/")
#
print(request1.content)
print(request2.content)
print(request3.content)
print(request4.content)
print(request5.content)
#print(request6.json)
#