from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379",
    default_limits=[]
)
def init_app(app):
    limiter.init_app(app)
