from pydantic import BaseModel


class UserBody(BaseModel):
    email: str
    password: str
    name: str
    level: int
    currentTime: list
    minTime: int
    currentScore: list
    highestScore: int
    maxLevel: int
