"""Tests for AI for Good agents."""

import pytest
from agents.core import BaseAgent
from agents.education import TutoringAgent
from agents.healthcare import DiagnosisAssistant
from agents.agriculture import CropAdvisor
from agents.arts import CreativityAssistant


class TestTutoringAgent:
    """Test suite for TutoringAgent."""

    def test_initialization(self):
        """Test agent initialization."""
        tutor = TutoringAgent(
            name="Math Tutor",
            subject="Mathematics",
            level="High School"
        )
        assert tutor.name == "Math Tutor"
        assert tutor.subject == "Mathematics"
        assert tutor.level == "High School"
        assert tutor.domain == "education"

    def test_process_query(self):
        """Test query processing."""
        tutor = TutoringAgent(
            name="Math Tutor",
            subject="Mathematics",
            level="High School"
        )
        response = tutor.process_query("What is algebra?")
        assert isinstance(response, str)
        assert "Tutoring Response" in response

    def test_student_profile(self):
        """Test student profile creation."""
        tutor = TutoringAgent(
            name="Math Tutor",
            subject="Mathematics",
            level="High School"
        )
        tutor.create_student_profile("STU001", "John Doe", "Grade 10")
        assert "STU001" in tutor.student_profiles
        assert tutor.student_profiles["STU001"]["name"] == "John Doe"


class TestDiagnosisAssistant:
    """Test suite for DiagnosisAssistant."""

    def test_initialization(self):
        """Test agent initialization."""
        assistant = DiagnosisAssistant()
        assert assistant.name == "Medical Diagnosis Assistant"
        assert assistant.domain == "healthcare"

    def test_process_query(self):
        """Test health query processing."""
        assistant = DiagnosisAssistant()
        response = assistant.process_query("I have a cough")
        assert isinstance(response, str)
        assert "Medical Diagnostic Support" in response


class TestCropAdvisor:
    """Test suite for CropAdvisor."""

    def test_initialization(self):
        """Test agent initialization."""
        advisor = CropAdvisor()
        assert advisor.name == "Crop Advisor"
        assert advisor.domain == "agriculture"

    def test_add_crop_info(self):
        """Test crop information database."""
        advisor = CropAdvisor()
        advisor.add_crop_info("wheat", {"season": "winter"})
        assert "wheat" in advisor.crop_database


class TestCreativityAssistant:
    """Test suite for CreativityAssistant."""

    def test_initialization(self):
        """Test agent initialization."""
        assistant = CreativityAssistant(art_form="Writing")
        assert assistant.domain == "arts"
        assert assistant.art_form == "Writing"

    def test_suggest_prompts(self):
        """Test prompt suggestion."""
        assistant = CreativityAssistant()
        prompts = assistant.suggest_prompts(count=3)
        assert len(prompts) == 3


class TestBaseAgent:
    """Test suite for BaseAgent."""

    def test_get_status(self):
        """Test agent status retrieval."""
        tutor = TutoringAgent(
            name="Math Tutor",
            subject="Mathematics",
            level="High School"
        )
        status = tutor.get_status()
        assert status["name"] == "Math Tutor"
        assert status["domain"] == "education"
        assert "created_at" in status


if __name__ == "__main__":
    pytest.main([__file__, "-v"])