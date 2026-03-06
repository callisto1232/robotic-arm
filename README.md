# robot-arm

This is a 6-DOF Robotic Arm based on the [Thor Open-Source Robot Arm](https://github.com/AngelLM/Thor) for MEB Industrial Robot Arm Competition 2026.

*http://thor.angel-lm.com/*
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/1cbbec92-6c14-4b87-b76b-f43d3795ae71" />

<<<<<<< HEAD
=======
<img width="635" height="705" alt="image" src="https://github.com/user-attachments/assets/5848a76b-e804-4acb-9c08-e7eb9ac484a7" />

<img width="580" height="708" alt="image" src="https://github.com/user-attachments/assets/c6dda4de-157a-4b50-9546-1472c3dab3bf" />

<img width="848" height="704" alt="image" src="https://github.com/user-attachments/assets/e6a8503b-aac6-48e6-a380-af7face8e42d" />
>>>>>>> parent of 2c24960 (.)

## Goal
This project is created to compete in the **18th International MEB Robot Competition Industrial Robot Arm Category**. The robot is designed to automatically identify, pick and place different colored cubes into the specific target bins.

## Gripper
Custom gripper optimized to manipulate 40x40 mm plexiglass cubes

## Image Processing
Image processing used for autonomous movement, color detection and precise pick-and-place movement with OpenCV
**Raspberry Pi 4 8GB** and **Raspberry Pi Camera Module 3** for fast image processing


## Bill of Materials

### 14/02/2026

| Category | Qty | Item Description | Unit Price (TRY) | Total Price (TRY) |
| :--- | :---: | :--- | :---: | :---: |
| **Stepper Motors** | 1 | Stepper Motor Type A | 617.14 | 617.14 |
| | 3 | Stepper Motor Type B | 3,062.40 | 9,187.20 |
| | 3 | Stepper Motor Type C | 323.40 | 970.20 |
| **Servo** | 0 | MG995 High Torque Servo (In Stock) | - | 0.00 |
| **Mechanical** | 1 | GT2 208mm Closed-Loop Belt | - | 0.00 |
| | 2 | GT2 Belt (1m) | 130.80 | 261.60 |
| | 1 | 16014 Ball Bearing | 565.55 | 565.55 |
| | 11 | 608zz Ball Bearing | 13.53 | 148.83 |
| | 10 | 625zz Ball Bearing | 24.00 | 240.00 |
| | 2 | mf84zz Flanged Bearing | 63.36 | 126.72 |
| | 1 | 6mm Steel Balls (Pack of 50) | 180.00 | 180.00 |
| | 2 | kfl08 Pillow Block Bearing | 92.40 | 184.80 |
| | 3 | 20 Tooth Pulley (8mm bore) | 42.24 | 126.72 |
| | 2 | 40 Tooth Pulley (8mm bore) | 113.52 | 227.04 |
| | 3 | 20 Tooth Pulley (5mm bore) | 40.05 | 120.15 |
| | 2 | 40 Tooth Pulley (5mm bore) | 114.81 | 229.62 |
| | 1 | 8mm Linear Shaft (1m) | 441.60 | 441.60 |
| | 1 | 5mm Linear Shaft (1m) | 209.51 | 209.51 |
| | 6 | M3 Brass Threaded Inserts | 4.37 | 26.22 |
| | 1 | M3 Socket Head Screw Set (300pcs) | 732.60 | 732.60 |
| | 1 | M3 Phillips Head Screw Set (632pcs) | 511.20 | 511.20 |
| | 1 | M4x20 Socket Head Screw | 43.20 | 43.20 |
| | 1 | M5x12 Phillips Head Screw | 52.20 | 52.20 |
| | 1 | M5x16 Socket Head Screw | 42.00 | 42.00 |
| | 1 | M5x20 Socket Head Screw | 47.40 | 47.40 |
| | 1 | 8x1 Magnets (15pcs) | 148.00 | 148.00 |
| **Electronics** | 1 | Raspberry Pi 4 (8GB RAM) | 6,412.16 | 6,412.16 |
| | 1 | Raspberry Pi Heatsink Case | 26.58 | 26.58 |
| | 1 | Arduino Mega 2560 | 844.11 | 844.11 |
| | 5 | Heatsink Set | 15.95 | 79.75 |
| | 6 | DRV8825 Stepper Motor Driver | 78.29 | 469.74 |
| | 1 | RAMPS 1.4 Shield | 339.24 | 339.24 |
| | 1 | Raspberry Pi Camera Module v3 | 2,091.46 | 2,091.46 |
| | 1 | Camera Ribbon Cable (100cm) | 78.14 | 78.14 |
| | 1 | XL4015 Buck Converter | 106.31 | 106.31 |
| | 4 | Optical Endstop Sensor | 71.28 | 285.12 |
| | 1 | Mechanical Limit Switch | 47.52 | 47.52 |
| | 1 | 64GB MicroSD Card | 529.00 | 529.00 |
| | 1 | USB-B Cable (30cm) | 27.11 | 27.11 |
| | 4 | 50x50x10 Cooling Fan | 42.24 | 168.96 |
| | 7 | 40x40x10 Cooling Fan | 42.24 | 295.68 |
| | 10 | XT60 Connector Pair (Male-Female) | 26.16 | 261.60 |
| | 1 | 11.1V 5000mAh Lipo Battery | 4,304.44 | 4,304.44 |
| | 1 | Lipo Voltage Tester/Alarm | 100.32 | 100.32 |
| | 1 | Toggle Power Switch | 22.33 | 22.33 |
| | 1 | Toggle Switch | 34.02 | 34.02 |
| | 1 | Heat Shrink Tubing Set | 130.80 | 130.80 |
| | 10 | Stepper Motor Extension Cables | 31.48 | 314.80 |
| **Filament** | 1 | Tough PLA (Grey) | 792.00 | 792.00 |
| | 3 | Tough PLA (White) | 792.00 | 2,376.00 |
| | 1 | ABS Filament (Natural) | 588.00 | 588.00 |
| | 1 | 1mm Creality Nozzle | 78.48 | 78.48 |
| **GRAND TOTAL** | | | | **36,243.17 TRY** |

## Project Goals
- [ ] Materials arrived

# Contributors:
<p align="center">
  <a href="https://github.com/fox197524">
    <img src="https://avatars.githubusercontent.com/u/188798769?v=4" width="100" height="100" alt="fox197524"/>
  </a>
  <a href="https://github.com/callisto1232">
    <img src="https://avatars.githubusercontent.com/u/146484672?v=4" width="100" height="100" alt="callisto1232"/>
  </a>
</p>


