from shared.schemas import Event
from shared.logger import write_event

def run_recon():
    event = Event.create(
        source="attacker",
        action="recon",
        target="localhost",
        status="success",
        metadata={"method" : "local"}
    )

    write_event(event)
    print('[+] Recon event generated and logged.')

if __name__ == "__main__":
    run_recon()