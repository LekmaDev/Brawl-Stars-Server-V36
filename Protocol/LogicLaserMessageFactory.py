from Protocol.Messages.Client.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.LoginMessage import LoginMessage
from Protocol.Messages.Client.EndClientTurnMessage import EndClientTurnMessage
from Protocol.Messages.Client.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Client.AskForBattleEndMessage import AskForBattleEndMessage
from Protocol.Messages.Client.GetLeaderBordMessage import GetLeaderBordMessage
from Protocol.Messages.Client.GoHome import GoHome
from Protocol.Messages.Server.Team import Team
from Protocol.Messages.Server.TeamLeft import TeamLeft
from Protocol.Messages.Client.LeaveTeam import LeaveTeam
from Protocol.Messages.Client.SetLocationTeam import SetLocationTeam
from Protocol.Messages.Client.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.LoginMessage import LoginMessage
from Protocol.Messages.Client.GetPlayerProfileMessage import GetPlayerProfileMessage
from Protocol.Messages.Client.Club.AskForAllianceData import AskForAllianceData
from Protocol.Messages.Client.Club.CreateAlliance import CreateAlliance
from Protocol.Messages.Server.PlayerProfileMessage import PlayerProfileMessage

packets = {

    10100: ClientHelloMessage,
    10101: LoginMessage,
    14102: EndClientTurnMessage,
    14110: AskForBattleEndMessage,
    14350: TeamCreateMessage,
    14113: GetPlayerProfileMessage,
    24113: PlayerProfileMessage,
    14403: GetLeaderBordMessage,
    14109: GoHome,
    14301: CreateAlliance,
    14302: AskForAllianceData,
     24124: Team,
     14363: SetLocationTeam,
     14353: LeaveTeam,
     24125: TeamLeft,
}
