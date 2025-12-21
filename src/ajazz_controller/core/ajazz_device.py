"""
Ajazz AKP153E spezifische Device-Klasse.
Implementiert das HID-Protokoll für das Stream Dock.
"""
from .hid_device import HidDevice


class AjazzDevice:
    """
    High-Level-Interface für das Ajazz AKP153E Stream Dock.
    
    VID: 0x260d
    PID: 0x1125
    """
    
    VENDOR_ID = 0x260d
    PRODUCT_ID = 0x1125
    
    def __init__(self):
        self._hid = HidDevice(vendor_id=self.VENDOR_ID, product_id=self.PRODUCT_ID)
    
    def open(self) -> None:
        """Öffnet die Verbindung zum Gerät."""
        self._hid.open()
    
    def close(self) -> None:
        """Schließt die Verbindung."""
        self._hid.close()
    
    def set_brightness(self, percent: int) -> None:
        """
        Setzt die Helligkeit des Displays.
        
        :param percent: Helligkeit in Prozent (0-100)
        """
        if not 0 <= percent <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        
        # Protokoll: 0x43 52 54 00 00 4C 49 47 00 00 <percent>
        report = bytearray(512)
        report[0:3] = b'\x43\x52\x54'  # Header "CRT"
        report[5:8] = b'\x4C\x49\x47'  # "LIG" (Light)
        report[10] = percent
        
        self._hid.write(report)
    
    def clear_button(self, button_index: int) -> None:
        """
        Löscht das Icon eines Buttons.
        
        :param button_index: Button-Index (1-15)
        """
        if not 1 <= button_index <= 15:
            raise ValueError("Button index must be between 1 and 15")
        
        # Protokoll: 0x43 52 54 CLE <button_index>
        report = bytearray(512)
        report[0:3] = b'\x43\x52\x54'  # Header
        report[3:6] = b'CLE'           # Clear
        report[6] = button_index
        
        self._hid.write(report)
    
    # TODO: set_image(), read_key_events()
