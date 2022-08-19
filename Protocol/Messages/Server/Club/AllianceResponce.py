from ByteStream.Writer import Writer


class AllianceResponce(Writer):
    def __init__(self, client, player, action):
        super().__init__(client)
        self.player = player
        self.action = action
        self.id = 24333

    def encode(self):
        self.writeVInt(self.action)