from ByteStream.Writer import Writer

class Friend(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20199
        self.player = player

    def encode(self):
    	self.writeInt(0)

    