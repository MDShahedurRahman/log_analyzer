def summary_report(entries, counts):
    return {
        "total_logs": len(entries),
        "by_level": counts
    }


def print_report(report):
    print("Log Summary Report")
    print("------------------")
    print(f"Total Logs: {report['total_logs']}")
    for level, count in report["by_level"].items():
        print(f"{level}: {count}")
