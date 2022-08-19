from ByteStream.Writer import Writer


class TeamLeft(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 24125

    def encode(self):
        self.writeInt(0)