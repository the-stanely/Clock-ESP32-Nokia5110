import pcd8544_fb
from machine import Pin, RTC, SPI
import ntptime
import sys
import utime
from writer import Writer

# Fonts
import marrada30 as clock   # This font only has ' 0123456789.:'
import arialn11 as small

#----------------------------------------------------------------------------------
# Mode of operation
timezone = -5
clockmode = 12  # 24 or 12
#----------------------------------------------------------------------------------

# Set up SPI 2 for hardware transfers.
spi = SPI(2, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
spi.init()

# Setup up ESP32 DEVKIT with Nokia 5110. Using SPI .
cs = Pin(16)
dc = Pin(5)
rst = Pin(21)
bl = Pin(17, Pin.OUT, value=1)

# Constants
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
scr_wd = 84     # Nokia 5110 width
scr_ht = 48     # Nokia 5110 height

# Check for network connection & exit if none.
if not station.isconnected():
    print('No network connection, exiting...')
    sys.exit()

# Get network time from ntp.
ntptime.settime()   # This sets the RTC to UTC.

# Get MicroPython UTC epoch time in seconds.
utc_time = utime.time()
# Offset UTC by timezone using 3600 seconds per hour.
local_time = utc_time + 3600 * timezone
# Get local time's datetime tuple.
yy, mo, dd, hh, mm, ss, wkd, yrd = [d for d in utime.localtime(local_time)]

# Set the RTC to local time.  (I don't think the uP docs are exactly right about this.)
RTC().datetime((yy, mo, dd, 0, hh, mm, ss, 0))

# Create a framebuf instance of display using SPI driver.
ssd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

# Create two Writer instances for two fonts.
wri_bcf = Writer(ssd, clock, verbose=False)     # Big Clock font.
wri_bcf.set_clip(True, True, False)             # Clip is on
wri_s = Writer(ssd, small, verbose=False)       # Small font line 2.
wri_s.set_clip(True, True, False)               # Clip is on


# Create blank strings to erase display lines to eol.
bcf_blank_wd = wri_bcf._charlen(' ')    # Width of a big font blank
px_to_eol = bcf_blank_wd                # Create big blanks to clear to eol 1.
bcf_clr_eol = ' '
while px_to_eol < scr_wd:
	bcf_clr_eol += ' '
	px_to_eol += bcf_blank_wd

s_blank_wd = wri_s._charlen(' ')        # Width of a small font blank
px_to_eol = s_blank_wd                  # Create small blanks to clear to eol 2.
s_clr_eol = ' '
while px_to_eol < scr_wd:
	s_clr_eol += ' '
	px_to_eol += s_blank_wd

if clockmode == 24:
    l2start = 10
else:
    l2start = 4

while True:
    now = RTC().datetime()

    now_day = str(DAYS[now[3]])[:3]
    now_date = '%2.2d/%2.2d/%2.2d' % (now[1], now[2], now[0])
    now_day_date = now_day + '. ' + now_date

    now4 = now[4]
    if clockmode == 24:
        am_pm = ''
    else:
        if now[4] >= 13:
            am_pm = '  PM'
            now4 = now[4] - 12
        elif now[4] == 0:
            now4 = 12
        else:
            am_pm = '  AM'

    now_time = "%2d:%2.2d:%2.2d" % (now4, now[5], now[6])

    wri_bcf.set_textpos(ssd, 0, 0)          # Clear line 1 to eol.
    wri_bcf.printstring(bcf_clr_eol)
    wri_bcf.set_textpos(ssd, 0, 0)          # Write the time.
    wri_bcf.printstring(now_time)
    
    wri_s.set_textpos(ssd, 33, 0)            # Clear line 2 to eol.
    wri_s.printstring(s_clr_eol)
    wri_s.set_textpos(ssd, 33, l2start)     # Write the date on line 2.
    wri_s.printstring(now_day_date+am_pm)
    ssd.show()

    utime.sleep(0.25)   # wait & loop
