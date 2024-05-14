from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class ChatRecord(BaseModel):
    chat_record_id: int
    conn_id: str
    context_strategy: Optional[str]
    prompt_template: Optional[str]
    attack_module: Optional[str]
    metric: Optional[str]
    prompt: str
    prepared_prompt: str
    system_prompt: Optional[str]
    predicted_result: str
    duration: float
    prompt_time: str

class SessionMetadataModel(BaseModel):
    session_id: str = Field(min_length=1)
    endpoints: List[str] = Field(min_length=1)
    created_epoch: str
    created_datetime: str = Field(min_length=1)
    prompt_template: Optional[str]
    context_strategy: Optional[str]
    cs_num_of_prev_prompts: int | None = 5
    attack_module: Optional[str]
    metric: Optional[str]
    system_prompt: Optional[str]

class SessionResponseModel(BaseModel):
    session: SessionMetadataModel
    chat_records: Optional[Dict[str, List[ChatRecord]]]
