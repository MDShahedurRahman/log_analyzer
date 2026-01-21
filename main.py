from log_loader import load_logs
from log_parser import parse_logs
from log_filter import filter_by_level
from analyzer import count_by_level
from report import summary_report, print_report


def main():
    lines = load_logs()
    entries = parse_logs(lines)
    error_entries = filter_by_level(entries, "ERROR")
    counts = count_by_level(entries)


if __name__ == "__main__":
    main()
