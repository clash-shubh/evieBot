import discord


TOKEN = 'NDcyNjY4NjE1MjI1OTAxMDU2.DkWXug.W7WabqmGdV3ETBtdweL0QU91LYc'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} :wave:'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!ping'):
        for user in message.mentions:
            msg = 'PONG {}'.format(user.mention)
            await client.send_message(message.channel, msg)
            
    if message.content.startswith('!author'):
        msg='I was created by @clashshubh#7547'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!invite'):
        msg='https://discordapp.com/oauth2/authorize?&client_id=472668615225901056&scope=bot&permissions=8'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        msg = '{0.author.mention} sorry the author is lazy to put help text'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!servers'):
        msg ='no. of servers i serve = {}'.format(len(client.servers))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!nameservers'):
        for server in client.servers:
            await client.send_message(message.channel, server)

    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
   # print(discord.utils.oauth_url(bott))
    print('------')
    

client.run(TOKEN)
