# API Reference

## BaseAgent

Base class for all agents in the AI for Good framework.

### Methods

#### `__init__(name: str, description: str, domain: str)`
Initialize a new agent.

**Parameters:**
- `name` (str): Name of the agent
- `description` (str): Agent description
- `domain` (str): Domain of operation

#### `process_query(query: str, context: Optional[Dict[str, Any]] = None) -> str`
Process a query and return a response.

**Parameters:**
- `query` (str): User query or input
- `context` (Optional[Dict]): Additional context information

**Returns:**
- `str`: Agent response

#### `log_interaction(query: str, response: str) -> None`
Log an agent-user interaction.

**Parameters:**
- `query` (str): User query
- `response` (str): Agent response

#### `get_status() -> Dict[str, Any]`
Get current agent status.

**Returns:**
- `Dict`: Status information

## TutoringAgent

Agent providing personalized tutoring services.

### Inherits From
`BaseAgent`

### Methods

#### `__init__(name: str, subject: str, level: str)`
Initialize tutoring agent.

**Parameters:**
- `name` (str): Agent name
- `subject` (str): Subject being tutored
- `level` (str): Education level

#### `create_student_profile(student_id: str, name: str, current_level: str) -> None`
Create student profile for personalized learning.

**Parameters:**
- `student_id` (str): Unique student identifier
- `name` (str): Student name
- `current_level` (str): Current education level

## DiagnosisAssistant

Healthcare support agent providing diagnostic information.

### Inherits From
`BaseAgent`

### Methods

#### `add_symptom(symptom: str, related_conditions: List[str]) -> None`
Add symptom to knowledge database.

**Parameters:**
- `symptom` (str): Symptom description
- `related_conditions` (List[str]): Possible related conditions

## CropAdvisor

Agriculture advisory agent for sustainable farming.

### Inherits From
`BaseAgent`

### Methods

#### `add_crop_info(crop_name: str, crop_data: Dict[str, Any]) -> None`
Add crop information to database.

**Parameters:**
- `crop_name` (str): Name of crop
- `crop_data` (Dict): Crop information

#### `analyze_soil(soil_sample: Dict[str, Any]) -> str`
Analyze soil properties.

**Parameters:**
- `soil_sample` (Dict): Soil test results

**Returns:**
- `str`: Soil analysis report

## CreativityAssistant

Arts support agent for creative expression.

### Inherits From
`BaseAgent`

### Methods

#### `__init__(name: str = "Creativity Assistant", art_form: str = "General")`
Initialize creativity assistant.

**Parameters:**
- `name` (str): Agent name
- `art_form` (str): Type of art form

#### `suggest_prompts(count: int = 5) -> List[str]`
Generate creative prompts.

**Parameters:**
- `count` (int): Number of prompts to generate

**Returns:**
- `List[str]`: Creative prompts

#### `add_to_portfolio(artwork: Dict[str, Any]) -> None`
Add artwork to portfolio.

**Parameters:**
- `artwork` (Dict): Artwork information

## Response Format

All agent responses follow a consistent format:

```python
{
    "status": "success",
    "agent": "agent_name",
    "timestamp": "ISO8601",
    "response": "Agent response text"
}
```

## Error Handling

Standard error responses:

```python
{
    "status": "error",
    "error_code": "ERROR_CODE",
    "message": "Error description",
    "agent": "agent_name"
}
```