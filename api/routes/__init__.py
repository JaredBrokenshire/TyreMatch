from database import get_db_connection
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

## TODO: Remove this
@main.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 'TEST to TyreMatch!'")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({"message": result[0]})