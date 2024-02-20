from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import uvicorn


app = FastAPI()
app.mount('/static', StaticFiles(directory='todo/static'), name='static')
templates = Jinja2Templates(directory='todo/templates')


from todo.routers import home, update, delete



if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)



