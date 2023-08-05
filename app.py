from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 



app = FastAPI()


class Person(BaseModel):
    name:str
    age:int
    height:Optional[int]  = 0 #این پارامتر آپشنال است 

#path parameter
#http://127.0.0.1:8000/home/mehrdad/12
@app.get('/home/{name}/{age}')
def home(name:str,age:int = 10):

    return {'message': f'hello {name} your have {age} years old'}


#query parameter
#http://127.0.0.1:8000/index/mehrdad?age=30
#age:int = 10 این مدل پارامتر اجباری نیست
@app.get('/index/{name}')
def index(name:str,age:int = 10):

    return {'message': f'hello {name} your have {age} years old'}

#در این حالت پارامتر ها در قالب کلاس با قالب json ارسال می شوند
@app.post('/phome/')
def phome(prs:Person):
    return prs



