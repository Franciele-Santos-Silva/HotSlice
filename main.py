from fastapi import FastAPI

app = FastAPI();

from auth_routes import auth_routes
from order_routes import order_routes