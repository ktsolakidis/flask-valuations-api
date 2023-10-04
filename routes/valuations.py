from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('valuations', __name__, url_prefix='/valuations')

@bp.route('/new', methods=['POST'])
def create_valuation():
    data = request.json
    student_id = data['student_id']
    class_id = data['class_id']
    theory = data['theory']
    # ... (similar for other fields)
    cursor = db.connection.cursor()
    cursor.execute("""
        INSERT INTO valuations (student_id, class_id, date, theory, solved_excercises, methodology, pronunciation, data_translation, general_difficulty, other_difficulty, metadotikotita, preparation)
        VALUES (%s, %s, CURRENT_DATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (student_id, class_id, theory, solved_excercises, methodology, pronunciation, data_translation, general_difficulty, other_difficulty, metadotikotita, preparation))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "New valuation created"})

@bp.route('/all', methods=['GET'])
def get_all_valuations():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM valuations")
    valuations = cursor.fetchall()
    cursor.close()
    return jsonify(valuations)

@bp.route('/del/<int:id>', methods=['DELETE'])
def delete_valuation(id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM valuations WHERE id = %s", (id,))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": f"Valuation with id {id} deleted"})
