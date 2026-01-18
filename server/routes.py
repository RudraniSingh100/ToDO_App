from flask import Blueprint, request, jsonify
from db import get_connection

routes = Blueprint('routes', __name__)

@routes.route('/todos', methods=['GET'])
def get_todos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return jsonify(todos)
# NOTE: Error handling omitted for simplicity

@routes.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json() or {}
    title = data['title']
    priority = data.get('priority', 'Medium')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title, priority) VALUES (%s, %s)",(title, priority))
    conn.commit()
    conn.close()
    return jsonify({"message": "Todo added"}), 201
# NOTE: Error handling omitted for simplicity

@routes.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json() or {}
    completed = data['completed']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET completed = %s WHERE id = %s", (completed, id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Todo updated"})
# NOTE: Error handling omitted for simplicity

@routes.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Todo deleted"})
# NOTE: Error handling omitted for simplicity
