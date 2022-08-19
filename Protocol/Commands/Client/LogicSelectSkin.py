from ByteStream.Reader import Reader
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters

class LogicSelectSkin(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.skinID = self.readDataReference()[1]


    def process(self, db):
        self.player.home_brawler = Characters.get_brawler_by_skin_id(self, self.skinID)