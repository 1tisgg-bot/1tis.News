import discord
from discord.ext import commands
import requests
import random
import os

# Noticia aleatoria.
def obtener_noticias_climaticas() -> str:
    """Obtiene una noticia aleatoria sobre el clima."""
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': 'cambio climático OR calentamiento global OR medio ambiente', # Búsqueda
        'language': 'es',             # En español
        'sortBy': 'relevancy',      # Las más relevantes primero
        'apiKey': "5a893f02a2f8444e93f866b03fd6a79d"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == 'ok' and data['totalResults'] > 0:
            
            # Tomamos una noticia aleatoria.
            articulos = data['articles'][:5]
            noticia = random.choice(articulos)
            
            titulo = noticia['title']
            url_noticia = noticia['url']
            fuente = noticia['source']['name']
            return f"📢 {titulo}\nFuente: {fuente}\n{url_noticia}"
        else:
            return "No encontré noticias recientes sobre el clima hoy. 🍃"
    except Exception as e:
        print(f"Error en API: {e}")
        return "Hubo un error al conectar con las noticias."

# Configuracion del bot

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# Respuestas del bot

@bot.event
async def on_ready():
     print("✅ Bot conectado como 1tis.GG")

# Comandos del bot

@bot.command()
async def hola(ctx):
    """Saludo inicial del bot."""
    await ctx.send("👋 ¡Hola! Soy 1tis.GG y estoy listo para darte algunos datos.")

@bot.command()
async def noticias(ctx):
    """Envía una noticia aleatoria sobre el clima."""
    hecho = obtener_noticias_climaticas()
    if not noticias:
        await ctx.send("algo anda mal...")
    else:
        await ctx.send(f"🤔 Noticia aleatoria: {hecho}")

# retos diarios.

@bot.command()
async def reto(ctx):
    retos = [
        # --- Ahorro de Energía ---
        "🕯️ Noche desconectada: Esta noche, evita usar pantallas 1 hora antes de dormir.",
        "🔌 Cazador de vampiros: Desconecta todos los aparatos que estén en 'stand-by' (luz roja) antes de salir.",
        "🌞 Luz natural: Hoy no enciendas ninguna bombilla hasta que sea totalmente de noche.",
        "❄️ Lavado en frío: Si pones la lavadora hoy, usa un ciclo de agua fría.",
        "🌡️ Ajuste térmico: Baja 1 grado la calefacción o sube 1 grado el aire acondicionado.",

        # --- Reducción de Residuos ---
        "🛍️ Sin bolsas: Ve a comprar algo y rechaza la bolsa de plástico (llévalo en la mano o mochila).",
        "🥤 Sin pajita/popote: Si pides una bebida hoy, di explícitamente 'sin pajita, por favor'.",
        "🍱 Cero desperdicio: Hoy trata de no generar ni un solo gramo de basura con tu almuerzo.",
        "🫙 Reutilización creativa: Busca un frasco de vidrio vacío y dale un nuevo uso (guardar lápices, especias, etc.).",
        "📰 Adiós papel: Cancela una suscripción de correo físico o factura en papel y pásala a digital.",
        "👖 Reparación: Cose ese botón suelto o arregla esa prenda en lugar de pensar en tirarla.",

        # --- Agua y Comida ---
        "🥦 Lunes sin carne: (Aunque no sea lunes) Hoy come 100% vegetariano.",
        "🚿 Reto de la canción: Tu ducha debe durar lo mismo que tu canción favorita (aprox 3-4 min).",
        "🪥 Grifo cerrado: Asegúrate de cerrar el grifo mientras te enjabonas las manos o te cepillas.",
        "🍎 Local: Compra una fruta o verdura que haya sido cultivada en tu propio país.",
        "💧 Termo: No compres agua embotellada hoy, rellena tu propia botella.",

        # --- Naturaleza y Aire Libre ---
        "🚶 Caminata: Si vas a un lugar que está a menos de 2km, ve andando.",
        "🚲 Sobre ruedas: Usa la bicicleta o patines para tu transporte principal de hoy.",
        "🌳 Conexión: Abraza un árbol o simplemente siéntate 5 minutos en un parque sin mirar el móvil.",
        "🚮 Héroe urbano: Recoge 3 plásticos o papeles que veas tirados en tu calle y tíralos al contenedor.",

        # --- Digital y Conciencia ---
        "📧 Limpieza digital: Borra 50 correos antiguos que no necesites (los servidores consumen mucha energía).",
        "🗣️ Influencer Eco: Comparte un dato sobre el cambio climático con un amigo o familiar hoy.",
        "📱 Modo oscuro: Activa el modo oscuro en todas tus apps para ahorrar batería en pantallas OLED.",
    ]
    await ctx.send(f"🏆 Tu reto de hoy es: {random.choice(retos)}")


