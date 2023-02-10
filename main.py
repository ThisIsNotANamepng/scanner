import os
import funcs
import subprocess


todo = input("'scan', 'quarantine'")

if (todo=="scan" or todo=="s"):
  funcs.initScan()
elif (todo=="quarantine" or todo=="q"):
  funcs.initQuarantine()
  