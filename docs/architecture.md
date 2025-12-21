# Architektur - Ajazz Controller

## Überblick

Das Projekt ist als Python-Package mit klarer Schichtentrennung aufgebaut:

- **Core-Layer**: Low-Level-HID-Kommunikation mit USB-Geräten
- **App-Layer**: Anwendungslogik (Profile, Aktionen, Makros) - *geplant*
- **UI-Layer**: Benutzeroberfläche (CLI/GUI) - *geplant*

Diese Struktur ermöglicht eine spätere Portierung der Core-Logik nach C++, oder die oberen Schichten neu schreiben zu müssen.

## Module

### ´src/ajazz_controller/core/´

Enthält die geräteunabhängige HID-Abstraktion:

- **´hid_device.py´**: Wrapper um das Python-Paket ´hid´ (HIDAPI).
  - Öffnen/Schließen von HID-Geräten über VID/PID oder Device-Path
  - Lesen/Schreiben von HID-Reports
  - Enumeration aller verfügbaren HID-Geräte

### `src/ajazz_controller/` *(geplant)*

- **`protocol.py`**: Ajazz-spezifische Befehle (SetImage, SetBrightness, ClearButton)
- **`app/profiles.py`**: Verwaltung von Button-Profilen
- **`app/actions.py`**: Aktionen (OBS-Steuerung, Shortcuts, etc.)
- **`ui/cli.py`**: Command-Line-Interface
- **`ui/qt_main.py`**: Grafische Oberfläche mit Qt

## Datenfluss

User → UI-Layer → App-Layer → Core-Layer (HID) → AJAZZ Stream Dock (USB)

- Alle USB-Kommunikation läuft über `HidDevice`.
- Protokoll-spezifische Details (Report-Struktur, Kommandos) werden in `protocol.py` gekapselt.
- Profile und Aktionen kennen nur High-Level-Funktionen, nicht die HID-Details.

## Abhängigkeiten

- **`hid`** (cython-hidapi): Python-Binding für HIDAPI, plattformübergreifend (Windows/Linux/macOS)
- **pytest** *(dev)*: Unit-Tests
- **black, flake8** *(dev)*: Code-Formatierung und Linting

## Zukünftige Erweiterungen

- Reverse Engineering des Ajazz-Protokolls via USB-Capture (Wireshark)
- Implementierung aller Gerätebefehle in `protocol.py`
- GUI mit Drag-and-Drop für Button-Konfiguration
- Portierung der Core-Logik nach C++ für bessere Performance