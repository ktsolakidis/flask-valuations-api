from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/new', methods=['POST'])
def create_student():
    data = request.json
    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    password = data['password']
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, username, password) VALUES (%s, %s, %s, %s)",
                   (first_name, last_name, username, password))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "New student created"})

@bp.route('/all', methods=['GET'])
def get_all_students():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    return jsonify(students)

@bp.route('/del/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": f"Student with id {id} deleted"})
