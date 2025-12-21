import hid

class HidDevice:
    """
    Wrapper um ein einzelnes USB-HID-Device.

    Kapselt das Öffnen/Schließen des Geräts sowie das Lesen/Schreiben
    von HID-Reports. Nutzt intern das Python-Paket `hid`, das auf HIDAPI basiert.
    """
    def __init__(self, vendor_id: int | None = None, product_id: int | None = None, path: bytes | None = None):
        """
        Erzeugt eine neue HidDevice-Instanz.

        :param vendor_id: USB Vendor ID des Geräts (z.B. 0x1234)
        :param product_id: USB Product ID des Geräts (z.B. 0x0001)
        :param path: Alternativer Gerätepfad, falls VID/PID nicht verwendet werden sollen.
        """
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.path = path
        self._dev: hid.Device | None = None

    def open(self) -> None:
        self._dev = hid.Device()
        if self.path is not None:
            self._dev.open_path(self.path)
        else:
            if self.vendor_id is None or self.product_id is None:
                raise ValueError("vendor_id und product_id oder path müssen gesetzt sein")
            self._dev.open(self.vendor_id, self.product_id)

    def close(self) -> None:
        if self._dev is not None:
            self._dev.close()
            self._dev = None

    def write(self, data: bytes | bytearray) -> int:
        if self._dev is None:
            raise RuntimeError("Device nicht geöffnet")
        return self._dev.write(data)

    def read(self, size: int = 64, timeout_ms: int = 100) -> bytes:
        if self._dev is None:
            raise RuntimeError("Device nicht geöffnet")
        return bytes(self._dev.read(size, timeout_ms))

    @staticmethod
    def enumerate_all() -> list[dict]:
        return list(hid.enumerate())