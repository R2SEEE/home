from ninja import NinjaAPI
from orders.api import router as orders_router

api = NinjaAPI(title="My Shop API", version="1.0.0")

api.add_router("/orders", orders_router)