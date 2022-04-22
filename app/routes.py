from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_of_moons = num_of_moons
    
    
planets = [
    Planet(1, "Earth", "", 1),
    Planet(2, "Jupiter", "", 79),
    Planet(3, "Neptune", "", 14),
    Planet(4, "Mars", "", 2),
    Planet(5, "Mercury", "", None),
    Planet(6, "Saturn", "", 82),
    Planet(7, "Uranus", "", 27),
    Planet(8, "Venus", "", None),
    Planet(9, "Pluto", "", 5)
    ]
#print(planets)

planets_bp = Blueprint("planets", __name__, url_prefix='/planets')

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "num_of_moons": planet.num_of_moons
        })
    return jsonify(planets_response)

print("Hello Sorida this is Nish")  
print("Hello Nish this is Sorida")