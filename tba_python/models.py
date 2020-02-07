# The Blue Alliance API Version 3.8.0 

from typing import TypeVar, List, NamedTuple, Generic

V = TypeVar("V")

class Alliances(NamedTuple, Generic[V]):
    blue: V
    red: V

class APIStatus(NamedTuple):
    data: dict
    current_season: int  # Year of the current FRC season.
    max_season: int  # Maximum FRC season year for valid queries.
    is_datafeed_down: bool  # True if the entire FMS API provided by FIRST is down.
    down_events: List[str]  # An array of strings containing event keys of any active events that are no longer updating.
    ios: "APIStatusAppVersion"
    android: "APIStatusAppVersion"

class APIStatusAppVersion(NamedTuple):
    data: dict
    min_app_version: int  # Internal use - Minimum application version required to correctly connect and process data.
    latest_app_version: int  # Internal use - Latest application version available.

class TeamSimple(NamedTuple):
    data: dict
    key: str  # TBA team key with the format `frcXXXX` with `XXXX` representing the team number.
    team_number: int  # Official team number issued by FIRST.
    nickname: str  # Team nickname provided by FIRST.
    name: str  # Official long name registered with FIRST.
    city: str  # City of team derived from parsing the address registered with FIRST.
    state_prov: str  # State of team derived from parsing the address registered with FIRST.
    country: str  # Country of team derived from parsing the address registered with FIRST.

class Team(NamedTuple):
    data: dict
    key: str  # TBA team key with the format `frcXXXX` with `XXXX` representing the team number.
    team_number: int  # Official team number issued by FIRST.
    nickname: str  # Team nickname provided by FIRST.
    name: str  # Official long name registered with FIRST.
    school_name: str  # Name of team school or affilited group registered with FIRST.
    city: str  # City of team derived from parsing the address registered with FIRST.
    state_prov: str  # State of team derived from parsing the address registered with FIRST.
    country: str  # Country of team derived from parsing the address registered with FIRST.
    address: str  # Will be NULL, for future development.
    postal_code: str  # Postal code from the team address.
    gmaps_place_id: str  # Will be NULL, for future development.
    gmaps_url: str  # Will be NULL, for future development.
    lat: float  # Will be NULL, for future development.
    lng: float  # Will be NULL, for future development.
    location_name: str  # Will be NULL, for future development.
    website: str  # Official website associated with the team.
    rookie_year: int  # First year the team officially competed.
    motto: str  # Team's motto as provided by FIRST. This field is deprecated and will return null - will be removed at end-of-season in 2019.
    home_championship: dict  # Location of the team's home championship each year as a key-value pair. The year (as a string) is the key, and the city is the value.

class TeamRobot(NamedTuple):
    data: dict
    year: int  # Year this robot competed in.
    robot_name: str  # Name of the robot as provided by the team.
    key: str  # Internal TBA identifier for this robot.
    team_key: str  # TBA team key for this robot.

class EventSimple(NamedTuple):
    data: dict
    key: str  # TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.
    name: str  # Official name of event on record either provided by FIRST or organizers of offseason event.
    event_code: str  # Event short code, as provided by FIRST.
    event_type: int  # Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2
    district: "DistrictList"
    city: str  # City, town, village, etc. the event is located in.
    state_prov: str  # State or Province the event is located in.
    country: str  # Country the event is located in.
    start_date: str  # Event start date in `yyyy-mm-dd` format.
    end_date: str  # Event end date in `yyyy-mm-dd` format.
    year: int  # Year the event data is for.

