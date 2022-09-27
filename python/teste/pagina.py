from os import POSIX_SPAWN_DUP2
import posix
import pyautogui as p
import time
timeesp1 = 0.9
timeesp2 = 1.0

x = 760 
y = 700
dx = 40
x2 = x + dx
x3 = x2 + dx
x4 = x3 + dx
x5 = x4 + dx
x6 = x5 + dx

time.sleep(timeesp1)
p.click (x,y)
time.sleep (timeesp1)

time.sleep(timeesp1)
p.click (x2,y)
time.sleep (timeesp1)

time.sleep(timeesp1)
p.click (x3,y)
time.sleep (timeesp1)

time.sleep(timeesp1)
p.click (x4,y)
time.sleep (timeesp1)

time.sleep(timeesp1)
p.click (x5,y)
time.sleep (timeesp1)

time.sleep(timeesp1)
p.click (x6,y)
time.sleep (timeesp1)


p.press('PgUp')
time.sleep (timeesp1)
