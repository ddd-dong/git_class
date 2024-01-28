import os
from dotenv import load_dotenv
path =  os.path.dirname(os.path.abspath(__file__))

load_dotenv(path+"/tst.env")

print(os.getenv("password"),os.getenv('token'))
print("good morning!!!")