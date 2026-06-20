"""Diagnosis assistance agent for healthcare domain."""

from typing import Optional, Dict, Any, List
from agents.core import BaseAgent


class DiagnosisAssistant(BaseAgent):
    """Agent assisting with medical diagnosis support."""

    def __init__(self, name: str = "Medical Diagnosis Assistant"):
        """
        Initialize diagnosis assistant.

        Args:
            name: Name of the assistant
        """
        super().__init__(
            name=name,
            description="Provides diagnostic support and health information",
            domain="healthcare"
        )
        self.symptom_database = {}

    def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process health-related query and provide diagnostic information.

        Args:
            query: Patient symptoms or health question
            context: Optional context like age, medical history, etc.

        Returns:
            Diagnostic information and recommendations
        """
        self.log_interaction(query, "response")

        response = f"""
        Medical Diagnostic Support:
        
        Patient Query: {query}
        
        IMPORTANT: This is informational only and NOT a medical diagnosis.
        
        This response provides:
        1. Possible conditions based on symptoms
        2. When to seek professional medical care
        3. General wellness recommendations
        4. Preventative health measures
        
        ALWAYS consult with a licensed healthcare provider for proper diagnosis and treatment.
        """
        return response

    def add_symptom(self, symptom: str, related_conditions: List[str]) -> None:
        """Add symptom and related conditions to database."""
        self.symptom_database[symptom.lower()] = related_conditions

    def get_status(self) -> Dict[str, Any]:
        """Get agent status with healthcare-specific info."""
        status = super().get_status()
        status.update({
            "symptom_database_size": len(self.symptom_database),
            "medical_compliance": True
        })
        return status