from flask import request, jsonify
from models import Alert, GenderDistribution, WeatherInfo
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from utils import get_weather_info

def init_routes(app, socketio):
    @app.route('/')
    async def home():
        return jsonify({"message": "Welcome to Women Safety Analytics Backend!"})

    @app.route('/alerts', methods=['POST'])
    async def create_alert():
        session = AsyncSessionLocal()
        data = request.json
        new_alert = Alert(message=data['message'], alert_type=data['alert_type'], data=data['data'])

        async with session:
            session.add(new_alert)
            await session.commit()
            socketio.emit('new_alert', {'message': data['message'], 'type': data['alert_type']})
            return jsonify({"message": "Alert created successfully!"}), 201

    @app.route('/alerts', methods=['GET'])
    async def get_alerts():
        session = AsyncSessionLocal()
        async with session:
            result = await session.execute(select(Alert))
            alerts = result.scalars().all()
            return jsonify([{"id": alert.id, "message": alert.message, "timestamp": alert.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "type": alert.alert_type, "data": alert.data} for alert in alerts])

    @app.route('/gender_distribution', methods=['POST'])
    async def update_gender_distribution():
        session = AsyncSessionLocal()
        data = request.json
        new_distribution = GenderDistribution(male_count=data['male_count'], female_count=data['female_count'])

        async with session:
            session.add(new_distribution)
            await session.commit()
            return jsonify({"message": "Gender distribution updated!"}), 201

    @app.route('/gender_distribution', methods=['GET'])
    async def get_gender_distribution():
        session = AsyncSessionLocal()
        async with session:
            result = await session.execute(select(GenderDistribution))
            distributions = result.scalars().all()
            return jsonify([{"id": dist.id, "male_count": dist.male_count, "female_count": dist.female_count, "timestamp": dist.timestamp.strftime("%Y-%m-%d %H:%M:%S")} for dist in distributions])

    @app.route('/weather', methods=['GET'])
    async def get_weather():
        weather_info = get_weather_info()
        session = AsyncSessionLocal()
        weather_entry = WeatherInfo(temperature=weather_info['temperature'], condition=weather_info['condition'])

        async with session:
            session.add(weather_entry)
            await session.commit()
            return jsonify(weather_info)
