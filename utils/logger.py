"""
File        : logger.py
Author      : Sai Krishna
Description : Centralized logger utility for the automation framework.
"""

import logging
from pathlib import Path
from datetime import datetime

from config.config import Config


class Logger:

    _logger = None

    @staticmethod
    def get_logger(name: str = "AutomationLogger") -> logging.Logger:
        """
        Returns a singleton logger instance.

        Args:
            name (str): Logger name.

        Returns:
            logging.Logger
        """

        if Logger._logger:
            return Logger._logger

        # Create logs directory if it doesn't exist
        Config.LOGS_DIR.mkdir(parents=True, exist_ok=True)

        # Log file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = Config.LOGS_DIR / f"Automation_{timestamp}.log"

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        # File Handler
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Log Format
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.propagate = False

        Logger._logger = logger

        return logger