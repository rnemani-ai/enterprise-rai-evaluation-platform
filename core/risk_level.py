"""
risk_level.py

Defines standardized enterprise risk levels used across
the Enterprise Responsible AI Evaluation Platform.

Using an Enum ensures consistent reporting and avoids
hard-coded string values throughout the framework.
"""

from enum import Enum


class RiskLevel(str, Enum):
    """
    Enterprise AI risk classification.

    LOW
        Minimal risk detected.

    MEDIUM
        Some concerns identified.

    HIGH
        Significant risk requiring attention.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"