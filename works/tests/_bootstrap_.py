# Add path to source code
import sys
import os
if os.getcwd().endswith('tests'):
    sys.path.insert(0, '..')
elif os.getcwd().endswith('websocket-server'):
    sys.path.insert(0, '.')
