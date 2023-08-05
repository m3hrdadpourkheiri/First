from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

"""برای کنترل خروجی استفاده می شود
همچنین در زمان پاسخ خودمان می توانیم استاتوس کد را مشخص کنیم
"""

app = FastAPI()


class UserIn(BaseModel):
    username:str
    email:str
    password:str 


class UserOut(BaseModel):
    username:str
    email:str


@app.get('/home/',response_model=UserOut,status_code=200)
def home(user:UserIn):
    if user.username == 'admin':
        #raise Exception('username cant be admin')  # این یک نوع اینترنال اررور است که فقط در ترمینال نمایش داده می شود
        raise HTTPException(detail="username cant be admin",status_code=400,) #برای ارسال خطا به طرف کاربر استفاده می شود
    return user



