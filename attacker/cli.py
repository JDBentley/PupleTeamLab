from attacker.recon import run_recon
from attacker.network_probe import run_network_probe
from shared.logger import write_event

def main():
    print("Select an action: ")
    print("1. Recon")
    print("2. Network Probe")

    choice = input("Enter choice:").strip()

    if choice == "1":
        event = run_recon()
    elif choice == "2":
        event = run_network_probe()
    else:
        print("Invalid choice.")
        return
    
    write_event(event)
    print(f"[+]{event.action} Event generated and logged.")


if __name__ == "__main__":
    main()