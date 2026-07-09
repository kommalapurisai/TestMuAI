"""
File        : config.py
Author      : Sai Krishna
Description : Centralized configuration used across the automation framework.
"""

from pathlib import Path
from utils.config_reader import ConfigReader


class Config:
    """
    Central configuration class.
    Reads all required values from the .env file through ConfigReader.
    """

    # ==========================
    # Project Directories
    # ==========================
    ROOT_DIR = Path(__file__).resolve().parent.parent

    LOGS_DIR = ROOT_DIR / "logs"
    REPORTS_DIR = ROOT_DIR / "reports"
    SCREENSHOTS_DIR = ROOT_DIR / "screenshots"

    # ==========================
    # Environment Configuration
    # ==========================
    BASE_URL = ConfigReader.get("BASE_URL")
    GRID_URL = ConfigReader.get("GRID_URL")

    EXECUTION_MODE = ConfigReader.get("EXECUTION_MODE").lower()

    TESTMU_USERNAME = ConfigReader.get("TESTMU_USERNAME")
    TESTMU_ACCESS_KEY = ConfigReader.get("TESTMU_ACCESS_KEY")

    IMPLICIT_WAIT = ConfigReader.get_int("IMPLICIT_WAIT")
    EXPLICIT_WAIT = ConfigReader.get_int("EXPLICIT_WAIT")

    # ==========================
    # Browser Configuration
    # ==========================
    PAGE_LOAD_TIMEOUT = 20
    SCRIPT_TIMEOUT = 20

    # ==========================
    # Report Configuration
    # ==========================
    HTML_REPORT_NAME = "Automation_Report.html"

    # ==========================
    # Screenshot Configuration
    # ==========================
    FAILED_SCREENSHOT_PREFIX = "FAILED"