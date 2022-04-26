from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_of_moons = num_of_moons
    
    
planets = [
    Planet(1, "Mercury", "Named after the Roman messenger god", None),
    Planet(2, "Venus", "Named after goddess of love and beauty", None),
    Planet(3, "Earth", "Named after the ground, root word ertha", 1),
    Planet(4, "Mars", "Named after the god of war", 2),
    Planet(5, "Jupiter", "Named after the supreme god the ancient Romans", 79),
    Planet(6, "Saturn", "Named after the king of the Titans", 82),
    Planet(7, "Uranus", "Named after the original Roman sky god", 27),
    Planet(8, "Neptune", "Named after the Roman god of the Sea", 14),
    ]


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


