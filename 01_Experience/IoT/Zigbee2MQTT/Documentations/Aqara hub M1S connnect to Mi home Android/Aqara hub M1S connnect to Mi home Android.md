# Aqara hub M1S connnect to Mi home Android
- Aqara hub m1s supports 2 clouds (aiot aqara / miot mijia)
	- aiot aqara cloud for Aqara Home app
	- miot mijia cloud for Mi Home app
- => To connect Aqara hub M1S to Mi Home app, you need to reroute the hub to miot mijia

- In Setting>Region, change location to Chinese Mainland
- Reset the hub:
	- Press 10 times button on the hub, it will factory reset. The light will turn off
	- In a few seconds you will hear Chinese voice prompt telling you that hub is being reset. The light will blink rapidly
- Change cloud:
	- After hearing the voice for a few seconds, press reset button twice
	- You should hear a "Ding" sound
		- If you don't hear ding sound, try pressing the button twice again
		- If there are still no ding sound, unplug the hub and plug again
	- After a while chinese prompt "bla bla bla **aqara app** bla bla bla"
		- => Your hub is connecting to aiot aqara cloud
	- Press reset button twice again and wait for the Ding sound and the Chinese prompt
		- If the chinese prompt "bla bla bla **mijia** bla bla bla", your hub is connecting to miot mijia cloud and ready to be paired to Mi Home app
		- If the chinese prompt is still aqara, try again a few times or unplug the hub and plug again


# For IOS, use 8-number code on the hub

---
- Status: #done

- Tags: #z2m 

- References:
	- [Source](https://www.reddit.com/r/Aqara/comments/pt9gv0/aqara_hub_m1s_will_not_connect_to_mihome_app/)
	- [Source2](https://www.reddit.com/r/Aqara/comments/jyads9/comment/gd28t4h/?utm_source=share&utm_medium=web2x&context=3)

- Related:
	- 
