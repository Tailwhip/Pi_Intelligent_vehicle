import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='intelligent_vehicle',
    entry_point='intelligent_vehicle.envs:IntelligentVehicleEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
