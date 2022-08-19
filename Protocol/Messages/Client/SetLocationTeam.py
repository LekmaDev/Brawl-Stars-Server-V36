from ByteStream.Reader import Reader
from Protocol.Messages.Server.Team import Team

class SetLocationTeam(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.none = self.readVInt()

    def process(self, db):
        self.player.map_id = self.none
        Team(self.client, self.player).send()