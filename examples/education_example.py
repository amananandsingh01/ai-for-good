"""Example usage of Education domain agents."""

from agents.education import TutoringAgent


def main():
    """Run education domain example."""
    # Create a tutoring agent
    math_tutor = TutoringAgent(
        name="Advanced Math Tutor",
        subject="Mathematics",
        level="High School"
    )

    # Example queries
    queries = [
        "How do I solve quadratic equations?",
        "What is the Pythagorean theorem?",
        "Explain calculus limits to me"
    ]

    print("=" * 60)
    print("Education Domain - Tutoring Agent Example")
    print("=" * 60)
    print(f"\nAgent: {math_tutor.name}")
    print(f"Subject: {math_tutor.subject}")
    print(f"Level: {math_tutor.level}\n")

    # Process queries
    for query in queries:
        print(f"Student: {query}")
        response = math_tutor.process_query(query)
        print(f"{response}\n")

    # Create student profile
    math_tutor.create_student_profile(
        student_id="STU001",
        name="John Doe",
        current_level="Grade 10"
    )

    # Print agent status
    print("\n" + "=" * 60)
    print("Agent Status")
    print("=" * 60)
    status = math_tutor.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()