# Log File Analyzer (CLI)

Log File Analyzer is a command-line Python application that reads,
parses, filters, and analyzes application log files.\
The project demonstrates clean modular design, clear separation of
concerns, and practical backend-style log processing using **Python's
standard library only**.

This project is suitable for learning, portfolio development, and
showcasing meaningful incremental Git commit history.

------------------------------------------------------------------------

## Features

-   Load log data from a text-based log file
-   Parse structured log entries
-   Filter logs by severity level and date
-   Count log occurrences by level
-   Generate and display a summary report in the terminal

------------------------------------------------------------------------

## Project Structure

    log_analyzer/
    │
    ├── main.py          # Application entry point
    ├── config.py        # Global configuration values
    ├── log_entry.py     # Log entry data model
    ├── log_loader.py    # Log file loading logic
    ├── log_parser.py    # Log parsing logic
    ├── log_filter.py    # Log filtering functions
    ├── analyzer.py      # Log analysis functions
    ├── report.py        # Report generation and output
    ├── utils.py         # Utility and validation helpers

------------------------------------------------------------------------

## Requirements

-   Python 3.8 or higher
-   No third-party dependencies

------------------------------------------------------------------------

## Log File Format

The application expects a log file named **`application.log`** in the
project root directory.

Each log entry must follow this format:

    YYYY-MM-DD LEVEL Message

### Example

    2026-01-10 INFO Application started
    2026-01-10 WARNING Low disk space
    2026-01-10 ERROR Database connection failed

------------------------------------------------------------------------

## How to Run

1.  Clone the repository:

    ``` bash
    git clone <repository-url>
    ```

2.  Navigate to the project directory:

    ``` bash
    cd log_analyzer
    ```

3.  Ensure `application.log` exists in the project root.

4.  Run the application:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

## Sample Output

    Log Summary Report
    ------------------
    Total Logs: 12
    INFO: 6
    WARNING: 4
    ERROR: 2

------------------------------------------------------------------------

## Design Goals

-   Keep functions small and focused
-   Enable easy testing and refactoring
-   Maintain readable and maintainable code
-   Support meaningful incremental Git commits

------------------------------------------------------------------------

## Potential Enhancements

-   Add unit tests
-   Support command-line arguments
-   Export reports to JSON or CSV
-   Integrate with cloud log sources (e.g., AWS CloudWatch)
-   Add time-range filtering

------------------------------------------------------------------------

## License

This project is intended for educational and demonstration purposes.
