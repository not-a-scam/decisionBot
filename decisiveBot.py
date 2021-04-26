import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='team', help='Generates teams from your current voice channel', aliases=['t'])
async def team(ctx, no_of_teams: int):
    guild = ctx.guild
    author = ctx.author
    checker = 0
    members = []
    for voice_channel in guild.voice_channels:
        if author in voice_channel.members:
            members = voice_channel.members.copy()
            checker = 1
            break

    if checker == 0:
        await ctx.send('You must be in a voice channel for this command to work!')
        return

    for member in members:
        if member.bot:
            members.remove(member)

    per_team_members = len(members) // no_of_teams
    no_of_extra_members = len(members) - (per_team_members * no_of_teams)
    teams = []
    random.shuffle(members)
    for x in range(no_of_teams):
        var_team = []
        for y in range(per_team_members):
            var_team.append(members.pop().name)
        teams.append(var_team)

    for x in range(no_of_extra_members):
        teams[x].append(members.pop().name)

    for index, team_ in enumerate(teams):
        await ctx.send(f'Team {index + 1}: {", ".join(team_)}')


@bot.command(name='map', help='Generates a random map!')
async def rand_map(ctx, game):
    game = game.lower()
    if game == 'valorant' or game == 'val':
        maps = ['Icebox', 'Split', 'Ascent', 'Bind', 'Haven']
        await ctx.send(f'Map generated: {random.choice(maps)}')
        return
    else:
        await ctx.send('Game does not exist/ is not supported!')


@bot.command(name='character', help='Generates a random character', aliases=['c'])
async def rand_char(ctx, *args):
    game = args[0].lower()
    char_type = ''
    if len(args) >= 2:
        char_type = args[1].lower()
    if game == 'valorant' or game == 'val':
        duelist = ['Jett', 'Phoenix', 'Raze',
                   'Reyna', 'Yoru']

        sentinel = ['Sage', 'Killjoy', 'Cypher']

        controller = ['Astra', 'Brimstone', 'Omen', 'Viper']

        initiator = ['Sova', 'Breach', 'Skye']

        characters = duelist + sentinel + controller + initiator

        if char_type == 'duelist' or char_type == 'duel' or char_type == 'd':
            await ctx.send(f'Character Generated: {random.choice(duelist)}')
            return

        elif char_type == 'sentinel' or char_type == 'senti' or char_type == 's':
            await ctx.send(f'Character Generated: {random.choice(sentinel)}')
            return

        elif char_type == 'controller' or char_type == 'cont' or char_type == 'c':
            await ctx.send(f'Character Generated: {random.choice(controller)}')
            return

        elif char_type == 'initiator' or char_type == 'init' or char_type == 'i':
            await ctx.send(f'Character Generated: {random.choice(initiator)}')
            return

        else:
            await ctx.send(f'Character Generated: {random.choice(characters)}')
            return

    elif game == 'pala' or game == 'paladins':
        front_line = ['Ash', 'Atlas', 'Barik', 'Fernando', 'Inara',
                      'Khan', 'Makoa', 'Raum', 'Ruckus', 'Terminus',
                      'Torvald', 'Yagorath']

        damage = ['Bomb King', 'Cassie', 'Dredge',
                  'Drogoz', 'Imani', 'Kinessa',
                  'Lian', 'Octavia', 'Sha Lin',
                  'Strix', 'Tiberius', 'Tyra',
                  'Viktor', 'Vivian', 'Willo']

        support = ['Corvus', 'Furia', 'Grohk',
                   'Grover', 'Io', 'Jenos', 'Mal\'Damba',
                   'Pip', 'Seris', 'Ying']

        flank = ['Androxus', 'Buck', 'Evie', 'Koga',
                 'Lex', 'Maeve', 'Moji', 'Skye',
                 'Talus', 'Vora', 'Zhin']

        characters = front_line + damage + support + flank

        if char_type == 'frontline' or char_type == 'fl':
            await ctx.send(f'Character Generated: {random.choice(front_line)}')
            return

        elif char_type == 'damage' or char_type == 'd':
            await ctx.send(f'Character Generated: {random.choice(damage)}')
            return
        elif char_type == 'support' or char_type == 's':
            await ctx.send(f'Character Generated: {random.choice(support)}')
            return
        elif char_type == 'flank' or char_type == 'f':
            await ctx.send(f'Character Generated: {random.choice(flank)}')
            return
        else:
            await ctx.send(f'Character Generated: {random.choice(characters)}')
            return

    elif game == 'apex':
        characters = ['Fuse', 'Bangalore', 'Bloodhound',
                      'Caustic', 'Crypto', 'Gibraltar',
                      'Horizon', 'Lifeline', 'Loba',
                      'Mirage', 'Octane', 'Pathfinder',
                      'Rampart', 'Revenant', 'Wattson',
                      'Wraith']
        await ctx.send(f'Character Generated: {random.choice(characters)}')
    else:
        await ctx.send('Game does not exist/ is not supported!')