class Event(NamedTuple):
    data: dict
    key: str  # TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.
    name: str  # Official name of event on record either provided by FIRST or organizers of offseason event.
    event_code: str  # Event short code, as provided by FIRST.
    event_type: int  # Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2
    district: "DistrictList"
    city: str  # City, town, village, etc. the event is located in.
    state_prov: str  # State or Province the event is located in.
    country: str  # Country the event is located in.
    start_date: str  # Event start date in `yyyy-mm-dd` format.
    end_date: str  # Event end date in `yyyy-mm-dd` format.
    year: int  # Year the event data is for.
    short_name: str  # Same as `name` but doesn't include event specifiers, such as 'Regional' or 'District'. May be null.
    event_type_string: str  # Event Type, eg Regional, District, or Offseason.
    week: int  # Week of the event relative to the first official season event, zero-indexed. Only valid for Regionals, Districts, and District Championships. Null otherwise. (Eg. A season with a week 0 'preseason' event does not count, and week 1 events will show 0 here. Seasons with a week 0.5 regional event will show week 0 for those event(s) and week 1 for week 1 events and so on.)
    address: str  # Address of the event's venue, if available.
    postal_code: str  # Postal code from the event address.
    gmaps_place_id: str  # Google Maps Place ID for the event address.
    gmaps_url: str  # Link to address location on Google Maps.
    lat: float  # Latitude for the event address.
    lng: float  # Longitude for the event address.
    location_name: str  # Name of the location at the address for the event, eg. Blue Alliance High School.
    timezone: str  # Timezone name.
    website: str  # The event's website, if any.
    first_event_id: str  # The FIRST internal Event ID, used to link to the event on the FRC webpage.
    first_event_code: str  # Public facing event code used by FIRST (on frc-events.firstinspires.org, for example)
    webcasts: "List[Webcast]"
    division_keys: List[str]  # An array of event keys for the divisions at this event.
    parent_event_key: str  # The TBA Event key that represents the event's parent. Used to link back to the event from a division event. It is also the inverse relation of `divison_keys`.
    playoff_type: int  # Playoff Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/playoff_type.py#L4, or null.
    playoff_type_string: str  # String representation of the `playoff_type`, or null.

class TeamEventStatus(NamedTuple):
    data: dict
    qual: "TeamEventStatusRank"
    alliance: "TeamEventStatusAlliance"
    playoff: "TeamEventStatusPlayoff"
    alliance_status_str: str  # An HTML formatted string suitable for display to the user containing the team's alliance pick status.
    playoff_status_str: str  # An HTML formatter string suitable for display to the user containing the team's playoff status.
    overall_status_str: str  # An HTML formatted string suitable for display to the user containing the team's overall status summary of the event.
    next_match_key: str  # TBA match key for the next match the team is scheduled to play in at this event, or null.
    last_match_key: str  # TBA match key for the last match the team played in at this event, or null.

class TeamEventStatusRank(NamedTuple):
    data: dict
    num_teams: int  # Number of teams ranked.
    ranking: dict
    sort_order_info: List[dict]  # Ordered list of names corresponding to the elements of the `sort_orders` array.
    status: str

class TeamEventStatusAlliance(NamedTuple):
    data: dict
    name: str  # Alliance name, may be null.
    number: int  # Alliance number.
    backup: "TeamEventStatusAllianceBackup"
    pick: int  # Order the team was picked in the alliance from 0-2, with 0 being alliance captain.

class TeamEventStatusAllianceBackup(NamedTuple):
    """Backup status, may be null."""
    data: dict
    out: str  # TBA key for the team replaced by the backup.
    _in: str  # TBA key for the backup team called in.

class TeamEventStatusPlayoff(NamedTuple):
    """Playoff status for this team, may be null if the team did not make playoffs, or playoffs have not begun."""
    data: dict
    level: str  # The highest playoff level the team reached.
    current_level_record: "WLTRecord"
    record: "WLTRecord"
    status: str  # Current competition status for the playoffs.
    playoff_average: int  # The average match score during playoffs. Year specific. May be null if not relevant for a given year.

class EventRanking(NamedTuple):
    data: dict
    rankings: List[dict]  # List of rankings at the event.
    extra_stats_info: List[dict]  # List of special TBA-generated values provided in the `extra_stats` array for each item.
    sort_order_info: List[dict]  # List of year-specific values provided in the `sort_orders` array for each team.

class EventDistrictPoints(NamedTuple):
    data: dict
    points: dict  # Points gained for each team at the event. Stored as a key-value pair with the team key as the key, and an object describing the points as its value.
    tiebreakers: dict  # Tiebreaker values for each team at the event. Stored as a key-value pair with the team key as the key, and an object describing the tiebreaker elements as its value.

class EventInsights(NamedTuple):
    """A year-specific event insight object expressed as a JSON string, separated in to `qual` and `playoff` fields. See also Event_Insights_2016, Event_Insights_2017, etc."""
    data: dict
    qual: dict  # Inights for the qualification round of an event
    playoff: dict  # Insights for the playoff round of an event

