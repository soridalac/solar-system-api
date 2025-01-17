from crypt import methods
from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix='/planets')

# class Planet:
#     def __init__(self, id, name, description, num_of_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_of_moons = num_of_moons
    
    
# planets = [
#     Planet(1, "Mercury", "Named after the Roman messenger god", None),
#     Planet(2, "Venus", "Named after goddess of love and beauty", None),
#     Planet(3, "Earth", "Named after the ground, root word ertha", 1),
#     Planet(4, "Mars", "Named after the god of war", 2),
#     Planet(5, "Jupiter", "Named after the supreme god the ancient Romans", 79),
#     Planet(6, "Saturn", "Named after the king of the Titans", 82),
#     Planet(7, "Uranus", "Named after the original Roman sky god", 27),
#     Planet(8, "Neptune", "Named after the Roman god of the Sea", 14),
#     ]

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or "num_moons" not in request_body:
        return make_response("invalid request", 400)

    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        num_moons = request_body["num_moons"]
    )

    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"Planet {new_planet.name} successfully created", 201)





@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planet_query = request.args

    if "name" in planet_query:
        planets = Planet.query.filter_by(name=planet_query["name"])
    elif "description" in planet_query:
        planets = Planet.query.filter_by(description=planet_query["description"])
    elif "num_moons" in planet_query:
        planets = Planet.query.filter_by(num_moons=planet_query["num_moons"])
    else:
        planets = Planet.query.all()


    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "num_moons": planet.num_moons
        })
    return jsonify(planets_response)



"""helper Function"""
# def validated_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response{"message":f"Planet {planet_id} is an invalid entry; must be a valid planet id"}, 400))
    

#     planet = Planet.query.get(planet_id)

#     if planet is None:
#         abort(make_response({"message":f"Planet {planet_id} not found"}, 404))

#     return planet

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except TypeError:
        return jsonify({"message":f"Planet {planet_id} is an invalid entry; must be a valid planet id"}), 400

    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify({"message":f"Planet {planet_id} not found"}), 404


    
        # if record.id.lower() == planet_id.lower():
            # return {
            #     "id": record.id,
            #     "name": record.name,
            #     "description": record.description,
            #     "num_moons": record.num_of_moons
            # } 
    return jsonify({"id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_moons": planet.num_moons})


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"message":f"Planet {planet_id} is an invalid entry; must be a valid planet id"}), 400

    request_body = request.get_json()
    
    if "name" not in request_body or "description" not in request_body or  "num_moons" not in request_body:
        return jsonify({'msg': f'Must include name , description and num moons'}), 400

    planet = Planet.query.get(planet_id)

    
   

    if planet is None:
        return jsonify({"message":f"Planet {planet_id} not found"}), 404

    

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.num_moons = request_body["num_moons"]

    db.session.commit()

    return jsonify({'msg': f'Successfully updated planet {planet.id}'}), 200


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"message":f"Planet {planet_id} is an invalid entry; must be a valid planet id"}), 400


    planet = Planet.query.get(planet_id)

    
   

    if planet is None:
        return jsonify({"message":f"Planet {planet_id} not found"}), 404

    db.session.delete(planet)
    db.session.commit()

    return jsonify({'msg': f"planet {planet.id} successfully deleted"})