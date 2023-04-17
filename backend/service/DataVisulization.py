from Connection import *

userCollection = database['userDetails']


def getAllUsersMaxScore():
    allUsers = userCollection.find({})
    nameAndScore = []
    for user in allUsers:
        tempMap = {};
        tempMap['name'] = user['name']
        tempMap['maxScore'] = user['highestScore']
        nameAndScore.append(tempMap)
    return nameAndScore


def getAllUsersMinTime():
    allUsers = userCollection.find({})
    nameAndTime = []
    for user in allUsers:
        tempMap = {};
        tempMap['name'] = user['name']
        tempMap['minTime'] = user['minTime']
        nameAndTime.append(tempMap)
    return nameAndTime


def getnoOfUsersinEachLevel():
    allUsers = userCollection.find({})
    levelCount = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0
    }
    for user in allUsers:
        levelCount[user['maxLevel']] += 1
    return levelCount


def averageMaxScore():
    allUsers = userCollection.find({})
    totalScore = 0
    count=0
    for user in allUsers:
        count+=1
        totalScore += user['highestScore']
    return totalScore / count


def averageMinTime():
    allUsers = userCollection.find({})
    totalTime = 0
    count=0
    for user in allUsers:
        count+=1
        totalTime += user['minTime']
    return totalTime / count


def getAllScoresByEmail(email):
    user = userCollection.find_one({'email': email})
    list= user['currentScore']
    return list


def getAllTimeByEmail(email):
    user = userCollection.find_one({'email': email})
    return user['currentTime']

def getAllUsersNameAndMail():
    allUsers = userCollection.find({})
    nameAndMail = []
    for user in allUsers:
        tempMap = {'name': user['name'], 'email': user['email']};
        nameAndMail.append(tempMap)
    return nameAndMail