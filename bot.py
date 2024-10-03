import discord
from discord.ext import commands
import io
from PIL import Image, ImageDraw, ImageFont
import requests
l1ve709token = "YOUR TOKEN HERE"  # TOKEN HERE
intents = discord.Intents.all()
l1ve709 = commands.Bot(command_prefix='.', intents=intents, help_command=None)
idler = {
    "kayıt_kanal_id": 1287811906467266580 # CHANNEL ID HERE
}

def arka_plan_simge(url):
    response = requests.get(url)
    background = Image.open(io.BytesIO(response.content)).convert("RGBA")
    return background

@l1ve709.event
async def on_ready():
    print(f'{l1ve709.user.name}')

@l1ve709.event
async def on_member_join(member):
    if not idler["kayıt_kanal_id"]:
        return
    
    kayıt_kanalı = l1ve709.get_channel(idler["kayıt_kanal_id"])
    
    if not kayıt_kanalı:
        print("kanal bulunamadı")
        return

    arkaplan_urlsi = "https://media.discordapp.net/attachments/1291134989466992711/1291187158874460160/a-photo-of-a-90-degree-angle-shot-of-a-highway-in--bFNb-rTgQqGcjPlBUBEYQg-8wz-x3kgTFC6WtfJ-IHRzg.jpg?ex=66ff2f3f&is=66fdddbf&hm=b67b28eeb00c5e442625bb3f8974340e18210f2fb473a87c83e3522af56f1fb7&=&format=webp&width=843&height=473"
    background = arka_plan_simge(arkaplan_urlsi).resize((900, 450))

    asset = member.avatar.url if member.avatar else member.default_avatar.url
    response = requests.get(asset)
    profile_image = Image.open(io.BytesIO(response.content)).resize((190, 190)).convert("RGBA")

    mask = Image.new("L", profile_image.size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0) + profile_image.size, fill=255)
    profile_image.putalpha(mask)

    background.paste(profile_image, (360, 270), profile_image)

    draw = ImageDraw.Draw(background)

    try:
        font_large = ImageFont.truetype("arial.ttf", 65) 
        font_small = ImageFont.truetype("arial.ttf", 35)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    hosgeldin = "Hoş Geldin"
    kullanici_adi = f"{member.name}!"
    member_count = f"Üye Sayısı: {len(member.guild.members)}"

    draw.text((20, 20), hosgeldin, font=font_large, fill=(255, 215, 0), stroke_width=2, stroke_fill=(0, 0, 0))  
    draw.text((20, 100), kullanici_adi, font=font_large, fill=(0, 255, 0), stroke_width=2, stroke_fill=(0, 0, 0))  
    draw.text((20, 180), member_count, font=font_small, fill=(220, 220, 220), stroke_width=1, stroke_fill=(50, 50, 50))

    buffer = io.BytesIO()
    background.save(buffer, format='PNG')
    buffer.seek(0)

    await kayıt_kanalı.send(
        f"Merhaba <@{member.id}>, ben **{l1ve709.user.name}**, sunucumuzun dijital asistanı. 🤖\n"
        f"Sunucumuza **hoş geldin!** 🎉 Seninle tanıştığımıza çok sevindik! Sunucumuzun tam **{len(member.guild.members)}.** üyesi oldun ve bu topluluğa katıldın. 🏆\n\n"
        f"Hesabın **{member.created_at.strftime('%d %B %Y')}** tarihinde açılmış, ve şimdi bizlerle birliktesin. Bu yolculukta seni desteklemek için buradayım.\n\n"
        f"⚠️ **İlk Adımlar:** Sunucumuzun kurallarını gözden geçirmeyi unutma. Herkesin güvenli ve eğlenceli bir deneyim yaşaması için bu kurallara uymanı rica ederiz. <#1291129276053196874>\n\n"
        f"📢 **Bilgilendirme:** Sunucumuzda düzenli olarak etkinlikler, çekilişler ve özel sohbetler düzenleniyor. Güncel kalmak için kanallarımızı takip et.\n\n"
        f"📌 **Kayıt Yetkilisi:** <@&1291125123507818568> Kayıt yetkilimiz seninle en kısa sürede ilgilenecektir.\n\n"
        f"Eğer bir sorunun olursa, ben her zaman buradayım. İyi eğlenceler dilerim! 🌟", 
        file=discord.File(buffer, "atlanta.png")
    )

@l1ve709.command()
async def ayarla(ctx, kanal: discord.TextChannel):
    idler["kayıt_kanal_id"] = kanal.id
    await ctx.send(f"Karşılama kanalı artık: **{kanal.name}** ✅"),
    

l1ve709.run(l1ve709token)
