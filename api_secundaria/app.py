from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Função Haversine
def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # raio da Terra em km

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c

    return distancia


@app.route('/distancia', methods=['GET'])
def distancia():
    try:
        lat1 = float(request.args.get('lat1'))
        lon1 = float(request.args.get('lon1'))
        lat2 = float(request.args.get('lat2'))
        lon2 = float(request.args.get('lon2'))

        resultado = calcular_distancia(lat1, lon1, lat2, lon2)

        return jsonify({
            "distancia_km": round(resultado, 2)
        })

    except Exception as e:
        return jsonify({
            "error": "Parâmetros inválidos",
            "details": str(e)
        }), 400


if __name__ == '__main__':
    app.run(port=5001, debug=True)