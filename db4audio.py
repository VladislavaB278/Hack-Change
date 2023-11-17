from fastapi import FastAPI

local_server = FastAPI()

@local_server.get('/')
def hello():
    return {'Status' : 200}

def main():
    hello()

if __name__ == '__main__':
    main()

import uvicorn 

uvicorn.run("db4audio:local_server", host = '127.0.0.1', port = 8000)