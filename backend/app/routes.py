from flask import Blueprint, jsonify, request
from app.models import BlogPost, db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/posts", methods=["GET"])
def get_posts():
    posts = BlogPost.query.all()
    return jsonify([{"id": post.id, "title": post.title, "content": post.content} for post in posts])

@api_blueprint.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    new_post = BlogPost(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created"}), 201
