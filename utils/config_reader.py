"""
File        : config_reader.py
Author      : Sai Krishna
Description : Reads configuration values from the .env file.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


class ConfigReader:
    """
    Utility class for loading and accessing environment variables.
    """

    # Project Root Directory
    ROOT_DIR = Path(__file__).resolve().parent.parent

    # .env File Path
    ENV_FILE = ROOT_DIR / ".env"

    # Load .env file only once
    load_dotenv(dotenv_path=ENV_FILE)

    @staticmethod
    def get(key: str, default=None):
        """
        Returns the value of an environment variable.

        Args:
            key (str): Environment variable name.
            default: Default value if the key is not found.

        Returns:
            str: Environment variable value.

        Raises:
            ValueError: If the required environment variable is missing.
        """

        value = os.getenv(key, default)

        if value is None:
            raise ValueError(
                f"Environment variable '{key}' is missing in the .env file."
            )

        return value

    @staticmethod
    def get_int(key: str, default=None):
        """
        Returns an integer environment variable.
        """

        return int(ConfigReader.get(key, default))

    @staticmethod
    def get_bool(key: str, default=False):
        """
        Returns a boolean environment variable.
        Accepts: true, false, yes, no, 1, 0
        """

        value = str(ConfigReader.get(key, default)).lower()

        return value in ("true", "1", "yes", "y")