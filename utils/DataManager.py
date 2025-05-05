import json
from pymongo import MongoClient

import os


class DataManager:
    def __init__(self):
        self.user = {}
        self.version = "Test"
        self.client = MongoClient("mongodb://root:rootpwd@localhost:27017/")
        self.db = self.client[self.version]

    def check_if_exists(self, collection, code):
        return self.db[collection].count_documents({'user_id': code}, limit=1) != 0

    def save_data(self, collection: str, user_id: str, session_id: str, data: dict):

        if isinstance(data, list):
            # If the data is a list, let's wrap it in a dictionary under the key 'responses'
            data = {"tracks": data}

        elif not isinstance(data, dict):
            print("[Error][save_data] Invalid data type. Expected dictionary or list, got:", type(data))
            return False

        data['user_id'] = user_id
        data['session_id'] = session_id

        idx = self.db[collection].insert_one(data).inserted_id

        if idx is None:
            return False

        return True