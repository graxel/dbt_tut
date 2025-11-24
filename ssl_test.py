import ssl
import socket

hostname = 'dbc-fe143535-5f0b.cloud.databricks.com'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as sslsock:
        print(sslsock.version())