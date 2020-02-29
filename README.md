# Clock-ESP32-Nokia5110
Simple clock for ESP32 &amp; Nokia 5110 written in MicroPython.
Using ESP32 DEVKIT.  Pinouts used are:

# Set up SPI 2 for hardware transfers.
spi = SPI(2, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
# sck = Pin(18)   # GPIO18 is Terminal pin 9 (labeled D18)
# MISO = Pin(19)  # GPIO19 is Terminal pin 10 (labeled D19) not used
# MOSI = Pin(23)  # GPIO23 is Terminal pin 15 (labeled D23)

# Setup up ESP32 DEVKIT with Nokia 5110. Using SPI .
cs = Pin(16)    # GPIO16 is Terminal pin 6 (labeled RX2)
dc = Pin(5)     # GPIO05 is Terminal pin 8 (labeled D5)
rst = Pin(21)   # GPIO21 is Terminal pin 11 (labeled D21)
bl = Pin(17, Pin.OUT, value=1)  # GPIO17 is Terminal pin 7 (labeled TX2)
