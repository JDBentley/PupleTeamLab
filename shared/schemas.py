from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

@dataclass
class Event:
    timestamp: str
    source: str
    action: str
    target: str
    status: str
    metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return{
            "timestamp": self.timestamp,
            "source": self.source,
            "action": self.action,
            "target": self.target,
            "status": self.status,
            "metadata": self.metadata
        }