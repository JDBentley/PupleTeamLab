from attacker.recon import run_recon
from shared.logger import write_event

def main():
    event = run_recon()
    write_event(event)
    print("[+] Recon event generated and logged.")


if __name__ == "__main__":
    main()