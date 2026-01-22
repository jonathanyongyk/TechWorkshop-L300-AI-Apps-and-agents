from app.agents.agent_processor import AgentProcessor
from typing import Dict
from azure.ai.agents.telemetry import trace_function

_agent_processor_cache: Dict[str, AgentProcessor] = {}

@trace_function()
def get_or_create_agent_processor(agent_id: str, agent_type: str, thread_id: str, project_client) -> AgentProcessor:
    """Get cached AgentProcessor or create new one to avoid repeated initialization."""
    cache_key = f"{agent_type}_{agent_id}"
    if cache_key in _agent_processor_cache:
        processor = _agent_processor_cache[cache_key]
        processor.thread_id = thread_id
        return processor
    processor = AgentProcessor(
        project_client=project_client,
        assistant_id=agent_id,
        agent_type=agent_type,
        thread_id=thread_id
    )
    _agent_processor_cache[cache_key] = processor
    return processor 