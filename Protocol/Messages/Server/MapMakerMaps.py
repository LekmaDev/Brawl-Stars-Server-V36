from ByteStream.Writer import Writer


class MapMakerMaps(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 22102

    def encode(self):
        self.writeVint(1)# Count
        for i in [3]:
        	self.writeLogicLong(int(i)) # Map ID
        	self.writeString(f"github.com/viadev228") # Map Name
        	self.writeVint(i) # Game Mode Variation
        	self.writeDataReference(47, 59) # Location Theme Data
        	self.writeString("M") # Compressed Map Data
        	self.writeLogicLong(self.player.ID) # Account ID
        	self.writeString("pon") # Avatar Name
        	self.writeVint(0) # State
        	self.writeLong(1) # Last Update Time Seconds Since Epoch
        	self.writeVint(1) # Friendly Participant Count
        	self.writeVint(0) # Friendly Signoff Count
        	self.writeVint(9339) # Likes
        	self.writeVint(1337) # Dislikes
        	self.writeVint(228) # Battles