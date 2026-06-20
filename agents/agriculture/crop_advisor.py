"""Crop advisor agent for sustainable agriculture."""

from typing import Optional, Dict, Any
from agents.core import BaseAgent


class CropAdvisor(BaseAgent):
    """Agent providing agricultural advisory for sustainable farming."""

    def __init__(self, name: str = "Crop Advisor"):
        """
        Initialize crop advisor agent.

        Args:
            name: Name of the advisor
        """
        super().__init__(
            name=name,
            description="Provides crop management and sustainable farming advice",
            domain="agriculture"
        )
        self.crop_database = {}
        self.soil_info = {}

    def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process farming query and provide agricultural advice.

        Args:
            query: Farmer's question about crops or farming practices
            context: Optional context like location, crop type, soil type, etc.

        Returns:
            Agricultural advice and recommendations
        """
        self.log_interaction(query, "response")

        response = f"""
        Agricultural Advisory:
        
        Farmer Query: {query}
        
        Recommendations include:
        1. Crop selection based on local conditions
        2. Soil preparation and management
        3. Pest and disease control strategies
        4. Sustainable farming practices
        5. Yield optimization techniques
        6. Irrigation and water management
        7. Market and economic considerations
        """
        return response

    def add_crop_info(self, crop_name: str, crop_data: Dict[str, Any]) -> None:
        """Add crop information to database."""
        self.crop_database[crop_name.lower()] = crop_data

    def analyze_soil(self, soil_sample: Dict[str, Any]) -> str:
        """Analyze soil properties and provide recommendations."""
        return "Soil analysis in progress..."

    def get_status(self) -> Dict[str, Any]:
        """Get agent status with agriculture-specific info."""
        status = super().get_status()
        status.update({
            "crops_in_database": len(self.crop_database),
            "soil_samples_analyzed": len(self.soil_info)
        })
        return status