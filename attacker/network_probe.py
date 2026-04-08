from shared.schemas import Event

def run_network_probe():
    """Simulate a basic lab-only network probe event."""
    event = Event.create(
        source = "attacker",
        action = "network_probe",
        target = "127.0.01",
        status = "success",
        metadata = {
            "port": 80,
            "protocol": "tcp",
            "method": "simulated"
        }
    )

    return event