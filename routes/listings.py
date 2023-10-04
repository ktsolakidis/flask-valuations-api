from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('listings', __name__, url_prefix='/listings')

@bp.route('/new', methods=['POST'])
def create_listing():
    data = request.json
    student_id = data['student_id']
    class_id = data['class_id']
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO listings (student_id, class_id, date) VALUES (%s, %s, CURRENT_DATE())",
                   (student_id, class_id))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "New listing created"})

@bp.route('/all', methods=['GET'])
def get_all_listings():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM listings")
    listings = cursor.fetchall()
    cursor.close()
    return jsonify(listings)
