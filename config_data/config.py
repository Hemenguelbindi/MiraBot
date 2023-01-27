from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    """ class for config telegram bot    """
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    """ class for config main  """
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None, debug: bool = True) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN') if debug == False else env('BOT_DEBUG'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env("DB_HOST"),
                                    db_user=env("DB_USER"),
                                    db_password=env("DB_PASSWORD")))


def get_admins(path: str | None = None) -> list[int]:
    env = Env()
    env.read_env(path)
    return list(map(int, env.list("ADMIN_IDS")))


if __name__ == "__main__":
    print(load_config('.env.dev'))
    print(load_config())
