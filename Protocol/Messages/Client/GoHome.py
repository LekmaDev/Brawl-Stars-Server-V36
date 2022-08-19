from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class GoHome(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()

    def decode(self):
        pass

    def process(self, db):
        OwnHomeDataMessage(self.client, self.player).send()
# by artem bs mods (сменил - маму с балкона кинул)


