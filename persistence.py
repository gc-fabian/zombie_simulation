import json
from building import Building
from simulation import Simulation

def save_state(simulation, filename="simulation_state.json"):
    state = {
        "turn": simulation.turn,
        "propagation_mode": simulation.propagation_mode,
        "building": {
            "floors": []
        }
    }
    for floor in simulation.building.floors:
        floor_dict = {"floor_number": floor.floor_number, "rooms": []}
        for room in floor.rooms:
            room_dict = {
                "room_number": room.room_number,
                "has_zombie": room.has_zombie,
                "sensor": room.sensor.status,
                "is_blocked": room.is_blocked
            }
            floor_dict["rooms"].append(room_dict)
        state["building"]["floors"].append(floor_dict)
    try:
        with open(filename, "w") as f:
            json.dump(state, f, indent=4)
        print(f"Estado guardado en '{filename}'.\n")
    except Exception as e:
        print(f"Error al guardar el estado: {e}\n")

def load_state(filename="simulation_state.json"):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
    except Exception as e:
        print(f"Error al cargar el estado: {e}\n")
        return None

    floors_data = state["building"]["floors"]
    floors_count = len(floors_data)
    rooms_per_floor = len(floors_data[0]["rooms"]) if floors_count > 0 else 0
    building = Building(floors_count, rooms_per_floor)
    for floor_data in floors_data:
        floor_number = floor_data["floor_number"]
        for room_data in floor_data["rooms"]:
            room_number = room_data["room_number"]
            room = building.get_room(floor_number, room_number)
            if room:
                room.has_zombie = room_data["has_zombie"]
                room.sensor.status = room_data["sensor"]
                room.is_blocked = room_data["is_blocked"]
    simulation = Simulation(
        building,
        propagation_mode=state.get("propagation_mode", "expansion"),
        turn=state.get("turn", 0)
    )
    print(f"Estado cargado desde '{filename}'.\n")
    return simulation
