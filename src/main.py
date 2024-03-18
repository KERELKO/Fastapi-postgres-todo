from fastapi import FastAPI


app = FastAPI()


@app.get('/test/')
async def first_func():
    return {'Hello': 'world!'}    

