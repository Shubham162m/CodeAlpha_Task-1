from database import Database
from deduplicator import Deduplicator

def main():
    db = Database()
    dedupe = Deduplicator(db)
    
    test_records = [
        {"name": "shubham", "email": "shubham@123.com"},
        {"name": "shubham", "email": "shubham@123.COM"},  
        {"name": "kishor", "email": "kishor@123.com"} 
    ]
    
    for record in test_records:
        result = dedupe.process(record)
        print(f"{record} -> {result}")
    
    print(f"\nFinal storage ({len(db.storage)} entries):")
    for entry in db.storage:
        print(entry["data"])

if __name__ == "__main__":
    main()