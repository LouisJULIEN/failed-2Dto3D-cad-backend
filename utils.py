import os


def env_is_local() -> bool:
    return os.environ.get('APP_ENV') == 'local'
