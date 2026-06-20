"""Example usage of Arts domain agents."""

from agents.arts import CreativityAssistant


def main():
    """Run arts domain example."""
    # Create creativity assistant for writing
    writing_assistant = CreativityAssistant(
        name="Writing Coach",
        art_form="Writing"
    )

    # Example creative queries
    queries = [
        "How can I develop compelling characters?",
        "What techniques can help overcome writer's block?",
        "How do I structure a short story effectively?"
    ]

    print("=" * 60)
    print("Arts Domain - Creativity Assistant Example")
    print("=" * 60)
    print(f"\nAgent: {writing_assistant.name}")
    print(f"Art Form: {writing_assistant.art_form}\n")

    # Process creative queries
    for query in queries:
        print(f"Creative Question: {query}")
        response = writing_assistant.process_query(query)
        print(f"{response}\n")

    # Generate creative prompts
    prompts = writing_assistant.suggest_prompts(count=3)
    print("Suggested Writing Prompts:")
    for i, prompt in enumerate(prompts, 1):
        print(f"  {i}. {prompt}")

    # Add artwork to portfolio
    writing_assistant.add_to_portfolio({
        "title": "My First Story",
        "type": "short story",
        "date": "2024-01-01"
    })

    print("\n" + "=" * 60)
    print("Agent Status")
    print("=" * 60)
    status = writing_assistant.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()