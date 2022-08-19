from ByteStream.Reader import Reader
from Protocol.Messages.Server.LeaderboardMessage import LeaderboardMessage
from Protocol.Messages.Server.LeaderboardClubMessage import LeaderboardClubMessage

class GetLeaderBordMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readBool()
        self.readVInt()
        self.type = self.readVInt()


    def process(self, db):
        LeaderboardMessage(self.client, self.player).send()
        LeaderboardClubMessage(self.client, self.player).send()
