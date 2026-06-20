"""Example usage of Agriculture domain agents."""

from agents.agriculture import CropAdvisor


def main():
    """Run agriculture domain example."""
    # Create crop advisor
    crop_advisor = CropAdvisor(
        name="Sustainable Farming Advisor"
    )

    # Example farming queries
    queries = [
        "What crops should I grow in clay soil?",
        "How can I reduce water usage in irrigation?",
        "What are the best practices for pest management?"
    ]

    print("=" * 60)
    print("Agriculture Domain - Crop Advisor Example")
    print("=" * 60)
    print(f"\nAgent: {crop_advisor.name}\n")

    # Process farming queries
    for query in queries:
        print(f"Farmer Question: {query}")
        response = crop_advisor.process_query(query)
        print(f"{response}\n")

    # Add crop information
    crop_advisor.add_crop_info("wheat", {
        "season": "winter",
        "water_needs": "moderate",
        "soil_type": "loamy",
        "yield": "high"
    })

    # Analyze soil
    soil_data = {
        "ph": 7.2,
        "nitrogen": "medium",
        "phosphorus": "low",
        "potassium": "high"
    }
    soil_analysis = crop_advisor.analyze_soil(soil_data)
    print(f"Soil Analysis Result: {soil_analysis}\n")

    # Print agent status
    print("\n" + "=" * 60)
    print("Agent Status")
    print("=" * 60)
    status = crop_advisor.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()