# hw
0514 changed. 
ghost modification

# ssh keep alive
/etc/ssh/sshd_config: 
- ClientAliveInterval 300
- ClientAliveCountMax 2
(Server will send signal every 300 seconds max 2 times before termination)
~/.ssh/config: ServerAliveInterval=50 # Client sends signal every 50 seconds
