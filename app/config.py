from hydra import compose, initialize
from omegaconf import DictConfig


def load_config(config_name: str = "config") -> DictConfig:
    with initialize(config_path="../conf", version_base=None):
        cfg = compose(config_name=config_name)
    return cfg