class EventInsights2016(NamedTuple):
    """Insights for FIRST Stronghold qualification and elimination matches."""
    data: dict
    LowBar: List[float]  # For the Low Bar - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    A_ChevalDeFrise: List[float]  # For the Cheval De Frise - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    A_Portcullis: List[float]  # For the Portcullis - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    B_Ramparts: List[float]  # For the Ramparts - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    B_Moat: List[float]  # For the Moat - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    C_SallyPort: List[float]  # For the Sally Port - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    C_Drawbridge: List[float]  # For the Drawbridge - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    D_RoughTerrain: List[float]  # For the Rough Terrain - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    D_RockWall: List[float]  # For the Rock Wall - An array with three values, number of times damaged, number of opportunities to damage, and percentage.
    average_high_goals: float  # Average number of high goals scored.
    average_low_goals: float  # Average number of low goals scored.
    breaches: List[float]  # An array with three values, number of times breached, number of opportunities to breach, and percentage.
    scales: List[float]  # An array with three values, number of times scaled, number of opportunities to scale, and percentage.
    challenges: List[float]  # An array with three values, number of times challenged, number of opportunities to challenge, and percentage.
    captures: List[float]  # An array with three values, number of times captured, number of opportunities to capture, and percentage.
    average_win_score: float  # Average winning score.
    average_win_margin: float  # Average margin of victory.
    average_score: float  # Average total score.
    average_auto_score: float  # Average autonomous score.
    average_crossing_score: float  # Average crossing score.
    average_boulder_score: float  # Average boulder score.
    average_tower_score: float  # Average tower score.
    average_foul_score: float  # Average foul score.
    high_score: List[str]  # An array with three values, high score, match key from the match with the high score, and the name of the match.

class EventInsights2017(NamedTuple):
    """Insights for FIRST STEAMWORKS qualification and elimination matches."""
    data: dict
    average_foul_score: float  # Average foul score.
    average_fuel_points: float  # Average fuel points scored.
    average_fuel_points_auto: float  # Average fuel points scored during auto.
    average_fuel_points_teleop: float  # Average fuel points scored during teleop.
    average_high_goals: float  # Average points scored in the high goal.
    average_high_goals_auto: float  # Average points scored in the high goal during auto.
    average_high_goals_teleop: float  # Average points scored in the high goal during teleop.
    average_low_goals: float  # Average points scored in the low goal.
    average_low_goals_auto: float  # Average points scored in the low goal during auto.
    average_low_goals_teleop: float  # Average points scored in the low goal during teleop.
    average_mobility_points_auto: float  # Average mobility points scored during auto.
    average_points_auto: float  # Average points scored during auto.
    average_points_teleop: float  # Average points scored during teleop.
    average_rotor_points: float  # Average rotor points scored.
    average_rotor_points_auto: float  # Average rotor points scored during auto.
    average_rotor_points_teleop: float  # Average rotor points scored during teleop.
    average_score: float  # Average score.
    average_takeoff_points_teleop: float  # Average takeoff points scored during teleop.
    average_win_margin: float  # Average margin of victory.
    average_win_score: float  # Average winning score.
    high_kpa: List[str]  # An array with three values, kPa scored, match key from the match with the high kPa, and the name of the match
    high_score: List[str]  # An array with three values, high score, match key from the match with the high score, and the name of the match
    kpa_achieved: List[float]  # An array with three values, number of times kPa bonus achieved, number of opportunities to bonus, and percentage.
    mobility_counts: List[float]  # An array with three values, number of times mobility bonus achieved, number of opportunities to bonus, and percentage.
    rotor_1_engaged: List[float]  # An array with three values, number of times rotor 1 engaged, number of opportunities to engage, and percentage.
    rotor_1_engaged_auto: List[float]  # An array with three values, number of times rotor 1 engaged in auto, number of opportunities to engage in auto, and percentage.
    rotor_2_engaged: List[float]  # An array with three values, number of times rotor 2 engaged, number of opportunities to engage, and percentage.
    rotor_2_engaged_auto: List[float]  # An array with three values, number of times rotor 2 engaged in auto, number of opportunities to engage in auto, and percentage.
    rotor_3_engaged: List[float]  # An array with three values, number of times rotor 3 engaged, number of opportunities to engage, and percentage.
    rotor_4_engaged: List[float]  # An array with three values, number of times rotor 4 engaged, number of opportunities to engage, and percentage.
    takeoff_counts: List[float]  # An array with three values, number of times takeoff was counted, number of opportunities to takeoff, and percentage.
    unicorn_matches: List[float]  # An array with three values, number of times a unicorn match (Win + kPa & Rotor Bonuses) occured, number of opportunities to have a unicorn match, and percentage.

