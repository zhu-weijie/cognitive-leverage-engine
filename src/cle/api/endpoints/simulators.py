from fastapi import APIRouter, Depends
from src.cle.models.simulators import FlopsSimulatorRequest, FlopsSimulatorResponse
from src.cle.simulators.flops import ProductivitySimulator

router = APIRouter()


def get_simulator():
    return ProductivitySimulator()


@router.post("/flops", response_model=FlopsSimulatorResponse)
def run_flops_simulation(
    request: FlopsSimulatorRequest,
    simulator: ProductivitySimulator = Depends(get_simulator),
):
    return simulator.calculate_leverage(request)
