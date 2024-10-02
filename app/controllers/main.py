from flask import Blueprint, jsonify, request
from app.models.admin import Admin
from app import db
from sqlalchemy import text

main = Blueprint('main', __name__)

@main.route('/test-db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({'message': 'Database connection successful!'}), 200
    except Exception as e:
        return jsonify({'message': 'Database connection failed', 'error': str(e)}), 500

@main.route('/admins', methods=['GET'])
def get_admins():
    try:
        admins = Admin.query.all()
        return jsonify([
            {
                'id_admin': admin.id_admin,
                'username': admin.username,
                'password': admin.password  # Catatan: Menampilkan password tidak disarankan dalam praktik nyata
            }
            for admin in admins
        ]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/admin', methods=['POST'])
def add_admin():
    data = request.json
    new_admin = Admin(username=data['username'], password=data['password'])
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({'message': 'Admin added successfully'}), 201
