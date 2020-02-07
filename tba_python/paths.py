# API Version 3.8.0 

from converter import *

def getStatus(tba, ):
    """Returns API status, and TBA status information."""
    return convertToAPIStatus(tba.get(f"/status"))

def getTeams(tba, page_num: int):
    """Gets a list of `Team` objects, paginated in groups of 500."""
    return [convertToTeam(item) for item in tba.get(f"/teams/{page_num}")]

def getTeamsSimple(tba, page_num: int):
    """Gets a list of short form `Team_Simple` objects, paginated in groups of 500."""
    return [convertToTeamSimple(item) for item in tba.get(f"/teams/{page_num}/simple")]

def getTeamsKeys(tba, page_num: int):
    """Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.)"""
    return tba.get(f"/teams/{page_num}/keys")

def getTeamsByYear(tba, year: int, page_num: int):
    """Gets a list of `Team` objects that competed in the given year, paginated in groups of 500."""
    return [convertToTeam(item) for item in tba.get(f"/teams/{year}/{page_num}")]

def getTeamsByYearSimple(tba, year: int, page_num: int):
    """Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups of 500."""
    return [convertToTeamSimple(item) for item in tba.get(f"/teams/{year}/{page_num}/simple")]

def getTeamsByYearKeys(tba, year: int, page_num: int):
    """Gets a list Team Keys that competed in the given year, paginated in groups of 500."""
    return tba.get(f"/teams/{year}/{page_num}/keys")

def getTeam(tba, team_key: str):
    """Gets a `Team` object for the team referenced by the given key."""
    return convertToTeam(tba.get(f"/team/{team_key}"))

def getTeamSimple(tba, team_key: str):
    """Gets a `Team_Simple` object for the team referenced by the given key."""
    return convertToTeamSimple(tba.get(f"/team/{team_key}/simple"))

def getTeamYearsParticipated(tba, team_key: str):
    """Gets a list of years in which the team participated in at least one competition."""
    return tba.get(f"/team/{team_key}/years_participated")

def getTeamDistricts(tba, team_key: str):
    """Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district."""
    return [convertToDistrictList(item) for item in tba.get(f"/team/{team_key}/districts")]

def getTeamRobots(tba, team_key: str):
    """Gets a list of year and robot name pairs for each year that a robot name was provided. Will return an empty array if the team has never named a robot."""
    return [convertToTeamRobot(item) for item in tba.get(f"/team/{team_key}/robots")]

def getTeamEvents(tba, team_key: str):
    """Gets a list of all events this team has competed at."""
    return [convertToEvent(item) for item in tba.get(f"/team/{team_key}/events")]

def getTeamEventsSimple(tba, team_key: str):
    """Gets a short-form list of all events this team has competed at."""
    return [convertToEventSimple(item) for item in tba.get(f"/team/{team_key}/events/simple")]

def getTeamEventsKeys(tba, team_key: str):
    """Gets a list of the event keys for all events this team has competed at."""
    return tba.get(f"/team/{team_key}/events/keys")

def getTeamEventsByYear(tba, team_key: str, year: int):
    """Gets a list of events this team has competed at in the given year."""
    return [convertToEvent(item) for item in tba.get(f"/team/{team_key}/events/{year}")]

def getTeamEventsByYearSimple(tba, team_key: str, year: int):
    """Gets a short-form list of events this team has competed at in the given year."""
    return [convertToEventSimple(item) for item in tba.get(f"/team/{team_key}/events/{year}/simple")]

def getTeamEventsByYearKeys(tba, team_key: str, year: int):
    """Gets a list of the event keys for events this team has competed at in the given year."""
    return tba.get(f"/team/{team_key}/events/{year}/keys")

def getTeamEventsStatusesByYear(tba, team_key: str, year: int):
    """Gets a key-value list of the event statuses for events this team has competed at in the given year."""
    return [convertToTeamEventStatus(v) for v in tba.get(f"/team/{team_key}/events/{year}/statuses").values()]

def getTeamEventMatches(tba, team_key: str, event_key: str):
    """Gets a list of matches for the given team and event."""
    return [convertToMatch(item) for item in tba.get(f"/team/{team_key}/event/{event_key}/matches")]

def getTeamEventMatchesSimple(tba, team_key: str, event_key: str):
    """Gets a short-form list of matches for the given team and event."""
    return [convertToMatch(item) for item in tba.get(f"/team/{team_key}/event/{event_key}/matches/simple")]

