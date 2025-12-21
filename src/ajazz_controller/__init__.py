"""
Ajazz Controller - Cross-platform controller for Ajazz AKP153E stream dock.

Main package providing HID communication and device abstraction.
"""

from .core import HidDevice

__version__ = "0.1.0"
__all__ = ["HidDevice"]