from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB container
client = MongoClient("mongodb://mongo-service:27017/")
db = client["moviesappdb"]
movies_collection = db["movies"]

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    user_id = data['user_id']
    movie = data['movie']
    movies_collection.insert_one({"user_id": user_id, "title": movie})
    return jsonify({"message": f"Movie '{movie}' added for user {user_id}"}), 201

@app.route('/movies/<user_id>', methods=['GET'])
def get_movies(user_id):
    movies = movies_collection.find({"user_id": user_id})
    movie_list = [m["title"] for m in movies]
    return jsonify({"movies": movie_list}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
