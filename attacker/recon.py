from shared.schemas import Event

def run_recon():
    # Simulates a basic reconnaissance action and returns an event.
    event = Event.create(
        source = "attacker",
        action = "recon",
        target = "localhost",
        status = "success",
        metadata = {"method": "local"}
    )
    
    return event