from crewai import Agent

post_quantum_kyber_migrator = Agent(
    role="Post Quantum Kyber Migrator",
    goal="Deliver high-precision autonomous Post Quantum Kyber Migrator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
