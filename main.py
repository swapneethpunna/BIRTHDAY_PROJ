from fastapi import FastAPI, status, Request, Form
from models.user import UserData
from fastapi.templating import Jinja2Templates 
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


app=FastAPI()

templates=Jinja2Templates(directory="html_templates/")

app.mount("/static",StaticFiles(directory="static"),name="static")

userData=[]


@app.post('/save_date_of_birth', tags=["Save Data"] )
def save_data(data: UserData):
    print(data)
    userData.append(data)
    print(userData)
    return {"user_data":userData}


@app.get('/', tags=["UI"] )
async def home(request: Request):
    
    return templates.TemplateResponse("form.html",{"request": request, "birthdays":userData})

@app.post('/save_form_data/', tags=["Save"])
async def save_data_response(name: str = Form(...), month: str = Form(...), day: str = Form(...)):
    print(name,month,day)

    data = UserData(name=name,month=month,day=day)
    print(data)
    userData.append(data)
    print(userData)
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