class EventInsights2018(NamedTuple):
    """Insights for FIRST Power Up qualification and elimination matches."""
    data: dict
    auto_quest_achieved: List[float]  # An array with three values, number of times auto quest was completed, number of opportunities to complete the auto quest, and percentage.
    average_boost_played: float  # Average number of boost power up scored (out of 3).
    average_endgame_points: float  # Average endgame points.
    average_force_played: float  # Average number of force power up scored (out of 3).
    average_foul_score: float  # Average foul score.
    average_points_auto: float  # Average points scored during auto.
    average_points_teleop: float  # Average points scored during teleop.
    average_run_points_auto: float  # Average mobility points scored during auto.
    average_scale_ownership_points: float  # Average scale ownership points scored.
    average_scale_ownership_points_auto: float  # Average scale ownership points scored during auto.
    average_scale_ownership_points_teleop: float  # Average scale ownership points scored during teleop.
    average_score: float  # Average score.
    average_switch_ownership_points: float  # Average switch ownership points scored.
    average_switch_ownership_points_auto: float  # Average switch ownership points scored during auto.
    average_switch_ownership_points_teleop: float  # Average switch ownership points scored during teleop.
    average_vault_points: float  # Average value points scored.
    average_win_margin: float  # Average margin of victory.
    average_win_score: float  # Average winning score.
    boost_played_counts: List[float]  # An array with three values, number of times a boost power up was played, number of opportunities to play a boost power up, and percentage.
    climb_counts: List[float]  # An array with three values, number of times a climb occurred, number of opportunities to climb, and percentage.
    face_the_boss_achieved: List[float]  # An array with three values, number of times an alliance faced the boss, number of opportunities to face the boss, and percentage.
    force_played_counts: List[float]  # An array with three values, number of times a force power up was played, number of opportunities to play a force power up, and percentage.
    high_score: List[str]  # An array with three values, high score, match key from the match with the high score, and the name of the match
    levitate_played_counts: List[float]  # An array with three values, number of times a levitate power up was played, number of opportunities to play a levitate power up, and percentage.
    run_counts_auto: List[float]  # An array with three values, number of times a team scored mobility points in auto, number of opportunities to score mobility points in auto, and percentage.
    scale_neutral_percentage: float  # Average scale neutral percentage.
    scale_neutral_percentage_auto: float  # Average scale neutral percentage during auto.
    scale_neutral_percentage_teleop: float  # Average scale neutral percentage during teleop.
    switch_owned_counts_auto: List[float]  # An array with three values, number of times a switch was owned during auto, number of opportunities to own a switch during auto, and percentage.
    unicorn_matches: List[float]  # An array with three values, number of times a unicorn match (Win + Auto Quest + Face the Boss) occurred, number of opportunities to have a unicorn match, and percentage.
    winning_opp_switch_denial_percentage_teleop: float  # Average opposing switch denail percentage for the winning alliance during teleop.
    winning_own_switch_ownership_percentage: float  # Average own switch ownership percentage for the winning alliance.
    winning_own_switch_ownership_percentage_auto: float  # Average own switch ownership percentage for the winning alliance during auto.
    winning_own_switch_ownership_percentage_teleop: float  # Average own switch ownership percentage for the winning alliance during teleop.
    winning_scale_ownership_percentage: float  # Average scale ownership percentage for the winning alliance.
    winning_scale_ownership_percentage_auto: float  # Average scale ownership percentage for the winning alliance during auto.
    winning_scale_ownership_percentage_teleop: float  # Average scale ownership percentage for the winning alliance during teleop.

class EventOPRs(NamedTuple):
    """OPR, DPR, and CCWM for teams at the event."""
    data: dict
    oprs: dict  # A key-value pair with team key (eg `frc254`) as key and OPR as value.
    dprs: dict  # A key-value pair with team key (eg `frc254`) as key and DPR as value.
    ccwms: dict  # A key-value pair with team key (eg `frc254`) as key and CCWM as value.

