from log_entry import LogEntry


def parse_log_line(line):
    parts = line.strip().split(" ", 2)
    if len(parts) != 3:
        return None
    date, level, message = parts
    return LogEntry(date, level, message)