def getTeamEventMatchesKeys(tba, team_key: str, event_key: str):
    """Gets a list of match keys for matches for the given team and event."""
    return tba.get(f"/team/{team_key}/event/{event_key}/matches/keys")

def getTeamEventAwards(tba, team_key: str, event_key: str):
    """Gets a list of awards the given team won at the given event."""
    return [convertToAward(item) for item in tba.get(f"/team/{team_key}/event/{event_key}/awards")]

def getTeamEventStatus(tba, team_key: str, event_key: str):
    """Gets the competition rank and status of the team at the given event."""
    return convertToTeamEventStatus(tba.get(f"/team/{team_key}/event/{event_key}/status"))

def getTeamAwards(tba, team_key: str):
    """Gets a list of awards the given team has won."""
    return [convertToAward(item) for item in tba.get(f"/team/{team_key}/awards")]

def getTeamAwardsByYear(tba, team_key: str, year: int):
    """Gets a list of awards the given team has won in a given year."""
    return [convertToAward(item) for item in tba.get(f"/team/{team_key}/awards/{year}")]

def getTeamMatchesByYear(tba, team_key: str, year: int):
    """Gets a list of matches for the given team and year."""
    return [convertToMatch(item) for item in tba.get(f"/team/{team_key}/matches/{year}")]

def getTeamMatchesByYearSimple(tba, team_key: str, year: int):
    """Gets a short-form list of matches for the given team and year."""
    return [convertToMatchSimple(item) for item in tba.get(f"/team/{team_key}/matches/{year}/simple")]

def getTeamMatchesByYearKeys(tba, team_key: str, year: int):
    """Gets a list of match keys for matches for the given team and year."""
    return tba.get(f"/team/{team_key}/matches/{year}/keys")

def getTeamMediaByYear(tba, team_key: str, year: int):
    """Gets a list of Media (videos / pictures) for the given team and year."""
    return [convertToMedia(item) for item in tba.get(f"/team/{team_key}/media/{year}")]

def getTeamMediaByTag(tba, team_key: str, media_tag: str):
    """Gets a list of Media (videos / pictures) for the given team and tag."""
    return [convertToMedia(item) for item in tba.get(f"/team/{team_key}/media/tag/{media_tag}")]

def getTeamMediaByTagYear(tba, team_key: str, media_tag: str, year: int):
    """Gets a list of Media (videos / pictures) for the given team, tag and year."""
    return [convertToMedia(item) for item in tba.get(f"/team/{team_key}/media/tag/{media_tag}/{year}")]

def getTeamSocialMedia(tba, team_key: str):
    """Gets a list of Media (social media) for the given team."""
    return [convertToMedia(item) for item in tba.get(f"/team/{team_key}/social_media")]

def getEventsByYear(tba, year: int):
    """Gets a list of events in the given year."""
    return [convertToEvent(item) for item in tba.get(f"/events/{year}")]

def getEventsByYearSimple(tba, year: int):
    """Gets a short-form list of events in the given year."""
    return [convertToEventSimple(item) for item in tba.get(f"/events/{year}/simple")]

def getEventsByYearKeys(tba, year: int):
    """Gets a list of event keys in the given year."""
    return tba.get(f"/events/{year}/keys")

def getEvent(tba, event_key: str):
    """Gets an Event."""
    return convertToEvent(tba.get(f"/event/{event_key}"))

def getEventSimple(tba, event_key: str):
    """Gets a short-form Event."""
    return convertToEventSimple(tba.get(f"/event/{event_key}/simple"))

def getEventAlliances(tba, event_key: str):
    """Gets a list of Elimination Alliances for the given Event."""
    return [convertToEliminationAlliance(item) for item in tba.get(f"/event/{event_key}/alliances")]

def getEventInsights(tba, event_key: str):
    """Gets a set of Event-specific insights for the given Event."""
    return convertToEventInsights(tba.get(f"/event/{event_key}/insights"))

def getEventOPRs(tba, event_key: str):
    """Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event."""
    return convertToEventOPRs(tba.get(f"/event/{event_key}/oprs"))

def getEventPredictions(tba, event_key: str):
    """Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time."""
    return convertToEventPredictions(tba.get(f"/event/{event_key}/predictions"))

