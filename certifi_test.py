import ssl
import socket
import certifi

print("Certifi CA bundle:", certifi.where())

context = ssl.create_default_context(cafile=certifi.where())

with context.wrap_socket(socket.socket(), server_hostname="dbc-fe143535-5f0b.cloud.databricks.com") as s:
    s.connect(("dbc-fe143535-5f0b.cloud.databricks.com", 443))
    print("SSL connection successful:", s.version())
