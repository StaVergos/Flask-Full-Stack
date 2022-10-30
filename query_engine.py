from pymongo import MongoClient
from models.user_model import UserModel
from typing import List, Dict, Any


client = MongoClient('mongodb://localhost:27017')

db = client['flask-full-stack']
users_auth = db['users']


def db_create_user(user: MongoClient) -> bool:
    users_auth.insert_one(user.__dict__)


def db_update_book(user_id: str, book: Dict[str, Any]) -> bool:
    res = users_auth.update_one({"id": user_id}, {"$set": user})
    return res.modified_count > 0


def db_list_books() -> List[UserModel]:
    return [UserModel.from_dict(r) for r in users_auth.find()]


def db_retrieve_user(user_id: str) -> UserModel:
    _book = users_auth.find_one({"id": user_id})
    return UserModel.from_dict(_book) if _book else None


def db_delete_book(user_id: str) -> bool:
    res = users_auth.delete_one({"id": user_id})
    return res.deleted_count > 0