# Paisajes aleatorios.

naturaleza = [
    "C:/Users/monte/Desktop/bot/nature/1.jpg",
    "C:/Users/monte/Desktop/bot/nature/2.jpg",
    "C:/Users/monte/Desktop/bot/nature/3.jpg",
    "C:/Users/monte/Desktop/bot/nature/4.jpg",
    "C:/Users/monte/Desktop/bot/nature/5.jpg",
    "C:/Users/monte/Desktop/bot/nature/6.jpg",
    "C:/Users/monte/Desktop/bot/nature/7.jpg",
    "C:/Users/monte/Desktop/bot/nature/8.jpg",
    "C:/Users/monte/Desktop/bot/nature/9.jpg",
    "C:/Users/monte/Desktop/bot/nature/10.jpg"
]


@bot.command()
async def paisaje(ctx):
    if not naturaleza:
        await ctx.send("❌ ¡Ups! No tengo ninguna imagen de naturaleza para mostrar en este momento.")
        return

    img = random.choice(naturaleza)

    try:
        with open(img, 'rb') as f:
            nombre_archivo = os.path.basename(img)
            archivo_discord = discord.File(f, filename=nombre_archivo)
            
            await ctx.send(
                content = " ¡Aquí tienes un hermoso paisaje para tu día! 💚", 
                file = archivo_discord 
            )
    except FileNotFoundError:
        await ctx.send(f"⚠️ ¡Error! No pude encontrar la imagen en la ruta: `{img}`. Por favor, revisa la ruta.")
    except Exception as e:
        await ctx.send(f"❌ Ocurrió un error al intentar enviar la imagen: `{e}`")


# Tips para cuidar el medio ambiente

