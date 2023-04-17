from config import *
from model.GameQuestionModel import Question
from service.QuestionService import *


@app.post('/addQuestion')
def addQuestiontoDb(question: Question):
    return addQuestion(question)


@app.get('/getQuestionByNumber/{number}')
def getQuestion(number: int):
    return getQuestionByNumber(number)


@app.post('/checkAns/{ans}/{num}')
def questionCheck(ans: str, num: int):
    return checkAns(ans, num)

@app.get('/getHints/{number}')
def getHintsByNumber(number:int):
    return getHints(number)