class EventPredictions(NamedTuple):
    """JSON Object containing prediction information for the event. Contains year-specific information and is subject to change."""
    data: dict

class MatchSimple(NamedTuple):
    data: dict
    key: str  # TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may append the competition level if more than one match in required per set.
    comp_level: str  # The competition level the match was played at.
    set_number: int  # The set number in a series of matches where more than one match is required in the match series.
    match_number: int  # The match number of the match in the competition level.
    alliances: "Alliances[MatchAlliance]"  # A list of alliances, the teams on the alliances, and their score.
    winning_alliance: str  # The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie.
    event_key: str  # Event key of the event the match was played at.
    time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule.
    predicted_time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time.
    actual_time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.

class Match(NamedTuple):
    data: dict
    key: str  # TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may be appended to the competition level if more than one match in required per set.
    comp_level: str  # The competition level the match was played at.
    set_number: int  # The set number in a series of matches where more than one match is required in the match series.
    match_number: int  # The match number of the match in the competition level.
    alliances: "Alliances[MatchAlliance]"  # A list of alliances, the teams on the alliances, and their score.
    winning_alliance: str  # The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie.
    event_key: str  # Event key of the event the match was played at.
    time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule.
    actual_time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.
    predicted_time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time.
    post_result_time: int  # UNIX timestamp (seconds since 1-Jan-1970 00:00:00) when the match result was posted.
    score_breakdown: dict  # Score breakdown for auto, teleop, etc. points. Varies from year to year. May be null.
    videos: List[dict]  # Array of video objects associated with this match.

class MatchAlliance(NamedTuple):
    data: dict
    score: int  # Score for this alliance. Will be null or -1 for an unplayed match.
    team_keys: List[str]
    surrogate_team_keys: List[str]  # TBA team keys (eg `frc254`) of any teams playing as a surrogate.
    dq_team_keys: List[str]  # TBA team keys (eg `frc254`) of any disqualified teams.

class Zebra(NamedTuple):
    data: dict
    key: str  # TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may be appended to the competition level if more than one match in required per set.
    times: List[float]  # A list of relative timestamps for each data point. Each timestamp will correspond to the X and Y value at the same index in a team xs and ys arrays. `times`, all teams `xs` and all teams `ys` are guarenteed to be the same length.
    alliances: "Alliances[ZebraTeam]"

class ZebraTeam(NamedTuple):
    data: dict
    team_key: str  # The TBA team key for the Zebra MotionWorks data.
    xs: List[float]  # A list containing doubles and nulls representing a teams X position in feet at the corresponding timestamp. A null value represents no tracking data for a given timestamp.
    ys: List[float]  # A list containing doubles and nulls representing a teams Y position in feet at the corresponding timestamp. A null value represents no tracking data for a given timestamp.

class MatchScoreBreakdown2015(NamedTuple):
    """See the 2015 FMS API documentation for a description of each value"""
    data: dict
    blue: "MatchScoreBreakdown2015Alliance"
    red: "MatchScoreBreakdown2015Alliance"
    coopertition: str
    coopertition_points: int

class MatchScoreBreakdown2015Alliance(NamedTuple):
    data: dict
    auto_points: int
    teleop_points: int
    container_points: int
    tote_points: int
    litter_points: int
    foul_points: int
    adjust_points: int
    total_points: int
    foul_count: int
    tote_count_far: int
    tote_count_near: int
    tote_set: bool
    tote_stack: bool
    container_count_level1: int
    container_count_level2: int
    container_count_level3: int
    container_count_level4: int
    container_count_level5: int
    container_count_level6: int
    container_set: bool
    litter_count_container: int
    litter_count_landfill: int
    litter_count_unprocessed: int
    robot_set: bool

class MatchScoreBreakdown2016(NamedTuple):
    """See the 2016 FMS API documentation for a description of each value."""
    data: dict
    blue: "MatchScoreBreakdown2016Alliance"
    red: "MatchScoreBreakdown2016Alliance"

