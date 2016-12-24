# D-Link-DSL2750B-ssh-adsl-speed

Requires: sudo apt-get install expect python3

A python script that call another script to launch an expect script that connect to the router via ssh and read the line containing the RX e TX bytes of the pppoa interface.
The python script parse that line and compute the speed from the last values.
