from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional 

"""اعتبار سنجی پارامتر های ورودی 
https://docs.pydantic.dev/latest/usage/fields/
"""

app = FastAPI()


class Person(BaseModel):
    name:str
    age:int = Path(ge=0,le=100) #دراین مثال مدار بزرگترین و کوچکترین را برای این متغییر مشخص کردیم
    height:Optional[int]  = 0 

@app.get('/home/{name}/{age}')
def home(name:str,age:int = 10):

    return {'message': f'hello {name} your have {age} years old'}


@app.get('/index/{name}')
def index(name:str=Query('no name',max_length=30,min_length=3),age:int = 10):#در این مثال پس پارامتر هارا میتوان اعتبار سنجی کرد مثلا متغییر نیم مقدار پیشفرض دارد و باید مقدارش بین 3 تا 30 کاراکتر باشد 

    return {'message': f'hello {name} your have {age} years old'}

@app.post('/phome/')
def phome(prs:Person):
    return prs



