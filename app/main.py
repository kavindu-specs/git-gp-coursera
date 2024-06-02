from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.endpoints import items
from app.core.db import startup_event

app = FastAPI()

app.add_event_handler("startup", startup_event)

# Include the router for item endpoints
app.include_router(items.router)

# Custom exception handlers can be added here
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={"message": "Validation error", "errors": exc.errors()})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)