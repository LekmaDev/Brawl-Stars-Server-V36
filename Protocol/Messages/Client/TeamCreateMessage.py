from ByteStream.Reader import Reader
from Protocol.Messages.Server.Team import Team

class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        Team(self.client, self.player).send()