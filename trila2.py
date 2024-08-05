from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "mongodb+srv://farrahman111:root@samurai.6l3x38m.mongodb.net/"

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client.Examninja


users_collection = db.users
exams_collection = db.exams
proctoring_logs_collection = db.proctoring_logs
results_collection = db.results

# Add new user
new_user = {
    "_id": "user_janedoe",
    "username": "janedoe",
    "password_hash": "hashed_password",
    "room_code": "satty",
    "ban": False
}
users_collection.insert_one(new_user)
print("New user added successfully!")

# Add new exam
new_exam = {
    "_id": "exam_science_101",
    "title": "Science 101",
    "description": "Basic science exam",
    "start_time": datetime(2024, 8, 11, 10, 0, 0),
    "end_time": datetime(2024, 8, 11, 12, 0, 0),
    "questions": [
        {
            "question_id": "q3",
            "question_text": "What is H2O?",
            "options": ["Oxygen", "Hydrogen", "Water", "Helium"],
            "correct_option": 2
        },
        {
            "question_id": "q4",
            "question_text": "What is the boiling point of water?",
            "options": ["50°C", "75°C", "100°C", "125°C"],
            "correct_option": 2
        }
    ]
}
exams_collection.insert_one(new_exam)
print("New exam added successfully!")



# Add new result
new_result = {
    "user_id": "user_janedoe", 
    "exam_id": "exam_science_101",  
    "score": 9,
    "violations":0,
    "answers": [
        {
            "question_id": "q3", 
            "selected_option": 2
        },
        {
            "question_id": "q4", 
            "selected_option": 2
        }
    ]
}
results_collection.insert_one(new_result)
print("New result added successfully!")