@bot.command(name='coinflip', help='Flips a coin!', aliases=['cf'])
async def rand_char(ctx):
    choices = ['Heads', 'Tails']
    await ctx.send(f'Coin shows: {random.choice(choices)}')
    return


@bot.command(name='choose', help='Chooses someone!')
async def choose(ctx):
    guild = ctx.guild
    author = ctx.author
    checker = 0
    members = []
    member_names = []

    for voice_channel in guild.voice_channels:
        if author in voice_channel.members:
            members = voice_channel.members.copy()
            checker = 1
            break

    if checker == 0:
        await ctx.send('You must be in a voice channel for this command to work!')
        return

    for member in members:
        if member.bot:
            members.remove(member)
        else:
            member_names.append(member.name)

    await ctx.send('I choose you, {}!'.format(random.choice(member_names)))


@bot.command(name='weapon', help='Generates a random character', aliases=['w'])
async def rand_weapon(ctx, *args):
    game = args[0].lower()
    if len(args) >= 2:
        weap_type = args[1].lower()
    else:
        weap_type = 'None'
    if game == 'valorant' or game == 'val':
        primary = ['Spectre', 'Stinger', 'Bucky', 'Judge', 'Bulldog', 'Guardian', 'Phantom',
                   'Vandal', 'Marshal', 'Operator', 'Ares', 'Odin']

        secondary = ['Classic', 'Shorty', 'Frenzy', 'Ghost', 'Sheriff']

        weapons = primary + secondary

        if weap_type == 'primary' or weap_type == 'p':
            await ctx.send(f'Weapon Generated: {random.choice(primary)}')
            return

        elif weap_type == 'secondary' or weap_type == 's':
            await ctx.send(f'Weapon Generated: {random.choice(secondary)}')
            return

        else:
            await ctx.send(f'Weapon Generated: {random.choice(weapons)}')
            return

    elif game == 'apex':
        weapons = ['HAVOC Rifle', 'VK-47 Flatline', 'G7 Scout', 'Hemlok Burst AR', 'R-301 Carbine',
                   '30-30 Repeater', 'Alternator SMG', 'Prowler Burst PDW', 'R-99 SMG',
                   'Volt SMG', 'Devotion LMG', 'M600 Spitfire', 'L-STAR EMG', 'Charge Rifle',
                   'Longbow DMR', 'Kraber .50-Cal Sniper', 'Sentinel', 'Triple Take', 'EVA-8 Auto',
                   'Mastiff Shotgun', 'Mozambique Shotgun', 'Peacekeeper', 'RE-45 Auto', 'P2020',
                   'Wingman']
        await ctx.send(f'Weapon Generated: {random.choice(weapons)}')
        return

    else:
        await ctx.send('Game does not exist/ is not supported!')

bot.run(TOKEN)
