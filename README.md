# Quickstart


- Obtener el token del bot en https://discord.com/developers/applications
- Crear el archivo `.env` y dentro colocar el token.
```
# Dentro de .env
DISCORD_TKN="..."
```

- Luego desde `main.py`.
```
from dotenv import load_dotenv
load_dotenv()

import os
print(os.getenv("DISCORD_TKN"))
```




