EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Switch:SW_Push SW3
U 1 1 6052AA51
P 2000 4200
F 0 "SW3" H 2000 4485 50  0000 C CNN
F 1 "Zoom In" H 2000 4394 50  0000 C CNN
F 2 "" H 2000 4400 50  0001 C CNN
F 3 "~" H 2000 4400 50  0001 C CNN
	1    2000 4200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW4
U 1 1 6052B9B2
P 2450 4100
F 0 "SW4" H 2450 4385 50  0000 C CNN
F 1 "Resolution" H 2450 4294 50  0000 C CNN
F 2 "" H 2450 4300 50  0001 C CNN
F 3 "~" H 2450 4300 50  0001 C CNN
	1    2450 4100
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW2
U 1 1 6052B9F4
P 1550 4400
F 0 "SW2" H 1550 4685 50  0000 C CNN
F 1 "Zoom Out" H 1550 4594 50  0000 C CNN
F 2 "" H 1550 4600 50  0001 C CNN
F 3 "~" H 1550 4600 50  0001 C CNN
	1    1550 4400
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 6052BA36
P 1100 4500
F 0 "SW1" H 1100 4785 50  0000 C CNN
F 1 "Center" H 1100 4694 50  0000 C CNN
F 2 "" H 1100 4700 50  0001 C CNN
F 3 "~" H 1100 4700 50  0001 C CNN
	1    1100 4500
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT_US RV1
U 1 1 6052C0F0
P 4900 3500
F 0 "RV1" H 4833 3546 50  0000 R CNN
F 1 "X Position" H 4833 3455 50  0000 R CNN
F 2 "" H 4900 3500 50  0001 C CNN
F 3 "~" H 4900 3500 50  0001 C CNN
	1    4900 3500
	-1   0    0    -1  
$EndComp
$Comp
L Device:R_POT_US RV2
U 1 1 6052D839
P 5700 3500
F 0 "RV2" H 5633 3546 50  0000 R CNN
F 1 "Y Position" H 5633 3455 50  0000 R CNN
F 2 "" H 5700 3500 50  0001 C CNN
F 3 "~" H 5700 3500 50  0001 C CNN
	1    5700 3500
	-1   0    0    -1  
$EndComp
$Comp
L Device:R_POT_US RV3
U 1 1 6052DABB
P 6550 3500
F 0 "RV3" H 6483 3546 50  0000 R CNN
F 1 "Zoom Level" H 6483 3455 50  0000 R CNN
F 2 "" H 6550 3500 50  0001 C CNN
F 3 "~" H 6550 3500 50  0001 C CNN
	1    6550 3500
	-1   0    0    -1  
$EndComp
$Comp
L MCU_RaspberryPi_and_Boards:Pico U1
U 1 1 6052B1D4
P 3500 3550
F 0 "U1" H 3500 4765 50  0000 C CNN
F 1 "Pi Pico" H 3500 4674 50  0000 C CNN
F 2 "RPi_Pico:RPi_Pico_SMD_TH" V 3500 3550 50  0001 C CNN
F 3 "" H 3500 3550 50  0001 C CNN
	1    3500 3550
	1    0    0    -1  
$EndComp
$Comp
L SSD1306-128x64_OLED:SSD1306 Brd1
U 1 1 6052C233
P 1950 2950
F 0 "Brd1" V 1535 3008 50  0000 C CNN
F 1 "SSD1306 OLED" V 1626 3008 50  0000 C CNN
F 2 "" H 1950 3200 50  0001 C CNN
F 3 "" H 1950 3200 50  0001 C CNN
	1    1950 2950
	0    1    1    0   
$EndComp
$Comp
L power:+3.3V #PWR04
U 1 1 6052D643
P 2200 1950
F 0 "#PWR04" H 2200 1800 50  0001 C CNN
F 1 "+3.3V" H 2215 2123 50  0000 C CNN
F 2 "" H 2200 1950 50  0001 C CNN
F 3 "" H 2200 1950 50  0001 C CNN
	1    2200 1950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR05
