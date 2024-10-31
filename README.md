# Python Keylogger

A Python-based keylogger that captures and logs keystrokes to a specified file. Designed for educational purposes to help understand input tracking.

## Features

- Captures keystrokes and saves them to a log file.
- Configurable log file output and interval for logging.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Install the required packages:
   ```bash
   pip install keyboard
   ```

## Usage

Run the keylogger with the following command:
```bash
python keylogger.py -o <output-file> -i <interval>
```
- `-o` or `--outfile`: Specify the output file name (default is `keys.log`).
- `-i` or `--interval`: Set the interval (in seconds) for logging (default is 1).

## Example

To run the keylogger and save the log to `keys.txt`:
```bash
python keylogger.py -o keys.txt
```

## Disclaimer

This project is intended for educational purposes only. Use responsibly and with permission.
