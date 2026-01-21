def summary_report(entries, counts):
    return {
        "total_logs": len(entries),
        "by_level": counts
    }
