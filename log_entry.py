class LogEntry:
    def __init__(self, date, level, message):
        self.date = date
        self.level = level
        self.message = message

    def to_dict(self):
        return {
            "date": self.date,
            "level": self.level,
            "message": self.message
        }