class MatchScoreBreakdown2016Alliance(NamedTuple):
    data: dict
    autoPoints: int
    teleopPoints: int
    breachPoints: int
    foulPoints: int
    capturePoints: int
    adjustPoints: int
    totalPoints: int
    robot1Auto: str
    robot2Auto: str
    robot3Auto: str
    autoReachPoints: int
    autoCrossingPoints: int
    autoBouldersLow: int
    autoBouldersHigh: int
    autoBoulderPoints: int
    teleopCrossingPoints: int
    teleopBouldersLow: int
    teleopBouldersHigh: int
    teleopBoulderPoints: int
    teleopDefensesBreached: bool
    teleopChallengePoints: int
    teleopScalePoints: int
    teleopTowerCaptured: int
    towerFaceA: str
    towerFaceB: str
    towerFaceC: str
    towerEndStrength: int
    techFoulCount: int
    foulCount: int
    position2: str
    position3: str
    position4: str
    position5: str
    position1crossings: int
    position2crossings: int
    position3crossings: int
    position4crossings: int
    position5crossings: int

class MatchScoreBreakdown2017(NamedTuple):
    """See the 2017 FMS API documentation for a description of each value."""
    data: dict
    blue: "MatchScoreBreakdown2017Alliance"
    red: "MatchScoreBreakdown2017Alliance"

class MatchScoreBreakdown2017Alliance(NamedTuple):
    data: dict
    autoPoints: int
    teleopPoints: int
    foulPoints: int
    adjustPoints: int
    totalPoints: int
    robot1Auto: str
    robot2Auto: str
    robot3Auto: str
    rotor1Auto: bool
    rotor2Auto: bool
    autoFuelLow: int
    autoFuelHigh: int
    autoMobilityPoints: int
    autoRotorPoints: int
    autoFuelPoints: int
    teleopFuelPoints: int
    teleopFuelLow: int
    teleopFuelHigh: int
    teleopRotorPoints: int
    kPaRankingPointAchieved: bool
    teleopTakeoffPoints: int
    kPaBonusPoints: int
    rotorBonusPoints: int
    rotor1Engaged: bool
    rotor2Engaged: bool
    rotor3Engaged: bool
    rotor4Engaged: bool
    rotorRankingPointAchieved: bool
    techFoulCount: int
    foulCount: int
    touchpadNear: str
    touchpadMiddle: str
    touchpadFar: str

class MatchScoreBreakdown2018(NamedTuple):
    """See the 2018 FMS API documentation for a description of each value. https://frcevents2.docs.apiary.io/#/reference/match-results/score-details"""
    data: dict
    blue: "MatchScoreBreakdown2018Alliance"
    red: "MatchScoreBreakdown2018Alliance"

class MatchScoreBreakdown2018Alliance(NamedTuple):
    data: dict
    adjustPoints: int
    autoOwnershipPoints: int
    autoPoints: int
    autoQuestRankingPoint: bool
    autoRobot1: str
    autoRobot2: str
    autoRobot3: str
    autoRunPoints: int
    autoScaleOwnershipSec: int
    autoSwitchAtZero: bool
    autoSwitchOwnershipSec: int
    endgamePoints: int
    endgameRobot1: str
    endgameRobot2: str
    endgameRobot3: str
    faceTheBossRankingPoint: bool
    foulCount: int
    foulPoints: int
    rp: int
    techFoulCount: int
    teleopOwnershipPoints: int
    teleopPoints: int
    teleopScaleBoostSec: int
    teleopScaleForceSec: int
    teleopScaleOwnershipSec: int
    teleopSwitchBoostSec: int
    teleopSwitchForceSec: int
    teleopSwitchOwnershipSec: int
    totalPoints: int
    vaultBoostPlayed: int
    vaultBoostTotal: int
    vaultForcePlayed: int
    vaultForceTotal: int
    vaultLevitatePlayed: int
    vaultLevitateTotal: int
    vaultPoints: int
    tba_gameData: str  # Unofficial TBA-computed value of the FMS provided GameData given to the alliance teams at the start of the match. 3 Character String containing `L` and `R` only. The first character represents the near switch, the 2nd the scale, and the 3rd the far, opposing, switch from the alliance's perspective. An `L` in a position indicates the platform on the left will be lit for the alliance while an `R` will indicate the right platform will be lit for the alliance. See also [WPI Screen Steps](https://wpilib.screenstepslive.com/s/currentCS/m/getting_started/l/826278-2018-game-data-details).

