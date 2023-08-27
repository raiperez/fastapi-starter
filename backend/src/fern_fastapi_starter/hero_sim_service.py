from .api.generated.resources.hero_sim.service.service import AbstractHeroSimService
from .api.generated import RunSimulationRequest, RunSimulationResponse, InvalidRequestError

MAX_SIMULATIONS: int = 100


class HeroSimService(AbstractHeroSimService):
    def run_simulation(self, *, request: RunSimulationRequest) -> RunSimulationResponse:
        if request.num_simulations > MAX_SIMULATIONS:
            raise InvalidRequestError(f"Invalid Request. Max amount of simulations to queue is {MAX_SIMULATIONS}")

        return RunSimulationResponse(startId=1, endId=2)
