import multiprocessing
import os

# Server Socket
bind = 'unix:/tmp/flask_app.sock'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = False
spew = False

# Logging
logfile = '/opt/ansible-web-application/log/app.log'
loglevel = 'info'
logconfig = None

# Process Name