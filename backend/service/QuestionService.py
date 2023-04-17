from Connection import *

questionCollection = database['gameQuestions']


def addQuestion(question):
    try:
        questionCollection.insert_one(dict(question))
        return True
    except:
        return False


def getQuestionByNumber(number):
    try:
        questionAndPhoto = []
        question = questionCollection.find_one({"questionNumber": number})
        questionAndPhoto.append(question['question'])
        questionAndPhoto.append(question['photo'])
        return questionAndPhoto
    except:
        return 'not found'


def checkAns(ans, questionNum):
    try:
        question = questionCollection.find_one({"questionNumber": questionNum})
        if ans.lower() == question['ans'].lower():
            return True
        else:
            return False
    except:
        return False


def getHints(questionNumber):
    question = questionCollection.find_one({"questionNumber": questionNumber})
    return question['hints']