class MatchTimeseries2018(NamedTuple):
    """Timeseries data for the 2018 game *FIRST* POWER UP.
*WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
*WARNING:* This model is currently under active development and may change at any time, including in breaking ways."""
    data: dict
    event_key: str  # TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.
    match_id: str  # Match ID consisting of the level, match number, and set number, eg `qm45` or `f1m1`.
    mode: str  # Current mode of play, can be `pre_match`, `auto`, `telop`, or `post_match`.
    play: int
    time_remaining: int  # Amount of time remaining in the match, only valid during `auto` and `teleop` modes.
    blue_auto_quest: int  # 1 if the blue alliance is credited with the AUTO QUEST, 0 if not.
    blue_boost_count: int  # Number of POWER CUBES in the BOOST section of the blue alliance VAULT.
    blue_boost_played: int  # Returns 1 if the blue alliance BOOST was played, or 0 if not played.
    blue_current_powerup: str  # Name of the current blue alliance POWER UP being played, or `null`.
    blue_face_the_boss: int  # 1 if the blue alliance is credited with FACING THE BOSS, 0 if not.
    blue_force_count: int  # Number of POWER CUBES in the FORCE section of the blue alliance VAULT.
    blue_force_played: int  # Returns 1 if the blue alliance FORCE was played, or 0 if not played.
    blue_levitate_count: int  # Number of POWER CUBES in the LEVITATE section of the blue alliance VAULT.
    blue_levitate_played: int  # Returns 1 if the blue alliance LEVITATE was played, or 0 if not played.
    blue_powerup_time_remaining: str  # Number of seconds remaining in the blue alliance POWER UP time, or 0 if none is active.
    blue_scale_owned: int  # 1 if the blue alliance owns the SCALE, 0 if not.
    blue_score: int  # Current score for the blue alliance.
    blue_switch_owned: int  # 1 if the blue alliance owns their SWITCH, 0 if not.
    red_auto_quest: int  # 1 if the red alliance is credited with the AUTO QUEST, 0 if not.
    red_boost_count: int  # Number of POWER CUBES in the BOOST section of the red alliance VAULT.
    red_boost_played: int  # Returns 1 if the red alliance BOOST was played, or 0 if not played.
    red_current_powerup: str  # Name of the current red alliance POWER UP being played, or `null`.
    red_face_the_boss: int  # 1 if the red alliance is credited with FACING THE BOSS, 0 if not.
    red_force_count: int  # Number of POWER CUBES in the FORCE section of the red alliance VAULT.
    red_force_played: int  # Returns 1 if the red alliance FORCE was played, or 0 if not played.
    red_levitate_count: int  # Number of POWER CUBES in the LEVITATE section of the red alliance VAULT.
    red_levitate_played: int  # Returns 1 if the red alliance LEVITATE was played, or 0 if not played.
    red_powerup_time_remaining: str  # Number of seconds remaining in the red alliance POWER UP time, or 0 if none is active.
    red_scale_owned: int  # 1 if the red alliance owns the SCALE, 0 if not.
    red_score: int  # Current score for the red alliance.
    red_switch_owned: int  # 1 if the red alliance owns their SWITCH, 0 if not.

class MatchScoreBreakdown2019(NamedTuple):
    """See the 2019 FMS API documentation for a description of each value. https://frcevents2.docs.apiary.io/#/reference/match-results/score-details"""
    data: dict
    blue: "MatchScoreBreakdown2019Alliance"
    red: "MatchScoreBreakdown2019Alliance"

class MatchScoreBreakdown2019Alliance(NamedTuple):
    data: dict
    adjustPoints: int
    autoPoints: int
    bay1: str
    bay2: str
    bay3: str
    bay4: str
    bay5: str
    bay6: str
    bay7: str
    bay8: str
    cargoPoints: int
    completeRocketRankingPoint: bool
    completedRocketFar: bool
    completedRocketNear: bool
    endgameRobot1: str
    endgameRobot2: str
    endgameRobot3: str
    foulCount: int
    foulPoints: int
    habClimbPoints: int
    habDockingRankingPoint: bool
    habLineRobot1: str
    habLineRobot2: str
    habLineRobot3: str
    hatchPanelPoints: int
    lowLeftRocketFar: str
    lowLeftRocketNear: str
    lowRightRocketFar: str
    lowRightRocketNear: str
    midLeftRocketFar: str
    midLeftRocketNear: str
    midRightRocketFar: str
    midRightRocketNear: str
    preMatchBay1: str
    preMatchBay2: str
    preMatchBay3: str
    preMatchBay6: str
    preMatchBay7: str
    preMatchBay8: str
    preMatchLevelRobot1: str
    preMatchLevelRobot2: str
    preMatchLevelRobot3: str
    rp: int
    sandStormBonusPoints: int
    techFoulCount: int
    teleopPoints: int
    topLeftRocketFar: str
    topLeftRocketNear: str
    topRightRocketFar: str
    topRightRocketNear: str
    totalPoints: int

