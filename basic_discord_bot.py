import discord
from discord.ext import commands
import random
import os
import requests
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='> ', intents=intents)
number = random.randint(1, 100)

def adivinar_numero(numero):
    global number
    if numero == number:
        number = random.randint(1, 100)
        return "¡Correcto! El número es {number}."
    elif numero < number:
        return "El número es demasiado bajo. Intenta de nuevo."
    else:
        return "El número es demasiado alto. Intenta de nuevo."

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy el bot {bot.user}!')

@bot.command()
async def ja(ctx, count_ja = 5):
    await ctx.send("ja" * count_ja)

@bot.command()
async def python(ctx):
    await ctx.send(f'Python es el lenguaje de programacion mas facil del mundo, yo fui creado con python!')

@bot.command()
async def adivinar(ctx, numero: int):
    await ctx.send(adivinar_numero(numero))

@bot.command()
async def suma(ctx, num1: int, num2: int):
    await ctx.send(f'La suma de {num1} y {num2} es {num1 + num2}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls)) + " 🎲"
    await ctx.send(result)

@bot.command()
async def jaja(ctx):
    sticker = discord.utils.get(ctx.guild.stickers, name="Kody Riendo")

    if sticker:
        await ctx.send(stickers=[sticker])
    else:
        await ctx.send("No encontré el sticker 😢")

@bot.command()
async def meme(ctx):
    meme_path = random.choice(['images/mem1.jpeg', 'images/mem2.jpeg', 'images/mem3.jpeg', 'images/mem4.jpeg', 'images/mem5.jpeg'])
    with open(meme_path, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def pato(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

formas_reciclar = [
    "Convertir botellas en maceteros 🪴",
    "Reutilizar botellas como recipientes 🧴",
    "Hacer organizadores con envases 📦",
    "Reutilizar bolsas de plástico 🛍️",
    "Hacer comederos para aves 🐦",
    "Crear mosaicos con tapas 🎨",
    "Crear juguetes con envases 🧸",
    "Convertir recipientes en cajas 🗃️",
    "Usar envases para germinar plantas 🌱",
    "Reutilizar recipientes grandes 🪣",
    "Separar los residuos reciclables ♻️",
    "Llevar plástico a un punto limpio 🚮",
    "Llevar papel a reciclar 📄",
    "Llevar cartón a reciclar 📦",
    "Reciclar botellas de vidrio 🍾",
    "Reciclar latas de aluminio 🥫",
    "Reciclar latas de acero 🥫",
    "Reciclar periódicos viejos 📰",
    "Reutilizar revistas 📖",
    "Reutilizar hojas por ambas caras 📃",
    "Crear libretas con papel usado 📓",
    "Hacer manualidades con cartón ✂️",
    "Convertir cajas en organizadores 🗂️",
    "Usar tubos de cartón para manualidades 🧻",
    "Crear adornos con papel usado 🎨",
    "Hacer sobres con papel reutilizado ✉️",
    "Crear tarjetas con cartón reciclado 💌",
    "Usar cajas viejas para almacenar objetos 📦",
    "Reutilizar bolsas de papel 🛍️",
    "Reciclar folletos usados 📄",
    "Reutilizar frascos de vidrio 🫙",
    "Convertir frascos en recipientes 🫙",
    "Usar frascos como portalápices ✏️",
    "Crear lámparas con frascos 💡",
    "Hacer decoraciones con vidrio 🎨",
    "Separar el vidrio por colores 🟢",
    "Llevar vidrio a un contenedor especial ♻️",
    "Reutilizar botellas de vidrio 🍾",
    "Convertir latas en maceteros 🌱",
    "Hacer portalápices con latas ✏️",
    "Crear instrumentos con latas 🥁",
    "Reutilizar latas como recipientes 🥫",
    "Crear adornos con latas 🎨",
    "Separar las latas del resto de residuos ♻️",
    "Reciclar tapas metálicas 🔩",
    "Reutilizar tapas para manualidades 🎨",
    "Donar ropa que ya no se usa 👕",
    "Convertir ropa vieja en trapos 🧹",
    "Hacer bolsas de tela con ropa vieja 👜",
    "Reutilizar jeans viejos 👖",
    "Convertir camisetas en bolsas 👕",
    "Donar zapatos que estén en buen estado 👟",
    "Reparar ropa antes de desecharla 🧵",
    "Convertir telas viejas en decoraciones 🎨",
    "Usar retazos de tela para manualidades ✂️",
    "Hacer muñecos con tela reutilizada 🧸",
    "Reutilizar madera de muebles viejos 🪵",
    "Restaurar muebles antiguos 🪑",
    "Convertir madera en estantes 🪵",
    "Hacer cajas con madera reutilizada 📦",
    "Crear decoraciones con madera 🎨",
    "Reutilizar palés de madera 🪵",
    "Reparar muebles dañados 🔧",
    "Usar restos de madera en manualidades ✂️",
    "Reciclar aparatos electrónicos 💻",
    "Llevar celulares viejos a puntos de reciclaje 📱",
    "Reciclar computadores antiguos 💻",
    "Reciclar cables viejos 🔌",
    "Llevar cargadores que ya no funcionan a reciclaje 🔋",
    "Reciclar teclados viejos ⌨️",
    "Reciclar impresoras antiguas 🖨️",
    "Llevar pilas usadas a puntos de recolección 🔋",
    "Reciclar baterías en lugares autorizados 🔋",
    "Reutilizar componentes electrónicos seguros ⚙️",
    "Hacer compost con residuos orgánicos 🌱",
    "Usar restos de frutas para compost 🍎",
    "Usar restos de verduras para compost 🥕",
    "Agregar hojas secas al compost 🍂",
    "Usar restos de café para compost ☕",
    "Usar cáscaras de huevo en el compost 🥚",
    "Aprovechar restos vegetales 🌿",
    "Separar residuos orgánicos 🥬",
    "Crear abono con residuos orgánicos 🌱",
    "Usar compost para plantas 🪴",
    "Reutilizar agua para regar plantas 💧",
    "Reutilizar recipientes de alimentos 🍱",
    "Usar envases para guardar materiales 🗃️",
    "Reutilizar cajas de zapatos 👟",
    "Convertir cajas en juguetes 🧸",
    "Usar rollos de papel para manualidades 🎨",
    "Reutilizar corchos para manualidades 🍾",
    "Crear adornos con materiales usados 🎄",
    "Reutilizar bolsas de regalo 🎁",
    "Guardar papel de regalo para otra ocasión 🎁",
    "Reutilizar sobres ✉️",
    "Reutilizar carpetas escolares 📁",
    "Donar libros que ya no utilizas 📚",
    "Intercambiar libros con otras personas 📚",
    "Donar juguetes en buen estado 🧸",
    "Reparar juguetes antes de desecharlos 🔧",
    "Intercambiar ropa con familiares o amigos 👕",
    "Llevar residuos a centros de reciclaje ♻️"
]

formas_reducir = [
    "Usar una botella reutilizable 🥤",
    "Llevar bolsas reutilizables al supermercado 🛍️",
    "Usar un vaso reutilizable ☕",
    "Evitar botellas de plástico de un solo uso 🧴",
    "Usar cubiertos reutilizables 🍴",
    "Llevar recipientes reutilizables 🍱",
    "Evitar bombillas/popotes de plástico 🥤",
    "Usar una bombilla reutilizable ♻️",
    "Comprar frutas sin envases plásticos 🍎",
    "Comprar verduras sin envases plásticos 🥕",
    "Comprar productos a granel 🛒",
    "Elegir productos con menos envoltorios 📦",
    "Preferir envases de vidrio 🫙",
    "Preferir envases de cartón 📦",
    "Usar bolsas de tela 👜",
    "Llevar una bolsa reutilizable en la mochila 🎒",
    "Rechazar bolsas innecesarias 🛍️",
    "Usar una lonchera reutilizable 🍱",
    "Usar platos reutilizables 🍽️",
    "Usar vasos de vidrio 🥛",
    "Evitar platos desechables 🍽️",
    "Evitar vasos plásticos desechables 🥤",
    "Evitar cubiertos desechables 🍴",
    "Evitar botellas pequeñas de agua 💧",
    "Llevar agua desde casa 🚰",
    "Usar un termo reutilizable 🧉",
    "Preparar bebidas en casa 🥤",
    "Preparar comida en casa 🍳",
    "Llevar comida en recipientes reutilizables 🍱",
    "Usar envoltorios reutilizables para alimentos 🥪",
    "Evitar alimentos con muchos envoltorios 🍬",
    "Elegir productos con envases reciclables ♻️",
    "Comprar productos en envases grandes cuando sea conveniente 📦",
    "Evitar productos con doble envoltorio 📦",
    "Comprar jabón en barra 🧼",
    "Comprar champú en barra 🧴",
    "Usar productos de limpieza recargables 🧽",
    "Comprar productos de limpieza a granel 🧹",
    "Usar paños reutilizables 🧽",
    "Evitar esponjas desechables 🧽",
    "Reutilizar recipientes de alimentos 🫙",
    "Usar frascos de vidrio para guardar alimentos 🫙",
    "Guardar alimentos en recipientes reutilizables 🍱",
    "Evitar bolsas para frutas cuando no sean necesarias 🍎",
    "Llevar bolsas reutilizables para frutas 🥕",
    "Comprar pan sin envoltorio plástico cuando sea posible 🥖",
    "Evitar productos envueltos individualmente 🍪",
    "Comprar alimentos frescos 🥦",
    "Preparar snacks en casa 🍎",
    "Llevar snacks en recipientes reutilizables 🍪",
    "Evitar pajitas de plástico 🥤",
    "Usar botellas metálicas 🥤",
    "Usar recipientes de acero inoxidable 🥣",
    "Usar utensilios de metal 🍴",
    "Evitar productos desechables 🗑️",
    "Reparar objetos en lugar de reemplazarlos 🔧",
    "Reutilizar envases antes de comprar nuevos ♻️",
    "Reutilizar bolsas varias veces 🛍️",
    "Reutilizar cajas 📦",
    "Evitar comprar productos con exceso de embalaje 📦",
    "Elegir productos duraderos 🔨",
    "Comprar ropa de buena duración 👕",
    "Reparar la ropa dañada 🧵",
    "Donar ropa que ya no utilizas 👕",
    "Comprar ropa de segunda mano 👚",
    "Reutilizar telas viejas 🧵",
    "Usar bolsas de tela para comprar ropa 👕",
    "Evitar accesorios con plástico desechable 👒",
    "Usar decoraciones reutilizables 🎉",
    "Evitar globos de plástico para decoraciones 🎈",
    "Usar adornos de papel reutilizable 🎊",
    "Usar vajilla reutilizable en fiestas 🍽️",
    "Evitar vasos desechables en reuniones 🥤",
    "Evitar platos desechables en celebraciones 🍽️",
    "Llevar recipientes propios para comida 🍱",
    "Usar cubiertos reutilizables fuera de casa 🍴",
    "Llevar una taza reutilizable al salir ☕",
    "Evitar comprar agua embotellada cuando haya agua potable 🚰",
    "Instalar un filtro de agua si es necesario 💧",
    "Usar dispensadores rellenables 🧴",
    "Comprar productos con envases recargables 🔄",
    "Elegir productos sin envoltorios innecesarios 📦",
    "Evitar productos de un solo uso ♻️",
    "Usar productos reutilizables en la escuela 🎒",
    "Llevar una botella reutilizable a clases 🥤",
    "Llevar una lonchera reutilizable a la escuela 🎒",
    "Evitar comprar bebidas en botellas plásticas en la escuela 🏫",
    "Usar lápices y útiles duraderos ✏️",
    "Evitar útiles escolares desechables 📚",
    "Reutilizar carpetas y materiales escolares 📁",
    "Comprar productos escolares sin exceso de plástico ✏️",
    "Usar bolsas reutilizables para compras pequeñas 🛍️",
    "Planificar las compras para evitar envases innecesarios 🛒",
    "Comprar solamente lo necesario 🛒",
    "Compartir objetos en lugar de comprar duplicados 🤝",
    "Prestar objetos reutilizables 🤝",
    "Intercambiar objetos con otras personas 🔄",
    "Enseñar a otras personas a reducir el plástico 🌎",
    "Participar en campañas para reducir plásticos 🌱",
    "Preferir productos reutilizables sobre desechables ♻️",
    "Crear un hábito de llevar siempre una botella reutilizable 🌎"
]
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy el EcoBot {bot.user}!')

@bot.command()
async def reducir(ctx):
    await ctx.send("Puedes " + random.choice(formas_reducir))

@bot.command()
async def reciclar(ctx):
    await ctx.send("Puedes " + random.choice(formas_reciclar))

bot.run("TU TOKEN AQUI")