U 1 1 6052DC4F
P 2200 2150
F 0 "#PWR05" H 2200 1900 50  0001 C CNN
F 1 "GND" H 2205 1977 50  0000 C CNN
F 2 "" H 2200 2150 50  0001 C CNN
F 3 "" H 2200 2150 50  0001 C CNN
	1    2200 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 3000 2800 3000
Wire Wire Line
	2300 3100 2650 3100
Wire Wire Line
	2650 3100 2650 2900
Wire Wire Line
	2650 2900 2800 2900
Wire Wire Line
	2200 2150 2200 2100
Wire Wire Line
	2200 2100 2450 2100
Wire Wire Line
	2450 2100 2450 2800
Wire Wire Line
	2450 2800 2300 2800
Wire Wire Line
	2300 2900 2550 2900
Wire Wire Line
	2550 2900 2550 2000
Wire Wire Line
	2550 2000 2200 2000
Wire Wire Line
	2200 2000 2200 1950
$Comp
L power:GND #PWR07
U 1 1 60538C72
P 3500 4800
F 0 "#PWR07" H 3500 4550 50  0001 C CNN
F 1 "GND" H 3505 4627 50  0000 C CNN
F 2 "" H 3500 4800 50  0001 C CNN
F 3 "" H 3500 4800 50  0001 C CNN
	1    3500 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 4700 3500 4800
Wire Wire Line
	4200 3500 4750 3500
Wire Wire Line
	4200 3400 4550 3400
Wire Wire Line
	4550 3400 4550 3100
Wire Wire Line
	4550 3100 5400 3100
Wire Wire Line
	5400 3100 5400 3500
Wire Wire Line
	5400 3500 5550 3500
Wire Wire Line
	4200 3200 4400 3200
Wire Wire Line
	4400 3200 4400 3000
Wire Wire Line
	4400 3000 6300 3000
Wire Wire Line
	6300 3000 6300 3500
Wire Wire Line
	6300 3500 6400 3500
$Comp
L power:+3.3V #PWR08
U 1 1 6053FB3C
P 5700 1900
F 0 "#PWR08" H 5700 1750 50  0001 C CNN
F 1 "+3.3V" H 5715 2073 50  0000 C CNN
F 2 "" H 5700 1900 50  0001 C CNN
F 3 "" H 5700 1900 50  0001 C CNN
	1    5700 1900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 605402D9
P 5700 4750
F 0 "#PWR09" H 5700 4500 50  0001 C CNN
F 1 "GND" H 5705 4577 50  0000 C CNN
F 2 "" H 5700 4750 50  0001 C CNN
F 3 "" H 5700 4750 50  0001 C CNN
	1    5700 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 3350 4900 3250
Wire Wire Line
	4900 3250 5700 3250
Wire Wire Line
	6550 3250 6550 3350
Wire Wire Line
	5700 3350 5700 3250
Connection ~ 5700 3250
Wire Wire Line
	5700 3250 6550 3250
Wire Wire Line
	5700 3250 5700 1900
Wire Wire Line
	4900 3650 4900 3750
Wire Wire Line
	4900 3750 5700 3750
Wire Wire Line
	6550 3750 6550 3650
Wire Wire Line
	5700 3650 5700 3750
Connection ~ 5700 3750
Wire Wire Line
	5700 3750 6550 3750
Wire Wire Line
	5700 3750 5700 4750
Wire Wire Line
	2800 4100 2650 4100
Wire Wire Line
	1750 4400 2800 4400
Wire Wire Line
	2800 4500 1300 4500
$Comp
L power:GND #PWR06
U 1 1 60552D32
P 2250 4800
F 0 "#PWR06" H 2250 4550 50  0001 C CNN
F 1 "GND" H 2255 4627 50  0000 C CNN
F 2 "" H 2250 4800 50  0001 C CNN
F 3 "" H 2250 4800 50  0001 C CNN
	1    2250 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 4200 2800 4200
Wire Wire Line
	2250 4100 2250 4800
