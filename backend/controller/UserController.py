from config import *
from model.UserModel import UserBody
from service.UserService import *

from bson import json_util
import json


@app.post('/signUp')
def signIn(userBody: UserBody):
    response = signUpUser(dict(userBody))
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.post('/signIn/{email}/{password}')
def signIn(email: str, password: str):
    response = signInUser(email, password)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.get('/getUserDetailsByEmail/{email}')
def signIn(email: str):
    response = getUserDetailsByMail(email)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.get('/getName')
def getName(email):
    return getNameByEmail(email)


@app.get('/getHighestScore')
def getScore(email):
    return getHighestScoreByEmail(email)


@app.get('/getMinTime')
def getScore(email):
    return getMinTimeByEmail(email)


@app.get('/gelAllusersScore')
def getAllScore():
    return getAllUsersScore()


@app.put('/updateLevel/{email}/{level}')
def updateGameLevel(email: str, level: int):
    response = updateLevel(email, level)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.put('/addScore/{email}/{score}')
def updateUserScore(email: str, score: int):
    response = updateScore(email, score)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.put('/addTime/{email}/{time}')
def addTime(email: str, time: int):
    response = updateTime(email, time)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.put('/updateAccuracy/{email}/{accuracy}')
def addTime(email: str, accuracy: int):
    response = updateAccuracy(email, accuracy)
    json_response = json.loads(json_util.dumps(response))
    return json_response
