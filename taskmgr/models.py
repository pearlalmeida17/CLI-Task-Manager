from dataclasses import dataclass, field, asdict
from typing import Optional, Literal
from datetime import datetime, timezone

@dataclass
class tasks:

    

    #details of the task class, what it is made of and what it comprises of
    
    id : int
    title: str
    done: bool = False
    priority: Literal['low','med','high'] = 'med'
    tags: list[str] = field(default_factory=list)
    date_created: str = field(default_factory=lambda:datetime.now(timezone.utc).isoformat())
    date_due: Optional[str] = None


    def to_dict(self)-> dict:
        #covert task objects into dictionary to load in JSON file 
        return asdict(self)

    @staticmethod
    def from_dict(data: dict)-> "tasks":
        #convert data in JSON data dictionaries into objects  
        return tasks(**data)