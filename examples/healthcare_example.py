"""Example usage of Healthcare domain agents."""

from agents.healthcare import DiagnosisAssistant


def main():
    """Run healthcare domain example."""
    # Create diagnosis assistant
    health_assistant = DiagnosisAssistant(
        name="Health Information Assistant"
    )

    # Example health queries
    queries = [
        "I have a persistent cough",
        "What should I do about high blood pressure?",
        "I'm experiencing fatigue and headaches"
    ]

    print("=" * 60)
    print("Healthcare Domain - Diagnosis Assistant Example")
    print("=" * 60)
    print(f"\nAgent: {health_assistant.name}\n")

    # Process health queries
    for query in queries:
        print(f"Patient Query: {query}")
        response = health_assistant.process_query(query)
        print(f"{response}\n")

    # Add symptom information
    health_assistant.add_symptom("cough", ["Common Cold", "Flu", "Bronchitis"])
    health_assistant.add_symptom("fever", ["Flu", "Infection", "Inflammation"])

    # Print agent status
    print("\n" + "=" * 60)
    print("Agent Status")
    print("=" * 60)
    status = health_assistant.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")

    print("\n⚠️  DISCLAIMER: This is informational only. Always consult with")
    print("a licensed healthcare provider for diagnosis and treatment.")


if __name__ == "__main__":
    main()