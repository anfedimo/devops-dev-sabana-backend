from pydantic import BaseModel, Field
from pydantic import StrictStr

class Challenge(BaseModel):
    title: StrictStr = Field(..., example="Ahorrar 10% de tu ingreso mensual")
    description: StrictStr
    difficulty: StrictStr