import os
from dotenv import load_dotenv

class codeService:
   def __init__(self):
    load_dotenv()
    self.code = os.environ.get('AUTH_HEADER').encode('utf-8')


   def get_code(self):
     return self.code

   def get_headers(self):
    headers = {
       'Content-Type': 'application/json',
       'Authorization': self.get_code(),
    }
    return headers
   
