from pathlib import Path
from detector.parser import parse_event_log

def main():
    """Start the detector CLI and verify the log source exists"""
    log_file = Path("logs/events.jsonl")

    print("[*] Detector starting...")

    if not log_file.exists():
        print(f'[!] Log file not found: {log_file}')
        return

    print(f"[*] Found log file: {log_file}")

    events = parse_event_log(str(log_file))
    print(f"[*] Ready to parse events from the log.")

if __name__ == "__main__":
    main()