from pydantic import BaseModel, Field


class FlopsSimulatorRequest(BaseModel):
    task_description: str = Field(
        ...,
        description="A description of the knowledge worker task to be simulated.",
        json_schema_extra={"example": "Summarize 10 financial reports"},
    )
    allocated_flops: float = Field(
        ...,
        ge=0,
        description="The amount of computational power (in TFLOPs) allocated to the task.",
        json_schema_extra={"example": 100.0},
    )


class FlopsSimulatorResponse(BaseModel):
    task: str
    productivity_multiplier: float = Field(
        ...,
        description="The calculated productivity gain factor.",
        json_schema_extra={"example": 5.7},
    )
    equivalent_human_hours_saved: float = Field(
        ...,
        description="The estimated number of human hours saved by using AI leverage.",
        json_schema_extra={"example": 32.98},
    )
