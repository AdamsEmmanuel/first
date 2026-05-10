import requests
from random import randrange
pat1 =  {
    "user_id": "1309a199-f77c-4fab-b5b3-79865186d778",
    'DOB': '1988-02-04',
    'medical_history': 'Weight management', 
    #"fullname": "Kunle Okafor",
    #"email": "kunle@email.com",
    #"password": "85236910",
    #"role": "Role.patient",
    #"contact_info": "8045678901",
    #"created": "2026-05-04 10:42:30"
  }
pat1 = {
    "user_id": "1e6a9af3-143c-4746-8719-910659878c7b",
    "fullname": "john",
    "email": "john@coding.com",
    "password": "39823640",
    "role": "Role.patient",
    "contact_info": "9110203204",
    "created": "2026-05-04 10:42:25"
  }
pat1 =   {
    "user_id": "2f4253d6-f72a-47e0-ab0b-741600d2d526",
    "fullname": "Chiamaka Osei",
    "email": "chiamaka@email.com",
    "password": "53244278",
    "role": "Role.patient",
    "contact_info": "8012345678",
    "created": "2026-05-04 10:42:27"
  },

pat1 =   {
    "user_id": "71ba3e4f-a34f-43d1-b714-d7b7cbc2cc37",
    "fullname": "Biodun Fashola",
    "email": "biodun@email.com",
    "password": "85236910",
    "role": "Role.patient",
    "contact_info": "8023456789",
    "created": "2026-05-04 10:42:28"
  },
pat1 =   {
    "user_id": "a19f3ef5-696b-465b-8c3f-22b9f2ff48d3",
    "fullname": "Yeside Williams",
    "email": "yeside@email.com",
    "password": "77645438",
    "role": "Role.patient",
    "contact_info": "8056789012",
    "created": "2026-05-04 10:42:32"
  },
pat1 =   {
    "user_id": "df91b4fa-7497-4b88-8930-23cc3919aa6d",
    "fullname": "Temi Adebayo",
    "email": "temi@email.com",
    "password": "12846802",
    "role": "Role.patient",
    "contact_info": "8034567890",
    "created": "2026-05-04 10:42:29"
  }

user1 = {
    "user_id": "334d813f-aff2-4520-9923-6d1615022ce4",
    "fullname": "Dr. Adaeze Obi",
    "email": "chiamaka@email.com",
    "password": "81712298",
    "role": "Role.practitioner",
    "contact_info": "8098765432",
    "created": "2026-05-04 22:05:34"
  }

prac1 = { 
    #'fullname': "Dr. Adaeze Obi",
    #'email': "chiamaka@email.com",  
    #'password': str(randrange(10000000, 90000000, 135562)),
    #'contact_info':"08098765432",
    #'role': 'practitioner',
    'user_id': user1['user_id'],
    'DOB': "1991-05-01T10:00:00",
    'gender': 'female',
    'specialization' :"Herbal Medicine",
    'certification_number': str(randrange(10000000, 90000000, 135562))    
}

prac1 = {
    "user_id": "334d813f-aff2-4520-9923-6d1615022ce4",
    "practitioner_id": "92fb78e4-82c6-4b82-ad13-50f7d8aecd38",
    "DOB": "1991-05-01 10:00:00",
    "gender": "Gender.female",
    "specialization": "Herbal Medicine",
    "certification_number": "18540406",
    "verificationStatus": "pending",
    "created": "2026-05-04 22:53:34"
  }


request1 = requests.post(
   "http://localhost:8000/api/v1/practitioners", json=prac1)

print(request1.content)