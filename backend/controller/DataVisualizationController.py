from config import *
from model.GameQuestionModel import Question
from service.DataVisulization import *


@app.get('/gelAllusersMaxScore')
def getAllScore():
    return getAllUsersMaxScore()


@app.get('/gelAllusersMinTime')
def getAllTime():
    return getAllUsersMinTime()


@app.get('/getnoOfUsersinEachLevel')
def getAllLevelAndUsers():
    return getnoOfUsersinEachLevel()


@app.get('/getAverageScore')
def getAverageScore():
    return averageMaxScore()


@app.get('/getAverageMintime')
def getAverageMinTime():
    return averageMinTime()


@app.get('/getUserAllScores/{email}')
def getUserScore(email: str):
    return getAllScoresByEmail(email)


@app.get('/getUsersAllTime/{email}')
def getUserTime(email: str):
    return getAllTimeByEmail(email)

@app.get('/getAllUSersNameAndMail')
def getAllMail():
    return getAllUsersNameAndMail()
