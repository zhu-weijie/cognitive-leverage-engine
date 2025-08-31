from pydantic import BaseModel, Field


class FlopsSimulatorRequest(BaseModel):
    task_description: str = Field(
        ...,
        description="A description of the knowledge worker task to be simulated.",
        example="Summarize 10 financial reports",
    )
    allocated_flops: float = Field(
        ...,
        gt=0,
        description="The amount of computational power (in TFLOPs) allocated to the task.",
        example=100.0,
    )


class FlopsSimulatorResponse(BaseModel):
    task: str
    productivity_multiplier: float = Field(
        ...,
        description="The calculated productivity gain factor.",
        example=1.0,
    )
    equivalent_human_hours_saved: float = Field(
        ...,
        description="The estimated number of human hours saved by using AI leverage.",
        example=0.0,
    )
