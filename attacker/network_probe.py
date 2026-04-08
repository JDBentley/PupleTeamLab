from shared.schemas import Event
from attacker.config_loader import load_targets

def run_network_probe():
    """Simulate a basic lab-only network probe event."""
    targets = load_targets()
    target = targets[1]["host"] # Loopback target from YAML config

    event = Event.create(
        source = "attacker",
        action = "network_probe",
        target = target,
        status = "success",
        metadata = {
            "port": 80,
            "protocol": "tcp",
            "method": "simulated"
        }
    )

    return event