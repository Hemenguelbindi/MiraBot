from dataclasses import dataclass

from environs import Env


@dataclass
class WatherAPI:
    api_token: str
    base_url: str 


@dataclass
class ConfigAPI:
    weath_token: str
    base_url_weather: str


def load_config_api(path: str | None = None) -> ConfigAPI:
    env = Env()
    env.read_env(path)
    return ConfigAPI(weath_token=env('API_WEATHER'), base_url_weather=env.str('BASE_URL_WEATHER'))
