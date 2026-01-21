def count_by_level(entries):
    counts = {}
    for e in entries:
        counts[e.level] = counts.get(e.level, 0) + 1
    return counts


def count_errors(entries):
    return len([e for e in entries if e.level == "ERROR"])
