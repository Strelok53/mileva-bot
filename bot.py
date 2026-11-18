import os
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


# Definišemo GIF-ove za svaku stavku
GIF_SLJIVA = "https://media.giphy.com/media/8vUEXZA2me7vnuUvrs/giphy.gif"
GIF_PIVO = "https://media.giphy.com/media/13CoXDiaCcCoyY/giphy.gif"
GIF_CEVAPI = "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif"
GIF_KARADJORDJEVA = "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif"
GIF_SALATA = "https://media.giphy.com/media/3o7bu3hJmCG910E1EI/giphy.gif"
GIF_KAFA = "https://media.giphy.com/media/J20Z2SH5WmCnzSrbqA/giphy.gif"

MEMES = [
    "https://i.imgur.com/Kz6u79n.jpg",
    "https://i.imgur.com/wV2Q98t.jpg",
    "https://i.imgur.com/3X12vQz.jpg",
]


@bot.event
async def on_ready():
    print(f"Mileva je spremna! Ulogovana kao {bot.user}")


# 1. Osnovne komande
@bot.command(name="zdravo")
async def zdravo(ctx):
    await ctx.send(f"Zdravo {ctx.author.mention}! Šta ćeš da popiješ? 🍻")


@bot.command(name="meme")
async def meme(ctx):
    slika = random.choice(MEMES)
    await ctx.send(slika)


# 2. Glavni meni pregled (!meni)
@bot.command(name="meni")
async def meni(ctx):
    embed = discord.Embed(
        title="📜 Kafanski Meni — Kod Mileve",
        description="Izvoli, izaberi šta ti duša ište:",
        color=discord.Color.gold(),
    )
    embed.add_field(
        name="1. 🥃 Domaća šljivovica",
        value="Prepečenica iz dedinog podruma — **150 din** (`!sljiva`)",
        inline=False,
    )
    embed.add_field(
        name="2. 🍺 Hladno točeno pivo (0.5l)",
        value=(
            "Orošena krigla pravo iz frižidera — **220 din** (`!pivo`)"
        ),
        inline=False,
    )
    embed.add_field(
        name="3. 🥩 Ćevapi na kajmaku (10 kom)",
        value=(
            "Domaća lepinja, luk i kajmak — **650 din** (`!cevapi`)"
        ),
        inline=False,
    )
    embed.add_field(
        name="4. 🥓 Karađorđeva šnicla",
        value=(
            "Sa pomfritom i tartar sosom — **890 din** (`!karadjordjeva`)"
        ),
        inline=False,
    )
    embed.add_field(
        name="5. 🥗 Šopska salata",
        value=(
            "Svež paradajz, krastavac i ovčiji sir — **280 din** (`!salata`)"
        ),
        inline=False,
    )
    embed.add_field(
        name="6. ☕ Domaća kafa i ratluk",
        value=(
            "Za otrežnjenje posle fajronta — **120 din** (`!kafa`)"
        ),
        inline=False,
    )
    embed.set_footer(
        text="Kucaj komandu u zagradi da poručiš željenu stavku!"
    )
    await ctx.send(embed=embed)


# --- POJEDINACNE KOMANDE ZA SVAKU STAVKU ---

# 1. Šljivovica (!sljiva)
@bot.command(name="sljiva")
async def sljiva(ctx):
    embed = discord.Embed(
        title="🥃 Domaća šljivovica",
        description="Prepečenica iz dedinog podruma, greje dušu!",
        color=discord.Color.orange(),
    )
    embed.add_field(name="Cena", value="— **150 din**", inline=False)
    await ctx.send(
        f"Živeli, {ctx.author.mention}! Stiže jedna ljuta! 🥃", embed=embed
    )
    await ctx.send(GIF_SLJIVA)


# 2. Pivo (!pivo)
@bot.command(name="pivo")
async def pivo(ctx):
    embed = discord.Embed(
        title="🍺 Hladno točeno pivo (0.5l)",
        description="Orošena krigla, taman za ove vrućine.",
        color=discord.Color.gold(),
    )
    embed.add_field(name="Cena", value="— **220 din**", inline=False)
    await ctx.send(
        f"Stiže jedno hladno točeno za {ctx.author.mention}! 🍺", embed=embed
    )
    await ctx.send(GIF_PIVO)


# 3. Ćevapi (!cevapi)
@bot.command(name="cevapi")
async def cevapi(ctx):
    embed = discord.Embed(
        title="🥩 Ćevapi na kajmaku (10 kom)",
        description="Domaća lepinja, sitno seckan luk i topao kajmak.",
        color=discord.Color.red(),
    )
    embed.add_field(name="Cena", value="— **650 din**", inline=False)
    await ctx.send(
        f"Evo svežih ćevapa sa skare za {ctx.author.mention}! 🥩", embed=embed
    )
    await ctx.send(GIF_CEVAPI)


