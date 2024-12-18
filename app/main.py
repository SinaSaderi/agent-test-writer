from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a GET endpoint that returns 'Hello World'
@app.get("/")
async def read_root():
    """
    GET endpoint that returns a simple 'Hello World' message.
    """
    return {"message": "Hello World"}
```
