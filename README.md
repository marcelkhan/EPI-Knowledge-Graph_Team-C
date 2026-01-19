# EPI Knowledge Graph – Team C
Wissensgraph zur Evaluation des Studiengangs Informatik (B.A.) an der TH Köln.

## Überblick
Dieses Projekt visualisiert eine strukturierte Wissensbasis als interaktiven Graphen.
Die Anwendung startet eine grafische Oberfläche (Pygame), in der Knoten, Kanten und
Beziehungen des Wissensgraphen dargestellt und erkundet werden können.

## Projektstruktur (Auszug)
* `main.py` – Einstiegspunkt der Anwendung (Initialisierung & Start der GUI).
* `Structured_Knowledge_Graph/` – Inhalte/Struktur des Wissensgraphen.
* `GraphModel/` – Datenmodell für Knoten, Kanten und Graph-Logik.
* `View/` – Darstellung und UI-Komponenten.
* `ComponentAssembly/` – Zusammensetzen der UI-Komponenten.

## Voraussetzungen
* Python 3.13 (siehe `requirements.txt`).
* Abhängigkeiten:
  ```bash
  python -m pip install -r requirements.txt
  ```

## Anwendung starten
```bash
python main.py
```
Die Anwendung öffnet ein Fenster und zeigt den Wissensgraphen an.

## Lizenz
Dieses Projekt steht unter der GNU General Public License v3.0.
Details siehe `COPYING.txt`.
