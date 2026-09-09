from time import perf_counter

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest
from pydantic import BaseModel, Field

app = FastAPI(
    title="Cloud-Native Microservices Platform",
    version="1.0.0",
)

REQ = Counter(
    "http_requests_total",
    "HTTP requests",
    ["method", "path", "status"],
)

LAT = Histogram(
    "http_request_duration_seconds",
    "HTTP duration",
    ["method", "path"],
)

USERS = {}
NEXT_ID = 1


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class User(UserCreate):
    id: int


@app.middleware("http")
async def observe(request: Request, call_next):
    start = perf_counter()

    response = await call_next(request)
    path = request.url.path

    REQ.labels(
        request.method,
        path,
        str(response.status_code),
    ).inc()

    LAT.labels(
        request.method,
        path,
    ).observe(perf_counter() - start)

    return response


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/ready")
def ready():
    return {"status": "READY"}


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain",
    )


@app.post("/api/v1/users", response_model=User, status_code=201)
def create_user(payload: UserCreate):
    global NEXT_ID

    user = User(
        id=NEXT_ID,
        **payload.model_dump(),
    )

    USERS[NEXT_ID] = user
    NEXT_ID += 1

    return user


@app.get("/api/v1/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return USERS[user_id]
