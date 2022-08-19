from ByteStream.Writer import Writer

class LeaderboardClubMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeVInt(4)#Type
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("RU")

        self.writeVInt(2)

        self.writeLogicLong(1)
        self.writeVInt(1)
        self.writeVInt(0)

        self.writeVInt(1)
        self.writeString("t.me/artemBSmods")#Club Name
        self.writeString(f"{self.player.name}")#Name

        self.writeVInt(9)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(0)
        
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeString("RU")


