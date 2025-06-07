import hashlib
import json

class Deduplicator:
    def __init__(self, db):
        self.db = db
    
    def normalize(self, data):
        """Convert to lowercase and strip whitespace"""
        if isinstance(data, dict):
            return {k: self.normalize(v) for k, v in data.items()}
        if isinstance(data, str):
            return data.strip().lower()
        return data
    
    def create_hash(self, data):
        """Generate MD5 hash of normalized data"""
        normalized = self.normalize(data)
        return hashlib.md5(json.dumps(normalized).encode()).hexdigest()
    
    def process(self, new_data):
        """Main workflow: check and add data"""
        data_hash = self.create_hash(new_data)
        
        if self.db.hash_exists(data_hash):
            return "DUPLICATE"
        
        self.db.add_entry(data_hash, new_data)
        return "ADDED"