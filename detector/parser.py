import json
from pathlib import Path

def parse_event_log(log_file: str = "logs/events.jsonl"):
    path = Path(log_file)
    events = []

    with path.open("r", encoding = "utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            event = json.loads(line)
            events.append(event)

    return events