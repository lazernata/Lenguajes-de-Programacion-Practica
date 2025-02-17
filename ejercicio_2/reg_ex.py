import re

email = "ejemplo1@red.ujaen.edu"

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|es)$", email, re.IGNORECASE):
    print("Email es válido")
else:
    print("Email es no válido")