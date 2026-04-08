from shared.schemas import Event
from attacker.config_loader import load_targets

def run_recon():
    # Simulates a basic reconnaissance action and returns an event.
    targets = load_targets()
    target = targets[0]["host"]
    
    event = Event.create(
        source = "attacker",
        action = "recon",
        target = "localhost",
        status = "success",
        metadata = {"method": "local"}
    )
    
    return event