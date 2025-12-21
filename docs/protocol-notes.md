# AJAZZ AKP153E Protokoll-Notizen

## Geräteinformationen

- **Vendor ID:** 0x260d (Sharkoon Technologies / Ajazz)
- **Product ID:** 0x1125
- **Device Name:** SKILLER SGM50W / AKP153E Stream Dock
- **Buttons:** 15 programmierbare Tasten
- **Display:** LCD-Buttons (85x85 Pixel pro Button, vermutlich)

## HID-Interfaces

Das Gerät registriert sich mit **8 HID-Interfaces** unter Windows:

| Interface | Usage Page | Usage | Funktion |
|-----------|------------|-------|----------|
| 1 | 1 | 6 | Generic Desktop, Keyboard |
| 1 | 65283 | 0 | Vendor-specific (1) |
| 1 | 12 | 1 | Consumer Control |
| 1 | 1 | 128 | Generic Desktop, System Control |
| 1 | 65281 | 0 | Vendor-specific (2) |
| 1 | 65284 | 2 | Vendor-specific (3) |
| 0 | 1 | 2 | Generic Desktop, Mouse |
| 1 | 65282 | 2 | Vendor-specific (4) |

Die vendor-spezifischen Interfaces (Usage Page 65281-65284) sind vermutlich für die Stream-Deck-Funktionalität gedacht.

## Bekannte Protokoll-Befehle

Basierend auf Community-Reverse-Engineering (GitHub: pyajazz, mirajazz):

### Brightness (Helligkeit setzen)

| Offset | Bytes          | Bedeutung                 |
| ------ | -------------- | ------------------------- |
| 0-2    | 0x43 0x52 0x54 | Header "CRT"              |
| 3-4    | 0x00 0x00      | Padding                   |
| 5-7    | 0x4C 0x49 0x47 | Command "LIG" (Light)     |
| 8-9    | 0x00 0x00      | Padding                   |
| 10     | 0x00-0x64      | Helligkeit 0-100%         |
| 11-511 | 0x00           | Padding (Report-Size 512) |


### Clear Button (Button leeren)

| Offset | Bytes          | Bedeutung             |
| ------ | -------------- | --------------------- |
| 0-2    | 0x43 0x52 0x54 | Header "CRT"          |
| 3-5    | 0x43 0x4C 0x45 | Command "CLE" (Clear) |
| 6      | 0x01-0x0F      | Button-Index (1-15)   |
| 7-511  | 0x00           | Padding               |


### Set Image (Icon auf Button laden)

| Offset | Bytes          | Bedeutung                                   |
| ------ | -------------- | ------------------------------------------- |
| 0-2    | 0x43 0x52 0x54 | Header "CRT"                                |
| 3-5    | 0x42 0x41 0x54 | Command "BAT" (Bild)                        |
| 6-7    | Size (uint16)  | JPEG-Dateigröße                             |
| 8      | Button-Index   | 0x01-0x0F                                   |
| 9-...  | JPEG-Daten     | Bild als JPEG, chunked über mehrere Reports |


Bilder werden in **512-Byte-Paketen** übertragen, JPEG-Format, 85x85 Pixel empfohlen.

## Windows HID-Zugriffsproblem

**Problem:** Unter Windows 10/11 blockiert der Standard-HID-Treiber direkten Schreibzugriff auf alle Interfaces:

- **Output Reports** (`hid.Device.write()`): Fehler `0x00000005` (Zugriff verweigert) oder `0x00000001` (Unzulässige Funktion)
- **Feature Reports** (`send_feature_report()`): Fehler `0x00000001` oder `0x00000057` (Falscher Parameter)

Selbst mit **Administrator-Rechten** ist kein Zugriff möglich.

### Mögliche Ursachen

1. Das Gerät nutzt einen **proprietären Kernel-Mode-Treiber** (Original-Software).
2. Windows klassifiziert das Gerät als **geschütztes Consumer-Device**.
3. HID-Report-Deskriptor ist nicht korrekt für Standard-HID-Zugriff konfiguriert.

### Lösungsansätze

1. **libusb + Zadig:**  
   - Treiber auf WinUSB/libusb-win32 umstellen  
   - Zugriff via `pyusb` statt `hid`  
   - ⚠️ Original-Software funktioniert danach nicht mehr

2. **Linux/macOS:**  
   - Direkter HID-Zugriff oft ohne Probleme möglich  
   - Python-Code sollte dort funktionieren

3. **USB-Traffic-Analyse:**  
   - Mit Wireshark + USBPcap Original-Software analysieren  
   - Alternative Zugriffsmethode identifizieren

4. **Kernel-Mode-Treiber:**  
   - Eigener Windows-Treiber (zu komplex für dieses Projekt)

## Nächste Schritte

- [ ] Tests unter Linux durchführen
- [ ] USB-Capture der Original-Software
- [ ] libusb-Implementierung als Alternative
- [ ] Image-Upload-Logik (JPEG-Chunking) implementieren
- [ ] Key-Event-Listener (Button-Drücke lesen)

## Quellen

- GitHub: [pyajazz](https://github.com/example/pyajazz) (Community-Library)
- GitHub: [mirajazz](https://github.com/example/mirajazz) (Rust-Implementation)
- USB-HID-Spezifikation: https://www.usb.org/hid