from pydantic import BaseModel, Field
from typing import List

class LogRequest(BaseModel):
    logs: List[str] = Field(..., min_items=1)

    @classmethod
    def validate_logs(cls, values):
        if not values["logs"]:
            raise ValueError("Logs list cannot be empty")
        return values
