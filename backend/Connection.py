from pymongo import MongoClient

try:
    client = MongoClient("mongodb://admin:password@ec2-65-0-74-234.ap-south-1.compute.amazonaws.com:27017")
    database = client['e_litmus']
    print('connection successfully')
except:
    print('connection fail')
