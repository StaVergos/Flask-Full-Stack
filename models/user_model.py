import uuid
from dataclasses import field
from datetime import datetime

from marshmallow_dataclass import dataclass as mm_dataclass
from typing import Optional, List
from dataclasses_json import dataclass_json, Undefined
from marshmallow import validate


@dataclass_json(undefined=Undefined.EXCLUDE)
@mm_dataclass(frozen=True)
class UserModel:
    username: str = field(metadata={"validate": validate.Length(min=8, max=20)})
    password: str = field(metadata={"validate": validate.Length(min=6, max=16)})
    # is_admin: bool

    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: datetime = field(metadata={
        'dataclasses_json': {
            'encoder': lambda x: datetime.timestamp(x),
        }
    }, default_factory=datetime.utcnow)
