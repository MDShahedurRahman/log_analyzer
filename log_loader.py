from config import LOG_FILE


def load_logs():
    try:
        with open(LOG_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
