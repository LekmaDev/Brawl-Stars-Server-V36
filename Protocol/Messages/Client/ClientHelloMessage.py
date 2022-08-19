from ByteStream.Reader import Reader
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

class ClientHelloMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()

    def decode(self):
        pass

    def process(self, db):
        LoginFailedMessage(self.client, self.player, "А нехуй аналлсики апк юзать\nКачай норм апк и тогда зайдёт").send()