class MatchScoreBreakdown2020(NamedTuple):
    """See the 2020 FMS API documentation for a description of each value. https://frcevents2.docs.apiary.io/#/reference/match-results/score-details"""
    data: dict
    blue: "MatchScoreBreakdown2020Alliance"
    red: "MatchScoreBreakdown2020Alliance"

class MatchScoreBreakdown2020Alliance(NamedTuple):
    data: dict
    initLineRobot1: str
    endgameRobot1: str
    initLineRobot2: str
    endgameRobot2: str
    initLineRobot3: str
    endgameRobot3: str
    autoCellsBottom: int
    autoCellsOuter: int
    autoCellsInner: int
    teleopCellsBottom: int
    teleopCellsOuter: int
    teleopCellsInner: int
    stage1Activated: bool
    stage2Activated: bool
    stage3Activated: bool
    stage3TargetColor: str
    endgameRungIsLevel: str
    autoInitLinePoints: int
    autoCellPoints: int
    autoPoints: int
    teleopCellPoints: int
    controlPanelPoints: int
    endgamePoints: int
    teleopPoints: int
    shieldOperationalRankingPoint: bool
    shieldEnergizedRankingPoint: bool
    foulCount: int
    techFoulCount: int
    adjustPoints: int
    foulPoints: int
    rp: int
    totalPoints: int

class Media(NamedTuple):
    """The `Media` object contains a reference for most any media associated with a team or event on TBA."""
    data: dict
    type: str  # String type of the media element.
    foreign_key: str  # The key used to identify this media on the media site.
    details: dict  # If required, a JSON dict of additional media information.
    preferred: bool  # True if the media is of high quality.
    direct_url: str  # Direct URL to the media.
    view_url: str  # The URL that leads to the full web page for the media, if one exists.

class EliminationAlliance(NamedTuple):
    data: dict
    name: str  # Alliance name, may be null.
    backup: dict  # Backup team called in, may be null.
    declines: List[str]  # List of teams that declined the alliance.
    picks: List[str]  # List of team keys picked for the alliance. First pick is captain.
    status: dict

class Award(NamedTuple):
    data: dict
    name: str  # The name of the award as provided by FIRST. May vary for the same award type.
    award_type: int  # Type of award given. See https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/award_type.py#L6
    event_key: str  # The event_key of the event the award was won at.
    recipient_list: "List[AwardRecipient]"  # A list of recipients of the award at the event. May have either a team_key or an awardee, both, or neither (in the case the award wasn't awarded at the event).
    year: int  # The year this award was won.

class AwardRecipient(NamedTuple):
    """An `Award_Recipient` object represents the team and/or person who received an award at an event."""
    data: dict
    team_key: str  # The TBA team key for the team that was given the award. May be null.
    awardee: str  # The name of the individual given the award. May be null.

class DistrictList(NamedTuple):
    data: dict
    abbreviation: str  # The short identifier for the district.
    display_name: str  # The long name for the district.
    key: str  # Key for this district, e.g. `2016ne`.
    year: int  # Year this district participated.

class DistrictRanking(NamedTuple):
    """Rank of a team in a district."""
    data: dict
    team_key: str  # TBA team key for the team.
    rank: int  # Numerical rank of the team, 1 being top rank.
    rookie_bonus: int  # Any points added to a team as a result of the rookie bonus.
    point_total: int  # Total district points for the team.
    event_points: List[dict]  # List of events that contributed to the point total for the team.

class WLTRecord(NamedTuple):
    """A Win-Loss-Tie record for a team, or an alliance."""
    data: dict
    losses: int  # Number of losses.
    wins: int  # Number of wins.
    ties: int  # Number of ties.

class Webcast(NamedTuple):
    data: dict
    type: str  # Type of webcast, typically descriptive of the streaming provider.
    channel: str  # Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.
    file: str  # File identification as may be required for some types. May be null.
