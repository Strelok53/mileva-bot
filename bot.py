import os
bot.run(os.environ{'TOKEN'})
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MEMES = [
    "https://i.imgur.com/Kz6u79n.jpg",
    "https://i.imgur.com/wV2Q98t.jpg",
    "https://i.imgur.com/3X12vQz.jpg",
]


@bot.event
async def on_ready():
    print(f"Mileva je spremna! Ulogovana kao {bot.user}")


@bot.command(name="zdravo")
async def zdravo(ctx):
    await ctx.send(f"Zdravo {ctx.author.mention}! Šta ćeš da popiješ? 🍻")


@bot.command(name="pivo")
async def pivo(ctx):
    await ctx.send(f"Stiže jedno hladno za {ctx.author.name}! 🍺")

# Definišemo GIF za kafu
GIF_KAFA = "https://media.giphy.com/media/J20Z2SH5WmCnzSrbqA/giphy.gif"


# Komanda za kafu: !kafa
@bot.command(name="kafa")
async def kafa(ctx):
  embed = discord.Embed(
      title="☕ Domaća kafa i ratluk",
      description=(
          "Sveže kuvana domaća kafa iz džezve, sa kockom šećera i ratlukom sa"
          " orasima!"
      ),
      color=discord.Color.from_rgb(139, 69, 19),  # Braon kafanska boja
  )

  embed.add_field(name="Cena", value="— **120 din**", inline=False)
  embed.set_footer(text="Idealno za otrežnjenje posle fajronta.")

  # Šalje poruku, embed i GIF
  await ctx.send(f"Evo jedne domaće za otrežnjenje, {ctx.author.mention}! ☕", embed=embed)
  await ctx.send(GIF_KAFA)

# Definišemo GIF za ćevape


# Komanda za ćevape: !cevapi
@bot.command(name="cevapi")
async def cevapi(ctx):
  embed = discord.Embed(
      title="🥩 Domaći ćevapi sa kajmakom",
      description=(
          "Sočni roštilj sa vrućom lepinjom, sitno seckanim lukom i domaćim"
          " kajmakom!"
      ),
      color=discord.Color.red(),
  )

  embed.add_field(name="Mala porcija (5 kom)", value="— **350 din**", inline=False)
  embed.add_field(
      name="Velika porcija (10 kom)", value="— **650 din**", inline=False
  )
  embed.set_footer(text="Mileva ih vadi direktno sa skare!")

  # Šalje Embed meni i GIF u istoj poruci
  await ctx.send(
      f"Stiže roštilj za {ctx.author.mention}! 🥩", embed=embed
  )



@bot.command(name="meme")
async def meme(ctx):
    slika = random.choice(MEMES)
    await ctx.send(slika)


# Kafanski meni
@bot.command(name="meni")
async def meni(ctx):
    embed = discord.Embed(
        title="📜 Kafanski Meni — Kod Mileve",
        description="Izvoli, izaberi šta ti duša ište:",
        color=discord.Color.gold(),
    )
    embed.add_field(
        name="1. 🥃 Domaća šljivovica",
        value="Prepečenica iz dedinog podruma — **150 din**",
        inline=False,
    )
    embed.add_field(
        name="2. 🍺 Hladno točeno pivo (0.5l)",
        value="Orošena krigla pravo iz frižidera — **220 din**",
        inline=False,
    )
    embed.add_field(
        name="3. 🥩 Ćevapi na kajmaku (10 kom)",
        value="Domaća lepinja, luk i kajmak — **650 din**",
        inline=False,
    )
    embed.add_field(
        name="4. 🥓 Karađorđeva šnicla",
        value="Sa pomfritom i tartar sosom — **890 din**",
        inline=False,
    )
    embed.add_field(
        name="5. 🥗 Šopska salata",
        value="Svež paradajz, krastavac i ovčiji sir — **280 din**",
        inline=False,
    )
    embed.add_field(
        name="6. ☕ Domaća kafa i ratluk",
        value="Za otrežnjenje posle fajronta — **120 din**",
        inline=False,
    )
    embed.set_footer(text="Za porudžbine samo vikni Milevu!")
    await ctx.send(embed=embed)


# Nova igra: Pogađanje brojeva (!broj <1-10>)
@bot.command(name="broj")
async def igra_brojeva(ctx, izabrani_broj: int = None):
    if izabrani_broj is None:
        await ctx.send(
            "⚠️ Moraš da uneseš broj od 1 do 10! Primer: `!broj 7`"
        )
        return

    if izabrani_broj < 1 or izabrani_broj > 10:
        await ctx.send(
            "❌ Igra se igra samo sa brojevima od **1 do 10**! Probaj ponovo."
        )
        return

    tajni_broj = random.randint(1, 10)

    if izabrani_broj == tajni_broj:
        await ctx.send(
            f"🎉 Bravo {ctx.author.mention}! Pogodio/la si! Mileva časti pićem! 🍻 (Izabrao si {izabrani_broj}, a tajni broj je bio {tajni_broj})."
        )
    else:
        await ctx.send(
            f"❌ Nisi imao sreće ovaj put, {ctx.author.name}. Ti si izabrao **{izabrani_broj}**, a Mileva je zamislila **{tajni_broj}**. Više sreće drugi put!"
        )
@bot.command(name="kafana")
async def kafana_info(ctx):
    # Običan tekst
    await ctx.send(
        "Radno vreme kafane je 24/7! Naruči piće uz komandu `!pivo` ili pogledaj mim uz `!meme`."
    )
    
    
   # Automatska dobrodošlica kada član uđe na server
@bot.event
async def on_member_join(member):
  # Pronalazi prvi tekstualni kanal na serveru i šalje poruku
  for kanal in member.guild.text_channels:
    # Možeš zameniti "general" sa imenom kanala gde želiš da Mileva dočekuje goste
    if kanal.name == "general":
      await kanal.send(
          f"Vrata su se otvorila! Dobro došao/la u kafanu 'Kod Mileve', "
          f"{member.mention}! 🍻 Sedi, naruči nešto hladno i opusti se!"
      )
      break

# Ovde nalepi svoj pravi token
bot.run(os.environ['TOKEN'])