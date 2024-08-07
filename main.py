
from discord import Intents
from discord.ext.commands import Bot
from os import getcwd, listdir, environ
from os.path import exists

from json import load


class Slime(Bot):


    def __init__(self) -> None:
        super().__init__()

        self.intents = Intents().all()
        self.config = {

        }
        self.database = 'mongodb client here'
        self.__modules_loaded = []

    def load_all_extensions(self):

        path = getcwd()+'/cogs'

        files = [f for f in listdir(path) if '.py' in f]
        for cog in files:
            self.load_extension(f"cogs.{cog.replace('.py','',9)}")
            self.__modules_loaded.append(cog.replace('.py','',9))
         
    def load_config(self):
        if exists('config.json'):
            with open("config.json", 'r') as f:
                self.config = load(f)
   

    def b_run(self):              

        
        self.run(self.config['BOT_TOKEN'])