@bot.command()
async def tips(ctx):
    """Envía un consejo aleatorio sobre el cuidado del medio ambiente."""
    
    consejos = [
        "Usa botellas de agua reutilizables en lugar de comprar botellas de plástico.",
        "Apaga las luces cuando salgas de una habitación.",
        "Cierra el grifo mientras te cepillas los dientes.",
        "Desconecta los aparatos electrónicos cuando no los estés usando.",
        "Usa bolsas de tela para tus compras en lugar de bolsas de plástico.",
        "Separa la basura: recicla papel, vidrio, plástico y cartón.",
        "Reduce el consumo de carne; la ganadería intensiva contamina mucho.",
        "Usa el transporte público, camina o usa bicicleta siempre que puedas.",
        "Planta un árbol o ten plantas en casa; ayudan a purificar el aire.",
        "Evita los productos de un solo uso como cubiertos y platos desechables.",
        "Dúchate en lugar de bañarte y trata de hacerlo en menos de 5 minutos.",
        "Aprovecha la luz natural del día para no encender bombillas.",
        "Compra productos locales y de temporada para reducir la huella de carbono.",
        "Repara tu ropa o dónala en lugar de tirarla.",
        "Usa pilas recargables en lugar de desechables.",
        "Evita imprimir documentos si no es estrictamente necesario.",
        "Usa servilletas de tela en lugar de servilletas de papel.",
        "No tires aceite usado por el desagüe; guárdalo y llévalo a un punto limpio.",
        "Instala bombillas LED de bajo consumo en tu casa.",
        "Lava la ropa con agua fría para ahorrar energía.",
        "Seca la ropa al aire libre en lugar de usar secadora.",
        "Compra a granel para evitar envases innecesarios.",
        "Lleva tu propia taza de café si compras para llevar.",
        "No dejes el cargador del móvil enchufado si no estás cargando nada.",
        "Usa recipientes de vidrio para guardar comida en lugar de film plástico.",
        "Recoge la basura que veas en la naturaleza cuando salgas a pasear.",
        "Evita el uso de pesticidas químicos en tu jardín.",
        "Composta tus residuos orgánicos para crear abono natural.",
        "Reutiliza frascos de vidrio para almacenar cosas.",
        "Dona juguetes, libros y muebles que ya no uses.",
        "Usa papel reciclado siempre que sea posible.",
        "Configura tu ordenador en modo ahorro de energía.",
        "No uses pajitas (popotes) de plástico; usa de metal o bambú.",
        "Cierra bien las ventanas si tienes la calefacción o el aire acondicionado encendido.",
        "Revisa que no haya fugas de agua en tus grifos o tuberías.",
        "Usa jabones y detergentes biodegradables.",
        "Evita comprar frutas y verduras que vengan envueltas en plástico.",
        "Lleva tu almuerzo en recipientes reutilizables.",
        "Comparte coche (carpooling) si tienes que ir lejos.",
        "Infórmate y educa a otros sobre el cambio climático.",
        "Apoya a empresas que sean responsables con el medio ambiente.",
        "Usa el modo 'eco' en tu lavadora y lavavajillas.",
        "No tires colillas de cigarro al suelo; contaminan el agua.",
        "Usa cepillos de dientes de bambú en lugar de plástico.",
        "Reduce el brillo de tu monitor para ahorrar energía.",
        "Borra correos electrónicos antiguos; almacenarlos consume energía en servidores.",
        "Usa una olla a presión para cocinar; ahorra tiempo y energía.",
        "Tapa las ollas al cocinar para aprovechar mejor el calor.",
        "Evita el 'fast fashion' y compra ropa de mejor calidad que dure más.",
        "¡Sé el cambio que quieres ver en el mundo! Cada pequeña acción cuenta."
    ]
    
    consejo_aleatorio = random.choice(consejos)
    await ctx.send(f"💡 Consejo Eco: {consejo_aleatorio}")


# Comando "help" para explicar las funciones del bot.

@bot.command()
async def help(ctx):

    embed = discord.Embed(
        title ="📚 Guía de Comandos | 1tis.GG 🌍",
        description ="¡Hola! Soy tu asistente ecológico. Usa los siguientes comandos para aprender y ayudar al planeta:",
        color=discord.Color.green()
    )
    
    # --- Comandos de Información ---
    embed.add_field(
        name="📰 Información y Saludo",
        value="""
        `!hola`: Saludo inicial del bot.
        `!noticias`: Muestra un titular reciente sobre el clima o medio ambiente.
        """
    )

    # --- Comandos de Acción y Motivación ---
    embed.add_field(
        name="💡 Acción Diaria",
        value="""
        `!tips`: Envía un consejo aleatorio para cuidar el medio ambiente.
        `!reto`: Te asigna un desafío ecológico específico para hacer hoy.
        """
    )
    
    # --- Comando de Entretenimiento ---
    embed.add_field(
        name="🏞 Naturaleza",
        value="""
        `!paisaje`: Te envía una imagen aleatoria de la naturaleza para inspirarte.
        """
    )

    embed.set_footer(text="¡Cada pequeña acción cuenta para salvar el planeta!")
    
    # Enviamos el Embed al canal
    await ctx.send(embed=embed)

#TOKEN DEL BOT

