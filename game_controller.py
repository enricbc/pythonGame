from db import get_db


def insert_player(name):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO player(Name) VALUES (?)"
    cursor.execute(statement, [name])
    db.commit()
    return cursor.lastrowid


def update_action_stage(action, stage, playerId):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE player SET Action = ?, Stage = ? WHERE Id = ?"
    cursor.execute(statement, [action, stage, playerId])
    db.commit()


def get_player_by_id(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT Name, Stage, Action FROM player WHERE id = ?"
    cursor.execute(query, [id])
    player = cursor.fetchone()
    return player


def get_players():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT Name FROM Player"
    cursor.execute(query)
    return cursor.fetchall()


def get_player(name):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT Name FROM Player WHERE Name = ?"
    cursor.execute(query)
    return cursor.fetchone()


def get_literal(name):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT data FROM literals WHERE Name = ?"
    cursor.execute(query, [name])
    return cursor.fetchone()
