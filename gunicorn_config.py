# gunicorn_config.py

bind = "127.0.0.1:8000"  # Replace with your desired host and port
workers = 4  # You can adjust this based on your server's capabilities
threads = 2  # You can also adjust this based on your server's capabilities
worker_class = "sync"  # You can experiment with other worker classes