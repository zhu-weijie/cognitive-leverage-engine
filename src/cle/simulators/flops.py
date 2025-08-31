from src.cle.models.simulators import FlopsSimulatorRequest, FlopsSimulatorResponse


class ProductivitySimulator:
    def calculate_leverage(
        self, request: FlopsSimulatorRequest
    ) -> FlopsSimulatorResponse:
        return FlopsSimulatorResponse(
            task=request.task_description,
            productivity_multiplier=1.0,
            equivalent_human_hours_saved=0.0,
        )
