import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ui import Select,view
from discord.utils import get
from discord.ext.commands import Bot


perfix="!!"
client=commands.Bot(command_prefix=commands.when_mentioned_or("Minetrack "))
client.remove_command("help")
colors = [0x01b8a1, 0xaa0e6c, 0x390174, 0xf6fa02, 0x5df306, 0x2206f3, 0xfffdfd, 0xff0a0e, 0x850000, 0xe76868, 0x4eca75, 0xb38203, 0xc44400, 0x000000, 0x0517dd, 0x6c6f92, 0x144900, 0xffffff, 0x020246, 0xe209b7, 0x0976e2, 0x3de209, 0xe29209, 0x08a247]
intents = discord.Intents.all()


@client.event
async def on_ready():
    print ("\033[96m bot is ready - https://github.com/MineTrack")
    await client.change_presence(activity=discord.Activity(status=discord.Status.idle , type=discord.ActivityType.watching, name="https://github.com/MineTrack"))


#onlinei?
@client.slash_command(name="online", description="✅ آنلاینی؟")
async def online(ctx):
    await ctx.respond(f"Im online",ephemeral=True)

# info #
#---------------------------------------#
# made by minetrack #


class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select( 
        placeholder = "Select One Options From Menu", 
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="View Rules", 
                emoji="<:7693bluedot:1034926606407434291>"
            ),
            discord.SelectOption(
                label="Read Information",
                emoji="<:3656blurpledot:1034926612245925908>"
            ),
            discord.SelectOption(
                label="Frequently Asked Questions",
                emoji="<:7693bluedot:1034926606407434291>"
            ),
            discord.SelectOption(
                label="How To Trust",
                emoji="<:3656blurpledot:1034926612245925908>"
            ),
            discord.SelectOption(
                label="Products",
                emoji="<:7693bluedot:1034926606407434291>"
            ),
            discord.SelectOption(
                label="Create Ticket",
                emoji="<:3656blurpledot:1034926612245925908>"
            ),
            discord.SelectOption(
                label="Donate Us",
                emoji="<:7693bluedot:1034926606407434291>"
            ),
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        if select.values[0] == "View Rules": # ----> if action (line 55 label = select.values[0])
            await interaction.response.send_message(f"your text",ephemeral=True) 
        if select.values[0] == "Read Information": 
            await interaction.response.send_message(f"your text",ephemeral=True)
        if select.values[0] == "Frequently Asked Questions": 
            await interaction.response.send_message(f"your text",ephemeral=True)
        if select.values[0] == "How To Trust": 
            await interaction.response.send_message(f"your text",ephemeral=True)
        if select.values[0] == "Products": 
            await interaction.response.send_message(f"your text",ephemeral=True)
        if select.values[0] == "Create Ticket": 
            await interaction.response.send_message(f"your text",ephemeral=True)
        if select.values[0] == "Donate Us": 
            await interaction.response.send_message(f"your text",ephemeral=True)

@client.slash_command(timeout=None) #panel of info
async def info(ctx):
    embed=discord.Embed(title="Your Text", description=f"this is test text", color=0xC55FFC)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/1020732809419182090/1022149359720218745/sadada.png")
    embed.set_footer(text='https://github.com/MineTrack')
    await ctx.respond("Info Panel Has Created! https://github.com/MineTrack",ephemeral=True)
    await ctx.send(embed=embed, view=MyView())


# info #
#---------------------------------------#
# made by minetrack #


client.run("TOKEN")

