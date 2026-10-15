from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from service.users_services import UserService
import traceback

users_route = Blueprint('users_route', __name__)


@users_route.route("/crud")
def render_crud():
    users = UserService.get_all()
    return render_template('index.html', users=users)
    
@users_route.route("/user", methods=['GET'])
def get_all():
    try:
        
        users = UserService.get_all()
        
        return jsonify([
            user.to_dict()
            for user in users
        ])
        
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500
        
@users_route.route("/users/<string:username>", methods=['GET'])
def get_by_username(username):
    try:
        user = UserService.get_by_username(username)
        
        if not user:
            return jsonify({"message": "Nenhum usuário encontrado com esse username"}),404
        
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500
        
@users_route.route("/users/<int:id>", methods=['GET'])
def get_by_id(user_id):
    try:
        user = UserService.get_by_id(user_id)
        
        if not id:
            return jsonify({"message": "Nenhum usuário encontrado com esse id"}),404
        
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500
        
@users_route.route("/users", methods=['POST'])
def create():
    try:
        data = request.form
        
        create_user = UserService.create(data)
        
        return redirect(url_for('users_route.render_crud'))
        
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 400
        
@users_route.route("/users/<int:user_id>/delete", methods=['POST'])
def delete(user_id):
    try:
        UserService.delete(user_id)
        
        return redirect(url_for('users_route.render_crud'))
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": str(e)}), 400
    
    
@users_route.route("/update/<int:id>")
def render_update(id):
    users = UserService.get_by_id(id)
    return render_template('update.html', user=users)

    
@users_route.route("/users<int:id>", methods={'POST'})
def update(id):
    try:
        data = request.form
        
        UserService.update(data, id)
        
        return redirect(url_for('users_route.render_crud'))
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 400