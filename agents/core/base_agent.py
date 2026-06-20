"""Base agent class for AI for Good framework."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from datetime import datetime
import json


class BaseAgent(ABC):
    """Base class for all AI agents in the framework."""

    def __init__(self, name: str, description: str, domain: str):
        """
        Initialize the base agent.

        Args:
            name: Name of the agent
            description: Description of agent's purpose
            domain: Domain of application (education, healthcare, agriculture, arts)
        """
        self.name = name
        self.description = description
        self.domain = domain
        self.created_at = datetime.now()
        self.interactions = 0

    @abstractmethod
    def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process a query and return a response.

        Args:
            query: User query or input
            context: Optional context for the query

        Returns:
            Agent's response to the query
        """
        pass

    def log_interaction(self, query: str, response: str) -> None:
        """
        Log an interaction with the agent.

        Args:
            query: User query
            response: Agent response
        """
        self.interactions += 1

    def get_status(self) -> Dict[str, Any]:
        """
        Get current agent status.

        Returns:
            Dictionary containing agent status information
        """
        return {
            "name": self.name,
            "description": self.description,
            "domain": self.domain,
            "created_at": self.created_at.isoformat(),
            "total_interactions": self.interactions,
            "status": "active"
        }

    def __repr__(self) -> str:
        """String representation of the agent."""
        return f"{self.__class__.__name__}(name={self.name}, domain={self.domain})"