$Comp
L power:GND #PWR03
U 1 1 6055881A
P 1800 4800
F 0 "#PWR03" H 1800 4550 50  0001 C CNN
F 1 "GND" H 1805 4627 50  0000 C CNN
F 2 "" H 1800 4800 50  0001 C CNN
F 3 "" H 1800 4800 50  0001 C CNN
	1    1800 4800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 605596D7
P 1350 4800
F 0 "#PWR02" H 1350 4550 50  0001 C CNN
F 1 "GND" H 1355 4627 50  0000 C CNN
F 2 "" H 1350 4800 50  0001 C CNN
F 3 "" H 1350 4800 50  0001 C CNN
	1    1350 4800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR01
U 1 1 6055A0F7
P 900 4800
F 0 "#PWR01" H 900 4550 50  0001 C CNN
F 1 "GND" H 905 4627 50  0000 C CNN
F 2 "" H 900 4800 50  0001 C CNN
F 3 "" H 900 4800 50  0001 C CNN
	1    900  4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	900  4800 900  4500
Wire Wire Line
	1350 4400 1350 4800
Wire Wire Line
	1800 4200 1800 4800
NoConn ~ 4200 2600
NoConn ~ 4200 2700
NoConn ~ 4200 2900
NoConn ~ 4200 3100
NoConn ~ 4200 3300
NoConn ~ 4200 3600
NoConn ~ 4200 3700
NoConn ~ 4200 3900
NoConn ~ 4200 4000
NoConn ~ 4200 4100
NoConn ~ 4200 4200
NoConn ~ 4200 4400
NoConn ~ 4200 4500
NoConn ~ 2800 4000
NoConn ~ 2800 3900
NoConn ~ 2800 3800
NoConn ~ 2800 3600
NoConn ~ 2800 3700
NoConn ~ 2800 3500
NoConn ~ 2800 3400
NoConn ~ 2800 3200
NoConn ~ 2800 3100
NoConn ~ 2800 2700
NoConn ~ 2800 2600
NoConn ~ 3600 4700
NoConn ~ 3400 4700
NoConn ~ 2800 4300
NoConn ~ 4200 4300
NoConn ~ 4200 2800
NoConn ~ 2800 2800
NoConn ~ 2800 3300
NoConn ~ 4200 3800
$Comp
L power:+3.3V #PWR0101
U 1 1 6058410F
P 4300 1900
F 0 "#PWR0101" H 4300 1750 50  0001 C CNN
F 1 "+3.3V" H 4315 2073 50  0000 C CNN
F 2 "" H 4300 1900 50  0001 C CNN
F 3 "" H 4300 1900 50  0001 C CNN
	1    4300 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 3000 4300 1900
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 60586D2F
P 1600 1950
F 0 "#FLG0101" H 1600 2025 50  0001 C CNN
F 1 "PWR_FLAG" H 1600 2123 50  0000 C CNN
F 2 "" H 1600 1950 50  0001 C CNN
F 3 "~" H 1600 1950 50  0001 C CNN
	1    1600 1950
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG0102
U 1 1 6058814E
P 1600 2100
F 0 "#FLG0102" H 1600 2175 50  0001 C CNN
F 1 "PWR_FLAG" H 1600 2273 50  0000 C CNN
F 2 "" H 1600 2100 50  0001 C CNN
F 3 "~" H 1600 2100 50  0001 C CNN
	1    1600 2100
	1    0    0    1   
$EndComp
Wire Wire Line
	1600 1950 1600 2000
Wire Wire Line
	1600 2000 2200 2000
Connection ~ 2200 2000
Wire Wire Line
	1600 2100 2200 2100
Connection ~ 2200 2100
Wire Wire Line
	4300 3000 4200 3000
Text Notes 2700 1400 0    157  ~ 0
Mandelbrot Pico
Text Notes 2050 1550 0    79   ~ 0
https://github.com/hwiguna/HariFun_202_MandelbrotPico
$EndSCHEMATC
