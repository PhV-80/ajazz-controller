# Ajazz Controller

Cross‑platform Controller‑Software für das AJAZZ Stream Dock AKP153E.  
Ziel ist es, das Gerät ohne die Original‑Software vollwertig zu nutzen und dabei UAC‑Probleme unter Windows zu vermeiden.

## Ziele

- Eigene, herstellerunabhängige Steuer‑Software für das AJAZZ Stream Dock  
- Unterstützung für Windows, Linux und macOS  
- Volle Nutzung des Funktionsumfangs (Tasten, Icons, Helligkeit, Profile)
- Lern‑ und Portfolio‑Projekt im Rahmen der Ausbildung zum FIAE

## Technologie‑Stack

- Python 3 mit `hid` (HIDAPI‑Binding) für die Gerätekommunikation
- Geplante GUI mit Qt  
- Späterer Port der Kernlogik nach C++

## Projektstatus

- Projektstruktur, Git und GitHub-Repository sind eingerichtet
- HID-Device-Layer implementiert und getestet
- Device Discovery funktioniert (AJAZZ AKP153E erkannt: VID 0x260d, PID 0x1125)
- Architektur dokumentiert
- **Protokoll-Implementierung in Entwicklung:**
  - Brightness/Clear/SetImage-Befehle implementiert
  - **Windows HID-Zugriffsproblem identifiziert** (siehe `docs/protocol-notes.md`)
  - Tests unter Linux/macOS oder mit libusb geplant

**Nächster Meilenstein:** Alternative Zugriffsmethode testen oder auf Linux/macOS portieren
