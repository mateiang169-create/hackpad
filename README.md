# My RP2040 Hackpad

Welcome to the official documentation of my custom-built, open-source macro pad. This project was conceptualized, designed, and assembled from scratch as part of the Hack Club Stardance challenge. It combines a compact hardware footprint with highly customizable firmware to streamline daily developer workflows, shortcuts, and gaming macros.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features & Hardware Architecture](#key-features--hardware-architecture)
- [Repository Structure & File Organization](#repository-structure--file-organization)
- [Deep Dive: Design & Engineering Process](#deep-dive-design--engineering-process)
  - [1. Schematic Capture & PCB Routing (KiCad)](#1-schematic-capture--pcb-routing-kicad)
  - [2. 3D Enclosure Engineering (Autodesk Fusion 360)](#2-3d-enclosure-engineering-autodesk-fusion-360)
- [Step-by-Step Assembly & Getting Started Guide](#step-by-step-assembly--getting-started-guide)
- [License & Acknowledgments](#license--acknowledgments)

---

## 🔍 Project Overview
The primary goal of this project was to design a functional, aesthetically pleasing, and ergonomic macro pad that integrates physical tactile inputs with real-time visual feedback. Built around the powerful and versatile **Seeed Studio XIAO RP2040**, the board features a matrix of mechanical switches, an incremental rotary encoder for dynamic volume control or scrolling, and an I2C-enabled OLED display to render custom text, states, or animations on the fly.

---

## ✨ Key Features & Hardware Architecture
- **Core Processing Unit:** Powered by the dual-core ARM Cortex-M0+ RP2040 microcontroller running at up to 133 MHz, providing ample processing power and flexible Programmable I/O (PIO) capabilities.
- **Input Matrix:** Features 4 mechanical switch sockets wired in a custom matrix topology protected by 1N4148 switching diodes to eliminate ghosting and phantom presses during simultaneous inputs.
- **Rotary Control:** Integrates an EC11 incremental rotary encoder with an integrated push-button switch, ideal for multi-function controls (e.g., zooming, scrubbing timelines, or adjusting system audio levels).
- **Visual Feedback Display:** Equipped with a 0.91-inch SSD1306 monochrome OLED screen communicating via I2C protocol, offering crisp textual or graphical indicators.
- **Custom Enclosure:** A robust 3D-printed chassis engineered with a designated transparent viewing window (utilizing clear PETG or PLA filament) to showcase the internal soldered components and PCB traces.

---

## 📂 Repository Structure & File Organization
To maintain a clean and professional workflow compliant with hardware open-source standards, the repository is structured into distinct, dedicated directories:


├── CAD/              # Contains 3D computer-aided design files, step models, and fusion assemblies
├── Firmware/         # Contains source code, configuration scripts, and compiled binaries for the RP2040
├── PCB/              # Contains KiCad schematic (.sch/.kicad_sch), layout (.kicad_pcb), and project files
└── production/       # Contains manufacturing outputs, Gerber files, drill files, and BOM exports for fabrication

## Project Screenshots

### 3D PCB View
<img width="1280" height="685" alt="Screenshot 2026-09-21 185126" src="https://github.com/user-attachments/assets/2bdf3d37-6e5d-4272-9ff1-08af7fe81dd0" />


### Schematic
<img width="1280" height="683" alt="Screenshot 2026-09-21 184806" src="https://github.com/user-attachments/assets/c9b2ab66-8921-4da2-a362-2c17270dd5f1" />


### PCB Design
<img width="1280" height="684" alt="Screenshot 2026-09-21 184822" src="https://github.com/user-attachments/assets/59742784-ed79-40b4-a4e3-65ee8ba6429d" />


### 3D Case
<img width="1278" height="686" alt="Screenshot 2026-09-21 185040" src="https://github.com/user-attachments/assets/0c7c72ee-ee3f-4c66-be8b-6987298921af" />


---

## Bill of Materials (BOM)

| Component | Quantity | Description |
| :--- | :---: | :--- |
| Seeed Studio XIAO RP2040 | 1 | Microcontroller |
| Mechanical Switches | 4 | Key switches |
| EC11 Rotary Encoder | 1 | Knob encoder |
| 0.91" OLED Screen (SSD1306) | 1 | Display |
| 1N4148 Diodes | 4 | Matrix diodes |
| 3D Printed Case | 1 | Custom enclosure |
