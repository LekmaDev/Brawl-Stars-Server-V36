import json
from datetime import datetime

class LogicClientHome:

    def encode(self):
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        self.writeVInt(time_stamp)

        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.high_trophies)
        self.writeVInt(self.player.high_trophies)

        self.writeVInt(self.player.trophy_reward)
        self.writeVInt(self.player.exp_points)

        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        self.writeVInt(50)
        for x in range(50):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(1)

        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False)
        
        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)
        
        self.writeVInt(1) # Offers Count
        
        self.writeVInt(1) # Item Count
        
        self.writeVInt(16) # ItemType
        self.writeVInt(9339) # Amount
        self.writeDataReference(0,0) # CsvID
        self.writeVInt(0) # SkinID
        
        self.writeVInt(0) # Currency
        self.writeVInt(0) # Cost
        self.writeVInt(252000) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Claimed
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # DailyOffer
        self.writeVInt(0) # OldPrice
        self.writeInt(0)
        self.writeString("bruh") # Offer Text
        self.writeVInt(0)
        self.writeString("offer_velocirapids") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # Processing
        self.writeVInt(0) # TypeBenefit
        self.writeVInt(0) # Benefit

        self.writeVInt(0) # Array
        for x in range(0):
        	self.writeVInt(x)

        self.writeVInt(200)#Tokens
        self.writeVInt(-1)#Timer

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)#Tickets

        self.writeDataReference(16, self.player.home_brawler)

        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)
        
        if self.player.trophies == 0:
        	self.writeVInt(0)
        else:
            self.writeVInt(1) # 1
            self.writeInt(4) # что получаем? 4 - кубки, 8 - старпоинты, 10 - очки силовой гонки
            self.writeInt(1250) # количество получаемого

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(2)
        for x in range(5, 7):
            self.writeVInt(x)
            self.writeVInt(34500)
            self.writeUInt8(1)
            self.writeVInt(0)
            self.writeUInt8(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeBoolean(True) #Иконки, эмодзи
        self.writeVInt(520)
        for i in range(520):
        	self.writeDataReference(52, i)
        	self.writeVInt(1)
        	self.writeVInt(1)
        	self.writeVInt(1)

        self.writeBoolean(False)
        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(20)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24]:
            self.writeVInt(x)

        events = json.loads(open("events.json", "r").read())

        self.writeVInt(len(events))

        for event in events:
            self.writeVInt(events.index(event) + 1)
            if x == 0:
                self.writeVInt(20)
            else:
                self.writeVInt(events.index(event) + 1)
            self.writeVInt(event['Ended'])
            self.writeVInt(event['Timer'])
            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])
        self.writeArrayVint([20, 50, 140, 280])
        self.writeArrayVint([150, 400, 1200, 2600])

        self.writeUInt8(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(1)
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000000 + self.player.theme_id)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeLong(self.player.ID)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)

        self.writeUInt8(0)

        self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)