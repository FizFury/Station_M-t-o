"""
test_simple.py - test the basic feature of lcdi2c.py driver (LiquidCrystal_I2C portage to MicroPython).
* Author(s): Meurisse D. from MCHobby (shop.mchobby.be).
Products:
---> https://shop.mchobby.be/fr/afficheur-lcd-tft-oled/882-lcd-backpack-i2c-3232100008823.html
---> https://shop.mchobby.be/fr/nouveaute/1807-afficheur-lcd-16x2-i2c-3232100018075-dfrobot.html
	 The two transistor must be removed.
---> https://shop.mchobby.be/fr/afficheur-lcd-tft-oled/881-lcd-20x4-backpack-i2c-blanc-sur-bleu-3232100008816.html
MCHobby investit du temps et des ressources pour écrire de la
documentation, du code et des exemples.
Aidez nous à en produire plus en achetant vos produits chez MCHobby.
------------------------------------------------------------------------
History:
  12 april 2020 - Dominique - initial script
"""
from machine import I2C, Pin
from lcdi2c import LCDI2C
from time import sleep
from Lib import get_measures
import ujson

while True:
    i2c = I2C(Pin(0), Pin(2))
    lcd = LCDI2C( i2c, cols=16, rows=2 )
    lcd.backlight()
    lcd.clear()
    data = str(get_measures())
    lcd.print(data)
    sleep( 2 )
