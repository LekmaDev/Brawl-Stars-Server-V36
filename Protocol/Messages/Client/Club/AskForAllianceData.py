from ByteStream.Reader import Reader
from Protocol.Messages.Server.Club.AllianceData import AllianceData

class AskForAllianceData(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.idk = self.readLong()

    def process(self):
       print(self.idk)
       self.player.neededClub = self.idk
       # self.player.inTeam = False
       AllianceData(self.client, self.player).send()