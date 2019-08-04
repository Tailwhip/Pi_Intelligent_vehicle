import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='int-v0',
    entry_point='intelligent_vehicle.envs:IntelligentVehicleEnv',
    # timestep_limit=1000,
    # reward_threshold=1.0,
    # nondeterministic=True,
)
