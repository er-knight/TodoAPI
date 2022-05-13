import uvicorn

if __name__ == "__main__":

    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True) 
    # default host : 127.0.0.1
    # default port : 8000
    # reload=True <=> debug=True (in Flask/Django) 
    # set reload=False while deploying

    # or run `uvicorn main:app --reload` in terminal
    # https://fastapi.tiangolo.com/tutorial/first-steps/
