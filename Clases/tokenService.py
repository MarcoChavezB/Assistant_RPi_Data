import os
from dotenv import load_dotenv

class tokenService:
   def __init__(self):
    load_dotenv()
    self.token = os.environ.get('AUTH_HEADER').encode('utf-8')


   def get_token(self):
     return self.token

   def get_headers(self):
    headers = {
       'Content-Type': 'application/json',
       'Authorization': self.get_token(),
    }
    return headers
   
