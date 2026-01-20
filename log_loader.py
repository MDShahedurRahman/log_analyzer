from config import LOG_FILE


def load_logs():
    with open(LOG_FILE, "r") as file:
        return file.readlines()
