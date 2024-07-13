import gpiozero
from time import sleep

RELAY_PINS = [2, 3, 4]

for i in RELAY_PINS:
	relay = gpiozero.OutputDevice(i, active_high=False)

	relay.off()
	sleep(1)
	relay.on()
	sleep(1)
	relay.off()
	sleep(1)

print("Turned on and off")
