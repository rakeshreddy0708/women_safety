from flask import Flask
from flask_socketio import SocketIO
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from models import Base
import asyncio
import eventlet
from sqlalchemy.ext.asyncio import AsyncSession 



app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app, async_mode='eventlet')

# Database setup
engine = create_async_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Initialize database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.before_first_request
def setup_database():
    asyncio.run(init_db())

from routes import init_routes
init_routes(app, socketio)
eventlet.monkey_patch()
if __name__ == '__main__':
    socketio.run(app, debug=True)
    app.run(host='0.0.0.0', port=5000)
