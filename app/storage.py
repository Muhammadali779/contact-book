import json

class Storage:
    def __init__(self, filename="contacts.json"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
