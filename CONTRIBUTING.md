# Contributing to AI for Good

Thank you for your interest in contributing! We're excited to have you help build agents that solve societal challenges.

## Code of Conduct

Please read and adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to ensure a welcoming environment for all contributors.

## How to Contribute

### 1. Issues and Feature Requests
- Check existing issues before creating a new one
- Provide clear descriptions and reproducible examples
- Use appropriate labels to categorize issues

### 2. Pull Requests
- Fork the repository
- Create a feature branch: `git checkout -b feature/your-feature-name`
- Make your changes with clear, descriptive commits
- Ensure all tests pass: `pytest`
- Submit a PR with a detailed description

### 3. Code Standards
- Follow PEP 8 style guide
- Add docstrings to all functions and classes
- Write unit tests for new functionality
- Update documentation as needed

### 4. Documentation
- Update README.md for significant changes
- Add examples for new features
- Keep docs accurate and up-to-date

## Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/ai-for-good.git
cd ai-for-good
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 agents/
black agents/
```

## Areas We Need Help With

- **New Agent Implementations**: Add agents for specific challenges
- **Domain Expertise**: Contribute knowledge in education, healthcare, agriculture, or arts
- **Testing**: Expand test coverage
- **Documentation**: Improve guides and examples
- **Optimization**: Performance improvements and refactoring

## Questions?

Feel free to open a discussion or issue. We're here to help!

Thank you for making AI for Good better! 🌟