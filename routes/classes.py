from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('classes', __name__, url_prefix='/classes')

@bp.route('/new', methods=['POST'])
def create_class():
    data = request.json
    name = data['name']
    category = data['category']
    grade = data['grade']
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO classes (name, category, grade) VALUES (%s, %s, %s)",
                   (name, category, grade))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "New class created"})

@bp.route('/all', methods=['GET'])
def get_all_classes():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()
    cursor.close()
    return jsonify(classes)

@bp.route('/del/<int:id>', methods=['DELETE'])
def delete_class(id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM classes WHERE id = %s", (id,))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": f"Class with id {id} deleted"})
