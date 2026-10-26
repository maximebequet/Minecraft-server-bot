import os
import discord
from discord.ext import commands
from wakeonlan import send_magic_packet

# Retrieve environment variables for security
TOKEN = os.getenv("DISCORD_TOKEN")
MAC_ADDRESS = os.getenv("MAC_ADDRESS")  # Example format: "AA:BB:CC:DD:EE:FF"
PUBLIC_IP = os.getenv("HOME_IP")        # Your home public IP address or DDNS hostname

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command(name="start")
async def start_server(ctx):
    try:
        # Sends UDP magic packet on port 9 to your home network broadcast address
        send_magic_packet(MAC_ADDRESS, ip_address=PUBLIC_IP, port=9)
        await ctx.send("🚀 **Wake-on-LAN packet sent!** The PC is waking up and launching the Minecraft server. Try connecting in 1–2 minutes.")
    except Exception as e:
        await ctx.send(f"❌ **Failed to send wake packet:** `{e}`")

if __name__ == "__main__":
    bot.run(TOKEN)
