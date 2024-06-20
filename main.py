import atexit
from pathlib import Path

import typer
from dotenv import load_dotenv

from plugin_system.plugin_manager import PluginManager
from utilities.config_loader import load_character_config
from utilities.logging import get_logger
from utilities.version import get_version

logger = get_logger("Engine")
load_dotenv()

version = get_version()


def exit_cleanup() -> None:
    logger.warning("Engine is closing")


def main(character_config_file: str) -> None:
    atexit.register(exit_cleanup)
    logger.info("Wasurenakusa Engine version %s", version)
    logger.info("Loading character from file '%s'", character_config_file)
    character_config = load_character_config(Path(character_config_file))
    logger.info("Character '%s' successfully loaded", character_config.name)
    logger.info("Initialize plugin manager")
    pm = PluginManager(character_config)

    logger.info("Start listening to channels")
    pm.call("listen_to_channel").all()


if __name__ == "__main__":
    typer.run(main)
