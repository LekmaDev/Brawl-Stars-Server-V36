from ByteStream.Reader import Reader
from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
#from Protocol.Messages.Server.Team import Team
from Friend import Friend

class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()
        #Team(self.client, self.player).send()
        Friend(self.client, self.player).send()