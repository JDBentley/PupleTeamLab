# Purple Team Lab

A safe, educational cybersecurity project that simulates controlled attacker activity in a lab and detects that activity through structured logging and rule-based analysis.

## Overview

Purple Team Lab is a Python-based project with two connected parts:

- **Attacker side**: Generates controlled, lab-only events such as local reconnaissance and limited network probing against authorized targets.
- **Detector side**: reads structured logs, applies rule-based detections, and produces alerts and reports.

The goal of the project is to learn both offensive and defensive thinking while building software in a safe, professional, and explainable way.

## Why This Project Exists

This project is designed to help me practice:

- Python software design
- structured logging
- detection engineering
- cybersecurity analysis
- safe adversary emulation in a controlled lab
- professional GitHub project organization

It is intended to be both a learning project and a portfolio project tha demonstrates how attacker behavior can be modeled and how defenders can detect it.

## Scope

### In Scope
- structured event generation
- local system reconnaissance
- limited lab-only network probing against authorized targets
- JSON-based logging
- log parsing
- rule-based detection
- alert generation
- report generation

## Out of Scope
- malware
- persistance
- credential theft
- privilege escalation
- stealth or evasion features
- internet-wide scanning
- unauthorized access
- real C2 functionality

## Ethics and Safety

This project is for educational use in controlled enviroments only.

All testing is intended to be performed on systems I own or am explicitly authorized to use in a lab setting. This project is designed to demonstrate safe adversary emulation and defensive detection concepts, not to support unauthorized access or real-world abuse.

## Planned Structure

```text
purpleteamlab
├── attacker/
├── detector/
├── shared/
├── logs/
├── reports/
├── tests/
└── lab/
```

```md
- [x] Initialize repository structure
- [x] Define project scope and README
- [ ] Create shared event schema
- [ ] Build shared logger
- [ ] Add attacker recon module
- [ ] Add attacker network probe module
- [ ] Build detector parser
- [ ] Add first detection rule
- [ ] Generate alerts and reports
- [ ] Add tests
- [ ] Finalize documentation
```
