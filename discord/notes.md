

### Adjuntar ficheros.

```python
# Para adjuntar un conjunto de ficheros.
my_files = [
    discord.File('imagen.png'),
    discord.File('imagen1.png'),
]
await ctx.send(files = my_files)

# Para adjuntar un único fichero.
await ctx.send(file = discord.File('imagen1.png'))
```






