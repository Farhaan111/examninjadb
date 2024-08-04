from urllib.parse import quote_plus
from pymongo import MongoClient
from datetime import datetime
username = "farrahman111"
password = "Magnetite@111"

# URL-encode the username and password





MONGO_URI = "mongodb+srv://farrahman111:root@samurai.6l3x38m.mongodb.net/"

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client.Examninja

# Create Users collection and insert sample document
users_collection = db.users
users_collection.insert_one({
    "_id": "user_johndoe",  # Using an alphanumeric string as the user ID
    "username": "johndoe",
    "password_hash": "hashed_password",
    
})

# Create Exams collection and insert sample document
exam_id = "exam_math_101"  # Using an alphanumeric string as the exam ID
exams_collection = db.exams
exams_collection.insert_one({
    "_id": exam_id,
    "title": "Math 101",
    "description": "Basic math exam",
    "start_time": datetime(2024, 8, 10, 10, 0, 0),
    "end_time": datetime(2024, 8, 10, 12, 0, 0),
    "questions": [
        {
            "question_id": "q1",
            "question_text": "What is 2 + 2?",
            "options": ["2", "3", "4", "5"],
            "correct_option": 2
        },
        {
            "question_id": "q2",
            "question_text": "What is 3 * 3?",
            "options": ["6", "7", "8", "9"],
            "correct_option": 3
        }
    ]
})

# Create ProctoringLogs collection and insert sample document
proctoring_logs_collection = db.proctoring_logs
proctoring_logs_collection.insert_one({
    "user_id": "user_johndoe",  # Reference the user by alphanumeric ID
    "exam_id": exam_id,         # Reference the exam by alphanumeric ID
    "event_type": "tab_switch",
    "event_time": datetime.now(),
    "details": {
        "previous_tab": "exam_page",
        "current_tab": "google_search"
    }
})

# Create Results collection and insert sample document
results_collection = db.results
results_collection.insert_one({
    "user_id": "user_johndoe",  # Reference the user by alphanumeric ID
    "exam_id": exam_id,         # Reference the exam by alphanumeric ID
    "score": 8,
    "answers": [
        {
            "question_id": "q1",  # Reference the question by alphanumeric ID
            "selected_option": 2
        },
        {
            "question_id": "q2",  # Reference the question by alphanumeric ID
            "selected_option": 3
        }
    ]
})


