import os

def print_message(message: str) -> None:
    print(message)

def print_message_from_env() -> None:
    env_config_message = os.getenv("ENV_CONFIG_MESSAGE")
    print(env_config_message)