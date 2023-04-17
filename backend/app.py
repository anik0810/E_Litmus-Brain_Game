import uvicorn

from config import *
from controller.UserController import *
from controller.QuestionController import *
from controller.DataVisualizationController import *

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5151)

