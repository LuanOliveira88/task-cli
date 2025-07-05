from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Literal, Optional

@dataclass
class Task:
    id: int
    description: str
    status: Literal['todo', 'in-progress', 'done'] = 'todo'
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


    def to_dict(self):
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat() if self.updated_at else None
        
        return data
    
    @classmethod
    def from_dict(cls, data: dict):
        data = data.copy()
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        data['updated_at'] = datetime.fromisoformat(data['updated_at']) if data['updated_at'] else None

        return cls(**data)
    