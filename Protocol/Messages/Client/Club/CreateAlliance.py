#14301

from ByteStream.Reader import Reader
from Protocol.Messages.Server.Club.MyAlliance import MyAlliance
from Protocol.Messages.Server.Club.AllianceResponce import AllianceResponce
from Protocol.Messages.Server.Club.AllianceData import AllianceData
import random

class CreateAlliance(Reader):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player = player
	def decode(self):
		self.info = {}
		self.info["name"] = self.readString()
		self.info["desc"] = self.readString()
		self.info["icon"] = self.readDataReference()
		self.info["region"] = self.readDataReference()
		self.info["type"] = self.readVInt()
		self.info["trop"] = self.readVInt()
		self.info["ff"] = self.readBool()
		
	def process(self):
		a = self.info
		db = DB()
		user = db.loadPlayer(self.player.ID)
		
		
		
		
		
		
		
		if self.player.isInClub == False:
			self.player.isInClub = True
			self.player.aID = random.randint(1, 9999999)
			self.player.aname = a["name"]
			self.player.adesc = a["desc"]
			self.player.aicon = a["icon"]
			self.player.atype = a["type"]
			self.player.atrop = a["trop"]
			self.player.aff = a["ff"]
			user["isInClub"] = self.player.isInClub
			user["aID"] = self.player.aID
			user["aname"] = self.player.aname
			user["adesc"] = self.player.adesc
			user["aicon"] = self.player.aicon
			user["atype"] = self.player.atype
			user["atrop"] = self.player.atrop
			user["aff"] = self.player.aff
			db.replaceValue(user, self.player.Token)
			AllianceResponce(self.client, self.player, 20).send()
			MyAlliance(self.client, self.player).send()
			
		else:
			AllianceResponce(self.client, self.player, 47).send()
		#AllianceData(self.client, self.player).send()