from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    """ class for config telegram bot    """
    token: str           
    admin_ids: list[int]  
    

@dataclass
class Config:
    """ class for config main  """
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))))


# ADMINS
def get_admins(path: str | None = None) -> list[int]:
    env = Env()
    env.read_env(path)
    return list(map(int, env.list("ADMIN_IDS")))


if __name__ == "__main__":
    print(load_config())
    print(get_admins())
    print()