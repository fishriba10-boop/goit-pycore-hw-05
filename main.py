"""Task 3: log file analyzer.

Usage:
    python main.py /path/to/logfile.log
    python main.py /path/to/logfile.log error
"""

import sys
from collections import Counter

LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")


def parse_log_line(line: str) -> dict:
    """Split one log line into date, time, level and message.

    Raises ValueError if the line does not match the expected format.
    """
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        raise ValueError(f"Wrong log line format: {line.strip()!r}")

    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> list:
    """Read the log file and return a list of parsed log entries.

    Broken lines are skipped with a warning.
    """
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue  # skip empty lines
            try:
                logs.append(parse_log_line(line))
            except ValueError as error:
                print(f"Warning (line {line_number}): {error}")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Return only the log entries with the given level."""
    level = level.upper()
    # Functional style: filter + lambda
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    """Count how many entries there are for each log level."""
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict) -> None:
    """Print the counts as a table."""
    print(f"{'Рівень логування':<17}| Кількість")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
        sys.exit(1)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error: cannot read file '{file_path}': {error}")
        sys.exit(1)

    display_log_counts(count_logs_by_level(logs))

    # Optional second argument: show all entries of this level
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        if level not in LEVELS:
            print(f"\nUnknown level '{sys.argv[2]}'. Use one of: {', '.join(LEVELS)}")
            sys.exit(1)

        print(f"\nДеталі логів для рівня '{level}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
