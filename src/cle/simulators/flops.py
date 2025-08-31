import math
from cle.models.simulators import FlopsSimulatorRequest, FlopsSimulatorResponse


class ProductivitySimulator:
    BASE_TASK_TIME_HOURS: float = 40.0

    def calculate_leverage(
        self, request: FlopsSimulatorRequest
    ) -> FlopsSimulatorResponse:
        FLOPS_OFFSET = 10

        multiplier = 1 + math.log(request.allocated_flops + FLOPS_OFFSET)

        new_time_hours = self.BASE_TASK_TIME_HOURS / multiplier
        hours_saved = self.BASE_TASK_TIME_HOURS - new_time_hours

        return FlopsSimulatorResponse(
            task=request.task_description,
            productivity_multiplier=round(multiplier, 2),
            equivalent_human_hours_saved=round(hours_saved, 2),
        )
