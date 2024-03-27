from pymongo.collection import Collection


class UsersDB(Collection):

    def exist(self, user_id):
        return bool(self.find_one({
            "id": user_id
        }))

    def registrate(self, user_id):
        self.insert_one({
            "id": user_id
        })

    def get_records(self):
        return [
            user["id"]
            for user
            in self.find()
        ]