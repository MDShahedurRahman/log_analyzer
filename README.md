# log_analyzer
Overview

Log File Analyzer is a command-line Python application designed to read, parse, filter, and analyze application log files. The project demonstrates clean modular design, clear separation of concerns, and practical backend-style log processing using Python’s standard library only.

This project is intended for learning, portfolio development, and showcasing incremental Git commit history.


Features

Load log data from a text-based log file

Parse structured log entries

Filter logs by severity level and date

Count log occurrences by level

Generate and display a summary report in the terminal




Project Structure
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
