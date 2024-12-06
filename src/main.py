from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return { "msg": "Hello, world!" }

@app.get("/api/v1/hello-world/"
def read_hello_world():
    return { "what": "road", "where", "kubernetes", "version": "v1" }
