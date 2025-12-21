"""
Unit tests für HidDevice-Klasse.
"""

import pytest
from ajazz_controller.core.hid_device import HidDevice


def test_enumerate_returns_list():
    """Test: enumerate_all() gibt eine Liste zurück."""
    devices = HidDevice.enumerate_all()
    assert isinstance(devices, list)


def test_enumerate_constains_dicts():
    """Test: Jedes Device ist ein Dictionary mit vendor_id und product_id."""
    devices = HidDevice.enumerate_all()
    if len(devices) > 0:
        device = devices[0]
        assert isinstance(device, dict)
        assert "vendor_id" in device
        assert "product_id" in device


def test_hid_device_requires_vid_pid_or_path():
    """Test: HidDeice wirft Fehler, wenn weder VID/PID noch Path gesetzt sind."""
    dev = HidDevice()
    with pytest.raises(ValueError):
        dev.open()