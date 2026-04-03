import json
from pathlib import Path

from shared.schemas import Event

def write_event(event: Event, log_file: str = "logs/events.jsonl") -> None:
    # Writes structured event to a JSON log file
    path = Path(log_file)
    path.parent.mkdir(parents = True, exist_ok = True)

    with path.open("a", encoding = "utf-8") as file:
        json.dump(event.to_dict(), file)
        file.write("\n")