# allow writing to the flash - left true, right false

import storage
from adafruit_circuitplayground import cp

storage.remount("/", cp.switch)
