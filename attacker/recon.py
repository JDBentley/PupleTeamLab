from shared.schemas import Event

def run_recon():
    event = Event.create(
        source = "attacker",
        action = "recon",
        target = "localhost",
        status = "success",
        metadata = {"method": "local"}
    )
    
    return event