# 4. Karađorđeva šnicla (!karadjordjeva)
@bot.command(name="karadjordjeva")
async def karadjordjeva(ctx):
    embed = discord.Embed(
        title="🥓 Karađorđeva šnicla",
        description="Kraljevski uštipak punjen kajmakom, sa pomfritom i tartar sosom.",
        color=discord.Color.dark_gold(),
    )
    embed.add_field(name="Cena", value="— **890 din**", inline=False)
    await ctx.send(
        f"Gospođska porcija Karađorđeve za {ctx.author.mention}! 🥓", embed=embed
    )
    await ctx.send(GIF_KARADJORDJEVA)


# 5. Šopska salata (!salata)
@bot.command(name="salata")
async def salata(ctx):
    embed = discord.Embed(
        title="🥗 Šopska salata",
        description="Svež paradajz, krastavac, paprika i brdo rendanog ovčijeg sira.",
        color=discord.Color.green(),
    )
    embed.add_field(name="Cena", value="— **280 din**", inline=False)
    await ctx.send(
        f"Da se osvežiš, {ctx.author.mention}! Evo domaće šopske. 🥗",
        embed=embed,
    )
    await ctx.send(GIF_SALATA)


# 6. Kafa (!kafa)
@bot.command(name="kafa")
async def kafa(ctx):
    embed = discord.Embed(
        title="☕ Domaća kafa i ratluk",
        description="Sveže kuvana domaća iz džezve, sa ratlukom.",
        color=discord.Color.from_rgb(139, 69, 19),
    )
    embed.add_field(name="Cena", value="— **120 din**", inline=False)
    await ctx.send(
        f"Evo jedne domaće za otrežnjenje, {ctx.author.mention}! ☕", embed=embed
    )
    await ctx.send(GIF_KAFA)

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

# --- NOVA IGRA: POGAĐANJE KAFANSKIH REČI ---

# Reči koje bot može da zamisli
KAFANSKE_RECI = [
    "rakija",
    "kafana",
    "kelner",
    "burek",
    "pivo",
    "harmonika",
    "meze",
    "prase",
]

# Rečnik da pratimo aktivnu igru na serveru
aktivne_igre = {}


@bot.command(name="pokreni_igru")
async def pokreni_igru(ctx):
  # Izaberi nasumičnu reč
  tajna_rec = random.choice(KAFANSKE_RECI)
  # Zapamti reč za ovaj server/kanal
  aktivne_igre[ctx.guild.id] = {
      "rec": tajna_rec,
      "pogodjeno": ["_"] * len(tajna_rec),
      "promasaji": 0,
  }

  prikaz = " ".join(aktivne_igre[ctx.guild.id]["pogodjeno"])
  await ctx.send(
      f"🎮 **Nova kafanska igra je počela!**\n"
      f"Mileva je zamislila reč od **{len(tajna_rec)}** slova: `{prikaz}`\n"
      f"Pogađaj slovo komandom: `!slovo [slovo]` (na primer `!slovo a`)"
  )


@bot.command(name="slovo")
async def pogodite_slovo(ctx, slovo: str = None):
  if ctx.guild.id not in aktivne_igre:
    await ctx.send(
        "⚠️ Trenutno nema aktivne igre! Pokreni je komandom `!pokreni_igru`."
    )
    return

  if not slovo or len(slovo) != 1:
    await ctx.send("❌ Moraš da uneseš tačno **jedno slovo**! Primer: `!slovo k`")
    return

  slovo = slovo.lower()
  igra = aktivne_igre[ctx.guild.id]
  tajna_rec = igra["rec"]

  if slovo in tajna_rec:
    # Otkrij slovo na svim pozicijama gde se nalazi
    for i, s in enumerate(tajna_rec):
      if s == slovo:
        igra["pogodjeno"][i] = slovo

    prikaz = " ".join(igra["pogodjeno"])

    # Proveri da li je cela reč pogođena
    if "_" not in igra["pogodjeno"]:
      await ctx.send(
          f"🎉 Bravo {ctx.author.mention}! Pogodio/la si celu reč: **{tajna_rec}**!"
          " Mileva te časti pićem! 🍻"
      )
      del aktivne_igre[ctx.guild.id]  # Završi igru
    else:
      await ctx.send(
          f"✅ Bravo! Slovo **{slovo}** je u reči: `{prikaz}`\nSamo tako"
          " nastavi!"
      )
  else:
    igra["promasaji"] += 1
    prikaz = " ".join(igra["pogodjeno"])
    await ctx.send(
        f"❌ Nema slova **{slovo}**! Trenutno stanje: `{prikaz}` (Greške:"
        f" {igra['promasaji']}/5)"
    )

    if igra["promasaji"] >= 5:
      await ctx.send(
          f"💀 Propali ste! Mileva je popila sve zbog vaših promašaja. Tražena"
          f" reč je bila: **{tajna_rec}**."
      )
      del aktivne_igre[ctx.guild.id]


# Ovde nalepi svoj pravi token
bot.run(os.getenv("TOKEN"))