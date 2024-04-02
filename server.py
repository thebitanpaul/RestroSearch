from flask import Flask, request, jsonify

app = Flask(__name__)


restaurants = [
    {"name": "Italian Express", "latitude": 40.7128, "longitude": -74.0060, "cuisine": "Italian", "rating": 4.5},
    {"name": "Mexican Restro", "latitude": 34.0522, "longitude": -118.2437, "cuisine": "Mexican", "rating": 4.0},
    {"name": "Indian Cafe", "latitude": 51.5074, "longitude": -0.1278, "cuisine": "Indian", "rating": 4.8},
]

def haversine(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, sqrt, atan2

    R = 6371.0  

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1


    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance * 1000

@app.route('/search')
def search():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    radius = float(request.args.get('radius'))
    cuisine_type = request.args.get('cuisine_type')
    min_rating = float(request.args.get('min_rating'))

    results = []
    for restaurant in restaurants:
        distance = haversine(latitude, longitude, restaurant['latitude'], restaurant['longitude'])
        if distance <= radius and (not cuisine_type or cuisine_type.lower() in restaurant['cuisine'].lower()) and restaurant['rating'] >= min_rating:
            results.append(restaurant)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
