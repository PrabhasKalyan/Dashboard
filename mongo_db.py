# import json
# from pymongo import MongoClient
# client = MongoClient("mongodb+srv://prabhakalyan0473:mpks123456@cluster0.tkifbz6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# db= client["json_data"]
# collection = db["json_data_collection"]

# json_path = "jsondata.json"

# with open(json_path) as json_data:
#     data = json.load(json_data)


# collection.insert_many(data)


import os
import django

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")  # Update with your actual settings module
django.setup()  # Initialize Django

# Now import models
from dashboard1.models import Data

data = Data.objects.all()
print(data)




