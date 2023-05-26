from fastapi import FastAPI

app = FastAPI(title ='NeedWork', docs_url='/work')

@app.get('/')
def home():
    return 'Hello dear work needers'

@app.get('/about')
def about():
    return {'data': 'This is about page'}