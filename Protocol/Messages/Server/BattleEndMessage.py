from ByteStream.Writer import Writer


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player

    def encode(self):
        self.writeVint(2) # Battle End Game Mode (2 = Showdown, 3 = Robo Rumble, 4 = Big Game, 5 = Duo Showdown, 6 = Boss Fight/Super City Rampage. Else is 3vs3)
        self.writeVint(0) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(0) # Tokens Gained
        self.writeVint(8) # Trophies Result
        self.writeVint(0) # Power Play Points Gained
        self.writeVint(0) # Doubled Tokens
        self.writeVint(0) # Double Token Event
        self.writeVint(0) # Token Doubler Remaining
        self.writeVint(0) # Robo Rumble/Boss Fight/Super City Rampage Level Passed
        self.writeVint(0) # Epic Win Power Play Points Gained
        self.writeVint(0) # Championship Level Passed
        self.writeVint(0) # Challenge Reward Type (0 = Star Points, 1 = Star Tokens)
        self.writeVint(0) # Challenge Reward Ammount
        self.writeVint(0) # Championship Losses Left
        self.writeVint(0) # Championship Maximun Losses
        self.writeVint(0) # Coin Shower Event
        self.writeVint(0) # Underdog Trophies
        self.writeVint(48) # Battle Result Type ((-16)-(-1) = Power Play Battle End, 0-15 = Practice and Championship Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End, 64-79 = Championship Battle End)
        self.writeVint(0) # Championship Challenge Type
        self.writeVint(0) # Championship Cleared
        
        # Players Array
        self.writeVint(1) # Battle End Screen Players
        self.writeVint(1) # Player Team and Star Player Type
        self.writeScId(16, self.player.home_brawler) # Player Brawler
        self.writeScId(29, 0) # Player Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Player Power Play Points
        self.writeVint(9) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString(self.player.name) # Player Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000 + self.player.name_color) # Player Name Color
        self.writeVint(0) # Null Vint

        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(0) # Normal Experience Gained
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(0) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Trophies Bar Milestone ID
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Bar Milestone ID
        self.writeVint(0) # Player Experience
        self.writeVint(0) # Player Experience for Level
        
        self.writeScId(28, 0)  # Player Profile Icon
        self.writeBoolean(True)  # Play Again