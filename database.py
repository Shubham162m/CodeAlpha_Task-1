class Database:
    def __init__(self):
        self.storage = []
    
    def add_entry(self, data_hash, content):
        self.storage.append({"hash": data_hash, "data": content})
    
    def hash_exists(self, data_hash):
        return any(entry["hash"] == data_hash for entry in self.storage)