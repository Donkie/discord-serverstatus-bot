
from discord.ext import tasks
import discord
import a2s
from mcstatus import MinecraftServer

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.serverType = kwargs.get('type')
        self.ipport = kwargs.get('ipport')

        self.previousStatus = ''

        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def set_status(self, newStatus):
        """Set the bot's status to something, and indicate that the server is online."""
        if newStatus == self.previousStatus:
            return
        
        await self.change_presence(activity=discord.Activity(name=newStatus, type=discord.ActivityType.playing), status=discord.Status.online)
        self.previousStatus = newStatus

    async def set_offline(self):
        """Set the bot's status to indicate that the server is offline."""
        await self.change_presence(activity=discord.Activity(name='(offline)', type=discord.ActivityType.playing), status=discord.Status.dnd)
        self.previousStatus = ''
    
    async def get_a2s_info(self, tries=5):
        """Helper function to retry fetching server data from a Source server multiple times."""
        i = 0
        while True:
            i = i + 1
            try:
                return await a2s.ainfo(self.ipport)
            except BaseException as e:
                if i > tries:
                    raise e

    @tasks.loop(seconds=2) # < set update rate here
    async def my_background_task(self):
        """Main task to update the status"""
        if self.serverType == 'source':
            try:
                serverInfo = await self.get_a2s_info()
            except BaseException as e:
                print(f"Failed to get Source server info:")
                print(e)
                await self.set_offline()
                return
            await self.set_status(f'{serverInfo.player_count}/{serverInfo.max_players} on {serverInfo.map_name}')
        else:
            server = MinecraftServer(self.ipport[0], self.ipport[1])
            try:
                serverInfo = await server.async_status(tries = 1)
            except BaseException as e:
                print(f"Failed to get Minecraft server info:")
                print(e)
                await self.set_offline()
                return
            await self.set_status(f'{serverInfo.players.online}/{serverInfo.players.max}')

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in
