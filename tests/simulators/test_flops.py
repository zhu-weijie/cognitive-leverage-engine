import pytest

from cle.simulators.flops import ProductivitySimulator
from cle.models.simulators import FlopsSimulatorRequest


@pytest.fixture
def simulator():
    return ProductivitySimulator()


def test_calculate_leverage_zero_flops(simulator):
    request = FlopsSimulatorRequest(task_description="Test task", allocated_flops=0)
    response = simulator.calculate_leverage(request)
    assert response.productivity_multiplier > 1.0
    assert response.equivalent_human_hours_saved > 0


def test_calculate_leverage_increases_with_flops(simulator):
    request_low = FlopsSimulatorRequest(
        task_description="Test task", allocated_flops=100
    )
    request_high = FlopsSimulatorRequest(
        task_description="Test task", allocated_flops=1000
    )

    response_low = simulator.calculate_leverage(request_low)
    response_high = simulator.calculate_leverage(request_high)

    assert response_high.productivity_multiplier > response_low.productivity_multiplier
    assert (
        response_high.equivalent_human_hours_saved
        > response_low.equivalent_human_hours_saved
    )


def test_calculate_leverage_response_format(simulator):
    request = FlopsSimulatorRequest(task_description="Format test", allocated_flops=500)
    response = simulator.calculate_leverage(request)
    assert response.task == "Format test"
    assert isinstance(response.productivity_multiplier, float)
    assert isinstance(response.equivalent_human_hours_saved, float)
