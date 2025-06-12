import platform
import sys

from config import settings


def create_allure_environment_file():
    env_items = [f'{key} = {value}' for key, value in settings.model_dump().items()]
    env_items.append(f'os_info={platform.system()}, {platform.release()}')
    env_items.append(f'python_version={sys.version}')

    properties = '\n'.join(env_items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as prop_file:
        prop_file.write(properties)
