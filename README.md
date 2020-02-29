# Clock-ESP32-Nokia5110
Simple clock for ESP32 &amp; Nokia 5110 written in MicroPython.  Using ESP32 DEVKIT.  Pinouts used are:

5110 CLK --> Pin(18)   # GPIO18 is Terminal pin 9 (labeled D18.  SPI CLOCK

not used --> Pin(19)  # GPIO19 is Terminal pin 10, labeled D19, not used. SPI MASTER IN, SLAVE OUT

5110 DIN --> Pin(23)  # GPIO23 is Terminal pin 15, labeled D23.  SPI MASTER OUT, SLAVE IN

5110 CE --> Pin(16)    # GPIO16 is Terminal pin 6, labeled RX2.  CHIP ENABLE (CHIP SELECT)

5110 D/C --> Pin(5)     # GPIO05 is Terminal pin 8, labeled D5.  DATA / COMMAND

5110 RST --> Pin(21)   # GPIO21 is Terminal pin 11, labeled D21.  RESET

5110 BL --> Pin(17, Pin.OUT, value=1)  # GPIO17 is Terminal pin 7, labeled TX2.  BACKLIGHT
