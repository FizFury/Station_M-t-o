# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import main

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Julien-IOT', 'CESI76130$Rouen')
        while not sta_if.isconnected():
            pass
    print('Configuration internet:', sta_if.ifconfig())

#import webrepl
#webrepl.start()
gc.collect()
do_connect()