def getEventRankings(tba, event_key: str):
    """Gets a list of team rankings for the Event."""
    return convertToEventRanking(tba.get(f"/event/{event_key}/rankings"))

def getEventDistrictPoints(tba, event_key: str):
    """Gets a list of team rankings for the Event."""
    return convertToEventDistrictPoints(tba.get(f"/event/{event_key}/district_points"))

def getEventTeams(tba, event_key: str):
    """Gets a list of `Team` objects that competed in the given event."""
    return [convertToTeam(item) for item in tba.get(f"/event/{event_key}/teams")]

def getEventTeamsSimple(tba, event_key: str):
    """Gets a short-form list of `Team` objects that competed in the given event."""
    return [convertToTeamSimple(item) for item in tba.get(f"/event/{event_key}/teams/simple")]

def getEventTeamsKeys(tba, event_key: str):
    """Gets a list of `Team` keys that competed in the given event."""
    return tba.get(f"/event/{event_key}/teams/keys")

def getEventTeamsStatuses(tba, event_key: str):
    """Gets a key-value list of the event statuses for teams competing at the given event."""
    return [convertToTeamEventStatus(v) for v in tba.get(f"/event/{event_key}/teams/statuses").values()]

def getEventMatches(tba, event_key: str):
    """Gets a list of matches for the given event."""
    return [convertToMatch(item) for item in tba.get(f"/event/{event_key}/matches")]

def getEventMatchesSimple(tba, event_key: str):
    """Gets a short-form list of matches for the given event."""
    return [convertToMatchSimple(item) for item in tba.get(f"/event/{event_key}/matches/simple")]

def getEventMatchesKeys(tba, event_key: str):
    """Gets a list of match keys for the given event."""
    return tba.get(f"/event/{event_key}/matches/keys")

def getEventMatchTimeseries(tba, event_key: str):
    """Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data.
*WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
*WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways."""
    return tba.get(f"/event/{event_key}/matches/timeseries")

def getEventAwards(tba, event_key: str):
    """Gets a list of awards from the given event."""
    return [convertToAward(item) for item in tba.get(f"/event/{event_key}/awards")]

def getMatch(tba, match_key: str):
    """Gets a `Match` object for the given match key."""
    return convertToMatch(tba.get(f"/match/{match_key}"))

def getMatchSimple(tba, match_key: str):
    """Gets a short-form `Match` object for the given match key."""
    return convertToMatchSimple(tba.get(f"/match/{match_key}/simple"))

def getMatchTimeseries(tba, match_key: str):
    """Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if not available.
*WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
*WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways."""
    return tba.get(f"/match/{match_key}/timeseries")

def getMatchZebra(tba, match_key: str):
    """Gets Zebra MotionWorks data for a Match for the given match key."""
    return convertToZebra(tba.get(f"/match/{match_key}/zebra_motionworks"))

def getDistrictsByYear(tba, year: int):
    """Gets a list of districts and their corresponding district key, for the given year."""
    return [convertToDistrictList(item) for item in tba.get(f"/districts/{year}")]

def getDistrictEvents(tba, district_key: str):
    """Gets a list of events in the given district."""
    return [convertToEvent(item) for item in tba.get(f"/district/{district_key}/events")]

def getDistrictEventsSimple(tba, district_key: str):
    """Gets a short-form list of events in the given district."""
    return [convertToEventSimple(item) for item in tba.get(f"/district/{district_key}/events/simple")]

def getDistrictEventsKeys(tba, district_key: str):
    """Gets a list of event keys for events in the given district."""
    return tba.get(f"/district/{district_key}/events/keys")

def getDistrictTeams(tba, district_key: str):
    """Gets a list of `Team` objects that competed in events in the given district."""
    return [convertToTeam(item) for item in tba.get(f"/district/{district_key}/teams")]

def getDistrictTeamsSimple(tba, district_key: str):
    """Gets a short-form list of `Team` objects that competed in events in the given district."""
    return [convertToTeamSimple(item) for item in tba.get(f"/district/{district_key}/teams/simple")]

def getDistrictTeamsKeys(tba, district_key: str):
    """Gets a list of `Team` objects that competed in events in the given district."""
    return tba.get(f"/district/{district_key}/teams/keys")

def getDistrictRankings(tba, district_key: str):
    """Gets a list of team district rankings for the given district."""
    return [convertToDistrictRanking(item) for item in tba.get(f"/district/{district_key}/rankings")]
