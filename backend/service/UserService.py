from Connection import *

userCollection = database['userDetails']


def signUpUser(userDetails):
    try:
        existingUser = userCollection.find_one({"email": userDetails["email"]})
        if existingUser is None:
            userCollection.insert_one(userDetails)
            return userDetails
        else:
            return 'Already Have An Account !!'

    except:
        print('something went wrong')


def signInUser(email, password):
    try:
        existingUser = userCollection.find_one({"email": email})
        if existingUser is None:
            return 'You Have not Any Account !!'
        else:
            userDetails = userCollection.find_one({"email": email, "password": password})
            if userDetails is None:
                return 'invalid credential'
            else:
                return userDetails

    except:
        print('something went wrong')


def getUserDetailsByMail(email):
    try:
        existingUser = userCollection.find_one({"email": email})
        return existingUser
    except:
        return 'something went wrong'


def getNameByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return dict(existingUser)['name']


def getHighestScoreByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return existingUser['highestScore']


def getMinTimeByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return existingUser['minTime']


def getMaxLevelByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return existingUser['maxLevel'];


def updateLevel(email, level):
    query = ({"email": email})
    updatedLevel = {"$set": {"level": level}}
    userCollection.update_one(query, updatedLevel)
    updateMaxLevel(email, level)
    return userCollection.find_one(query)


def updateMaxLevel(email, level):
    query = ({"email": email})
    if getMaxLevelByEmail(email) < level:
        updatedLevel = {"$set": {"maxLevel": level}}
        userCollection.update_one(query, updatedLevel)
    return userCollection.find_one(query)


def updateScore(email, score):
    query = ({"email": email})
    updatedScore = {"$push": {"currentScore": score}}
    userCollection.update_one(query, updatedScore)
    updateHighestScore(email, score)
    return userCollection.find_one({"email": email})


def updateHighestScore(email, score):
    query = ({"email": email})
    if getHighestScoreByEmail(email) < score:
        updatedScore = {"$set": {"highestScore": score}}
        userCollection.update_one(query, updatedScore)
    return userCollection.find_one(query)


def updateTime(email, time):
    query = ({"email": email})
    updatedTime = {"$push": {"currentTime": time}}
    userCollection.update_one(query, updatedTime)
    updateMinTime(email, time)
    return userCollection.find_one({"email": email})


def updateMinTime(email, time):
    query = ({"email": email})
    if getMinTimeByEmail(email) > time:
        updatedTime = {"$set": {"minTime": time}}
        userCollection.update_one(query, updatedTime)
    return userCollection.find_one(query)


def getAllUsersScore():
    allUsers = userCollection.find({})
    nameAndScore = []
    for user in allUsers:
        nameAndScore.append([user['name'], user['highestScore']])

    nameAndScore = sorted(nameAndScore, key=lambda x: x[1], reverse=True)

    return nameAndScore


def updateAccuracy(email, accuracy):
    query = ({"email": email})
    updatedAccuracy = {"$set": {"accuracy": accuracy}}
    userCollection.update_one(query, updatedAccuracy)
    return userCollection.find_one(query)
