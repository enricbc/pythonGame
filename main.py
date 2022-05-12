from flask import Flask, jsonify, request
import game_controller
from db import create_tables
from schemas import PlayerSchema

app = Flask(__name__)

player_schema = PlayerSchema()


@app.route('/startGame', methods=["GET"])
def start():
    var = game_controller.get_literal("startGame1")
    return var[0]


@app.route("/startGame", methods=["POST"])
def insert_player():
    data = request.get_json()
    player_details = player_schema.load(data)
    name = player_details["Name"]
    result = game_controller.insert_player(name)

    if not result:
        var = game_controller.get_literal("CreateUserError")
        return var[0]
    else:
        return "Usuario creado correctamente, para empezar el juego debes \n" \
               "realizar una petición al enpoint startGame con tu id de jugador\n" \
               "en un GET\n" \
               "\n" \
               "Tu Id de Jugador es: " + str(result)


@app.route('/startGame/<id>', methods=["POST"])
def start_game(id):
    player = game_controller.get_player_by_id(id)
    if player[1] == 1 and player[2] == 0:
        var = game_controller.get_literal("Stage1")
        return var[0]
    if player[1] == 1 and player[2] < 0 and player[2] < 4:
        return ""
    else:
        return "error"


@app.route('/players', methods=["GET"])
def get_player():
    player = game_controller.get_players()
    return jsonify(player)


@app.route("/doAction/<userId>/<actionId>", methods=["POST"])
def doAction(userId,actionId):
    player = game_controller.get_player_by_id(userId)

    if player[1] == 1:
        if int(actionId) == 1:
            game_controller.update_action_stage(int(actionId), player[1]+1, userId)
            var = game_controller.get_literal("s1o1")
            return var[0]
        if int(actionId) == 2:
            game_controller.update_action_stage(int(actionId), player[1]+1, userId)
            var = game_controller.get_literal("s1o2")
            return var[0]
        if int(actionId) == 3:
            game_controller.update_action_stage(int(actionId), player[1]+1, userId)
            var = game_controller.get_literal("s1o3")
            return var[0]
        else:
            "No trolees al juego"

    if player[1] == 2:
        if player[2] == 1:#casa petunia
            if int(actionId) == 1:
                game_controller.update_action_stage(int(actionId), player[1] + 1, userId)
                var = game_controller.get_literal("s1o1_s2o1")
                return var[0]
            if int(actionId) == 2:
                game_controller.update_action_stage(int(actionId), player[1] + 1, userId)
                var = game_controller.get_literal("s1o1_s2o2")
                return var[0]
            if int(actionId) == 3:
                game_controller.update_action_stage(int(actionId), player[1] + 1, userId)
                var = game_controller.get_literal("s1o1_s2o3")
                return var[0]
            else:
                "No trolees al juego"
        if player[2] == 2:#edificio
            if player[2] == 1:
                if int(actionId) == 1:
                    game_controller.update_action_stage(int(actionId), player[1] + 1, userId)
                    var = game_controller.get_literal("s1o2_s2o1")
                    return var[0]
                if int(actionId) == 2:
                    game_controller.update_action_stage(int(actionId), player[1] + 1, userId)
                    var = game_controller.get_literal("s1o2_s2o2")
                    return var[0]
                if int(actionId) == 3:
                    game_controller.update_action_stage(int(actionId), player[1] + 1, userId)
                    var = game_controller.get_literal("s1o2_s2o3")
                    return var[0]
                else:
                    "No trolees al juego"
        if player[2] == 3:#muerto
            return "Estas muerto no puedes seguir"
    if player[1] == 3:
        return "Tu juego ha finalizado"
    else:
        "No trolees al juego"


if __name__ == "__main__":
    create_tables()

    app.run(host='0.0.0.0', port=8000, debug=False)
