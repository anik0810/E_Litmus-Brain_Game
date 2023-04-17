from pydantic import BaseModel


class Question(BaseModel):
    questionNumber: int
    question: str
    photo: str | None = None
    ans: str
    hints: list
    noOfSolution: int
