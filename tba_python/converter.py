# The Blue Alliance API Version 3.8.0 

from models import *

def convertToAPIStatus(data):
    return APIStatus(
        data,
        data["current_season"],
        data["max_season"],
        data["is_datafeed_down"],
        data["down_events"],
        convertToAPIStatusAppVersion(data["ios"]),
        convertToAPIStatusAppVersion(data["android"])
    )

def convertToAPIStatusAppVersion(data):
    return APIStatusAppVersion(
        data,
        data["min_app_version"],
        data["latest_app_version"]
    )

def convertToTeamSimple(data):
    return TeamSimple(
        data,
        data["key"],
        data["team_number"],
        data["nickname"],
        data["name"],
        data["city"],
        data["state_prov"],
        data["country"]
    )

def convertToTeam(data):
    return Team(
        data,
        data["key"],
        data["team_number"],
        data["nickname"],
        data["name"],
        data["school_name"],
        data["city"],
        data["state_prov"],
        data["country"],
        data["address"],
        data["postal_code"],
        data["gmaps_place_id"],
        data["gmaps_url"],
        data["lat"],
        data["lng"],
        data["location_name"],
        data["website"],
        data["rookie_year"],
        data["motto"],
        data["home_championship"]
    )

def convertToTeamRobot(data):
    return TeamRobot(
        data,
        data["year"],
        data["robot_name"],
        data["key"],
        data["team_key"]
    )

def convertToEventSimple(data):
    return EventSimple(
        data,
        data["key"],
        data["name"],
        data["event_code"],
        data["event_type"],
        convertToDistrictList(data["district"]),
        data["city"],
        data["state_prov"],
        data["country"],
        data["start_date"],
        data["end_date"],
        data["year"]
    )

def convertToEvent(data):
    return Event(
        data,
        data["key"],
        data["name"],
        data["event_code"],
        data["event_type"],
        convertToDistrictList(data["district"]),
        data["city"],
        data["state_prov"],
        data["country"],
        data["start_date"],
        data["end_date"],
        data["year"],
        data["short_name"],
        data["event_type_string"],
        data["week"],
        data["address"],
        data["postal_code"],
        data["gmaps_place_id"],
        data["gmaps_url"],
        data["lat"],
        data["lng"],
        data["location_name"],
        data["timezone"],
        data["website"],
        data["first_event_id"],
        data["first_event_code"],
        [convertToWebcast (item) for item in data["webcasts"]],
        data["division_keys"],
        data["parent_event_key"],
        data["playoff_type"],
        data["playoff_type_string"]
    )

def convertToTeamEventStatus(data):
    return TeamEventStatus(
        data,
        convertToTeamEventStatusRank(data["qual"]),
        convertToTeamEventStatusAlliance(data["alliance"]),
        convertToTeamEventStatusPlayoff(data["playoff"]),
        data["alliance_status_str"],
        data["playoff_status_str"],
        data["overall_status_str"],
        data["next_match_key"],
        data["last_match_key"]
    )

def convertToTeamEventStatusRank(data):
    return TeamEventStatusRank(
        data,
        data["num_teams"],
        data["ranking"],
        data["sort_order_info"],
        data["status"]
    )

def convertToTeamEventStatusAlliance(data):
    return TeamEventStatusAlliance(
        data,
        data["name"],
        data["number"],
        convertToTeamEventStatusAllianceBackup(data["backup"]),
        data["pick"]
    )

def convertToTeamEventStatusAllianceBackup(data):
    return TeamEventStatusAllianceBackup(
        data,
        data["out"],
        data["in"]
    )

def convertToTeamEventStatusPlayoff(data):
    return TeamEventStatusPlayoff(
        data,
        data["level"],
        convertToWLTRecord(data["current_level_record"]),
        convertToWLTRecord(data["record"]),
        data["status"],
        data["playoff_average"]
    )

def convertToEventRanking(data):
    return EventRanking(
        data,
        data["rankings"],
        data["extra_stats_info"],
        data["sort_order_info"]
    )

def convertToEventDistrictPoints(data):
    return EventDistrictPoints(
        data,
        data["points"],
        data["tiebreakers"]
    )

def convertToEventInsights(data):
    return EventInsights(
        data,
        data["qual"],
        data["playoff"]
    )

def convertToEventInsights2016(data):
    return EventInsights2016(
        data,
        data["LowBar"],
        data["A_ChevalDeFrise"],
        data["A_Portcullis"],
        data["B_Ramparts"],
        data["B_Moat"],
        data["C_SallyPort"],
        data["C_Drawbridge"],
        data["D_RoughTerrain"],
        data["D_RockWall"],
        data["average_high_goals"],
        data["average_low_goals"],
        data["breaches"],
        data["scales"],
        data["challenges"],
        data["captures"],
        data["average_win_score"],
        data["average_win_margin"],
        data["average_score"],
        data["average_auto_score"],
        data["average_crossing_score"],
        data["average_boulder_score"],
        data["average_tower_score"],
        data["average_foul_score"],
        data["high_score"]
    )

def convertToEventInsights2017(data):
    return EventInsights2017(
        data,
        data["average_foul_score"],
        data["average_fuel_points"],
        data["average_fuel_points_auto"],
        data["average_fuel_points_teleop"],
        data["average_high_goals"],
        data["average_high_goals_auto"],
        data["average_high_goals_teleop"],
        data["average_low_goals"],
        data["average_low_goals_auto"],
        data["average_low_goals_teleop"],
        data["average_mobility_points_auto"],
        data["average_points_auto"],
        data["average_points_teleop"],
        data["average_rotor_points"],
        data["average_rotor_points_auto"],
        data["average_rotor_points_teleop"],
        data["average_score"],
        data["average_takeoff_points_teleop"],
        data["average_win_margin"],
        data["average_win_score"],
        data["high_kpa"],
        data["high_score"],
        data["kpa_achieved"],
        data["mobility_counts"],
        data["rotor_1_engaged"],
        data["rotor_1_engaged_auto"],
        data["rotor_2_engaged"],
        data["rotor_2_engaged_auto"],
        data["rotor_3_engaged"],
        data["rotor_4_engaged"],
        data["takeoff_counts"],
        data["unicorn_matches"]
    )

def convertToEventInsights2018(data):
    return EventInsights2018(
        data,
        data["auto_quest_achieved"],
        data["average_boost_played"],
        data["average_endgame_points"],
        data["average_force_played"],
        data["average_foul_score"],
        data["average_points_auto"],
        data["average_points_teleop"],
        data["average_run_points_auto"],
        data["average_scale_ownership_points"],
        data["average_scale_ownership_points_auto"],
        data["average_scale_ownership_points_teleop"],
        data["average_score"],
        data["average_switch_ownership_points"],
        data["average_switch_ownership_points_auto"],
        data["average_switch_ownership_points_teleop"],
        data["average_vault_points"],
        data["average_win_margin"],
        data["average_win_score"],
        data["boost_played_counts"],
        data["climb_counts"],
        data["face_the_boss_achieved"],
        data["force_played_counts"],
        data["high_score"],
        data["levitate_played_counts"],
        data["run_counts_auto"],
        data["scale_neutral_percentage"],
        data["scale_neutral_percentage_auto"],
        data["scale_neutral_percentage_teleop"],
        data["switch_owned_counts_auto"],
        data["unicorn_matches"],
        data["winning_opp_switch_denial_percentage_teleop"],
        data["winning_own_switch_ownership_percentage"],
        data["winning_own_switch_ownership_percentage_auto"],
        data["winning_own_switch_ownership_percentage_teleop"],
        data["winning_scale_ownership_percentage"],
        data["winning_scale_ownership_percentage_auto"],
        data["winning_scale_ownership_percentage_teleop"]
    )

def convertToEventOPRs(data):
    return EventOPRs(
        data,
        data["oprs"],
        data["dprs"],
        data["ccwms"]
    )

def convertToEventPredictions(data):
    return EventPredictions(
        data,
        
    )

def convertToMatchSimple(data):
    return MatchSimple(
        data,
        data["key"],
        data["comp_level"],
        data["set_number"],
        data["match_number"],
        Alliances(
            convertToMatchAlliance(data["alliances"]["blue"]),
            convertToMatchAlliance(data["alliances"]["red"])
        ),
        data["winning_alliance"],
        data["event_key"],
        data["time"],
        data["predicted_time"],
        data["actual_time"]
    )

def convertToMatch(data):
    return Match(
        data,
        data["key"],
        data["comp_level"],
        data["set_number"],
        data["match_number"],
        Alliances(
            convertToMatchAlliance(data["alliances"]["blue"]),
            convertToMatchAlliance(data["alliances"]["red"])
        ),
        data["winning_alliance"],
        data["event_key"],
        data["time"],
        data["actual_time"],
        data["predicted_time"],
        data["post_result_time"],
        data["score_breakdown"],
        data["videos"]
    )

def convertToMatchAlliance(data):
    return MatchAlliance(
        data,
        data["score"],
        data["team_keys"],
        data["surrogate_team_keys"],
        data["dq_team_keys"]
    )

def convertToZebra(data):
    return Zebra(
        data,
        data["key"],
        data["times"],
        Alliances(
            convertToZebraTeam(data["alliances"]["blue"]),
            convertToZebraTeam(data["alliances"]["red"])
        )
    )

def convertToZebraTeam(data):
    return ZebraTeam(
        data,
        data["team_key"],
        data["xs"],
        data["ys"]
    )

def convertToMatchScoreBreakdown2015(data):
    return MatchScoreBreakdown2015(
        data,
        convertToMatchScoreBreakdown2015Alliance(data["blue"]),
        convertToMatchScoreBreakdown2015Alliance(data["red"]),
        data["coopertition"],
        data["coopertition_points"]
    )

def convertToMatchScoreBreakdown2015Alliance(data):
    return MatchScoreBreakdown2015Alliance(
        data,
        data["auto_points"],
        data["teleop_points"],
        data["container_points"],
        data["tote_points"],
        data["litter_points"],
        data["foul_points"],
        data["adjust_points"],
        data["total_points"],
        data["foul_count"],
        data["tote_count_far"],
        data["tote_count_near"],
        data["tote_set"],
        data["tote_stack"],
        data["container_count_level1"],
        data["container_count_level2"],
        data["container_count_level3"],
        data["container_count_level4"],
        data["container_count_level5"],
        data["container_count_level6"],
        data["container_set"],
        data["litter_count_container"],
        data["litter_count_landfill"],
        data["litter_count_unprocessed"],
        data["robot_set"]
    )

def convertToMatchScoreBreakdown2016(data):
    return MatchScoreBreakdown2016(
        data,
        convertToMatchScoreBreakdown2016Alliance(data["blue"]),
        convertToMatchScoreBreakdown2016Alliance(data["red"])
    )

def convertToMatchScoreBreakdown2016Alliance(data):
    return MatchScoreBreakdown2016Alliance(
        data,
        data["autoPoints"],
        data["teleopPoints"],
        data["breachPoints"],
        data["foulPoints"],
        data["capturePoints"],
        data["adjustPoints"],
        data["totalPoints"],
        data["robot1Auto"],
        data["robot2Auto"],
        data["robot3Auto"],
        data["autoReachPoints"],
        data["autoCrossingPoints"],
        data["autoBouldersLow"],
        data["autoBouldersHigh"],
        data["autoBoulderPoints"],
        data["teleopCrossingPoints"],
        data["teleopBouldersLow"],
        data["teleopBouldersHigh"],
        data["teleopBoulderPoints"],
        data["teleopDefensesBreached"],
        data["teleopChallengePoints"],
        data["teleopScalePoints"],
        data["teleopTowerCaptured"],
        data["towerFaceA"],
        data["towerFaceB"],
        data["towerFaceC"],
        data["towerEndStrength"],
        data["techFoulCount"],
        data["foulCount"],
        data["position2"],
        data["position3"],
        data["position4"],
        data["position5"],
        data["position1crossings"],
        data["position2crossings"],
        data["position3crossings"],
        data["position4crossings"],
        data["position5crossings"]
    )

def convertToMatchScoreBreakdown2017(data):
    return MatchScoreBreakdown2017(
        data,
        convertToMatchScoreBreakdown2017Alliance(data["blue"]),
        convertToMatchScoreBreakdown2017Alliance(data["red"])
    )

def convertToMatchScoreBreakdown2017Alliance(data):
    return MatchScoreBreakdown2017Alliance(
        data,
        data["autoPoints"],
        data["teleopPoints"],
        data["foulPoints"],
        data["adjustPoints"],
        data["totalPoints"],
        data["robot1Auto"],
        data["robot2Auto"],
        data["robot3Auto"],
        data["rotor1Auto"],
        data["rotor2Auto"],
        data["autoFuelLow"],
        data["autoFuelHigh"],
        data["autoMobilityPoints"],
        data["autoRotorPoints"],
        data["autoFuelPoints"],
        data["teleopFuelPoints"],
        data["teleopFuelLow"],
        data["teleopFuelHigh"],
        data["teleopRotorPoints"],
        data["kPaRankingPointAchieved"],
        data["teleopTakeoffPoints"],
        data["kPaBonusPoints"],
        data["rotorBonusPoints"],
        data["rotor1Engaged"],
        data["rotor2Engaged"],
        data["rotor3Engaged"],
        data["rotor4Engaged"],
        data["rotorRankingPointAchieved"],
        data["techFoulCount"],
        data["foulCount"],
        data["touchpadNear"],
        data["touchpadMiddle"],
        data["touchpadFar"]
    )

def convertToMatchScoreBreakdown2018(data):
    return MatchScoreBreakdown2018(
        data,
        convertToMatchScoreBreakdown2018Alliance(data["blue"]),
        convertToMatchScoreBreakdown2018Alliance(data["red"])
    )

def convertToMatchScoreBreakdown2018Alliance(data):
    return MatchScoreBreakdown2018Alliance(
        data,
        data["adjustPoints"],
        data["autoOwnershipPoints"],
        data["autoPoints"],
        data["autoQuestRankingPoint"],
        data["autoRobot1"],
        data["autoRobot2"],
        data["autoRobot3"],
        data["autoRunPoints"],
        data["autoScaleOwnershipSec"],
        data["autoSwitchAtZero"],
        data["autoSwitchOwnershipSec"],
        data["endgamePoints"],
        data["endgameRobot1"],
        data["endgameRobot2"],
        data["endgameRobot3"],
        data["faceTheBossRankingPoint"],
        data["foulCount"],
        data["foulPoints"],
        data["rp"],
        data["techFoulCount"],
        data["teleopOwnershipPoints"],
        data["teleopPoints"],
        data["teleopScaleBoostSec"],
        data["teleopScaleForceSec"],
        data["teleopScaleOwnershipSec"],
        data["teleopSwitchBoostSec"],
        data["teleopSwitchForceSec"],
        data["teleopSwitchOwnershipSec"],
        data["totalPoints"],
        data["vaultBoostPlayed"],
        data["vaultBoostTotal"],
        data["vaultForcePlayed"],
        data["vaultForceTotal"],
        data["vaultLevitatePlayed"],
        data["vaultLevitateTotal"],
        data["vaultPoints"],
        data["tba_gameData"]
    )

def convertToMatchTimeseries2018(data):
    return MatchTimeseries2018(
        data,
        data["event_key"],
        data["match_id"],
        data["mode"],
        data["play"],
        data["time_remaining"],
        data["blue_auto_quest"],
        data["blue_boost_count"],
        data["blue_boost_played"],
        data["blue_current_powerup"],
        data["blue_face_the_boss"],
        data["blue_force_count"],
        data["blue_force_played"],
        data["blue_levitate_count"],
        data["blue_levitate_played"],
        data["blue_powerup_time_remaining"],
        data["blue_scale_owned"],
        data["blue_score"],
        data["blue_switch_owned"],
        data["red_auto_quest"],
        data["red_boost_count"],
        data["red_boost_played"],
        data["red_current_powerup"],
        data["red_face_the_boss"],
        data["red_force_count"],
        data["red_force_played"],
        data["red_levitate_count"],
        data["red_levitate_played"],
        data["red_powerup_time_remaining"],
        data["red_scale_owned"],
        data["red_score"],
        data["red_switch_owned"]
    )

def convertToMatchScoreBreakdown2019(data):
    return MatchScoreBreakdown2019(
        data,
        convertToMatchScoreBreakdown2019Alliance(data["blue"]),
        convertToMatchScoreBreakdown2019Alliance(data["red"])
    )

def convertToMatchScoreBreakdown2019Alliance(data):
    return MatchScoreBreakdown2019Alliance(
        data,
        data["adjustPoints"],
        data["autoPoints"],
        data["bay1"],
        data["bay2"],
        data["bay3"],
        data["bay4"],
        data["bay5"],
        data["bay6"],
        data["bay7"],
        data["bay8"],
        data["cargoPoints"],
        data["completeRocketRankingPoint"],
        data["completedRocketFar"],
        data["completedRocketNear"],
        data["endgameRobot1"],
        data["endgameRobot2"],
        data["endgameRobot3"],
        data["foulCount"],
        data["foulPoints"],
        data["habClimbPoints"],
        data["habDockingRankingPoint"],
        data["habLineRobot1"],
        data["habLineRobot2"],
        data["habLineRobot3"],
        data["hatchPanelPoints"],
        data["lowLeftRocketFar"],
        data["lowLeftRocketNear"],
        data["lowRightRocketFar"],
        data["lowRightRocketNear"],
        data["midLeftRocketFar"],
        data["midLeftRocketNear"],
        data["midRightRocketFar"],
        data["midRightRocketNear"],
        data["preMatchBay1"],
        data["preMatchBay2"],
        data["preMatchBay3"],
        data["preMatchBay6"],
        data["preMatchBay7"],
        data["preMatchBay8"],
        data["preMatchLevelRobot1"],
        data["preMatchLevelRobot2"],
        data["preMatchLevelRobot3"],
        data["rp"],
        data["sandStormBonusPoints"],
        data["techFoulCount"],
        data["teleopPoints"],
        data["topLeftRocketFar"],
        data["topLeftRocketNear"],
        data["topRightRocketFar"],
        data["topRightRocketNear"],
        data["totalPoints"]
    )

def convertToMatchScoreBreakdown2020(data):
    return MatchScoreBreakdown2020(
        data,
        convertToMatchScoreBreakdown2020Alliance(data["blue"]),
        convertToMatchScoreBreakdown2020Alliance(data["red"])
    )

def convertToMatchScoreBreakdown2020Alliance(data):
    return MatchScoreBreakdown2020Alliance(
        data,
        data["initLineRobot1"],
        data["endgameRobot1"],
        data["initLineRobot2"],
        data["endgameRobot2"],
        data["initLineRobot3"],
        data["endgameRobot3"],
        data["autoCellsBottom"],
        data["autoCellsOuter"],
        data["autoCellsInner"],
        data["teleopCellsBottom"],
        data["teleopCellsOuter"],
        data["teleopCellsInner"],
        data["stage1Activated"],
        data["stage2Activated"],
        data["stage3Activated"],
        data["stage3TargetColor"],
        data["endgameRungIsLevel"],
        data["autoInitLinePoints"],
        data["autoCellPoints"],
        data["autoPoints"],
        data["teleopCellPoints"],
        data["controlPanelPoints"],
        data["endgamePoints"],
        data["teleopPoints"],
        data["shieldOperationalRankingPoint"],
        data["shieldEnergizedRankingPoint"],
        data["foulCount"],
        data["techFoulCount"],
        data["adjustPoints"],
        data["foulPoints"],
        data["rp"],
        data["totalPoints"]
    )

def convertToMedia(data):
    return Media(
        data,
        data["type"],
        data["foreign_key"],
        data["details"],
        data["preferred"],
        data["direct_url"],
        data["view_url"]
    )

def convertToEliminationAlliance(data):
    return EliminationAlliance(
        data,
        data["name"],
        data["backup"],
        data["declines"],
        data["picks"],
        data["status"]
    )

def convertToAward(data):
    return Award(
        data,
        data["name"],
        data["award_type"],
        data["event_key"],
        [convertToAwardRecipient (item) for item in data["recipient_list"]],
        data["year"]
    )

def convertToAwardRecipient(data):
    return AwardRecipient(
        data,
        data["team_key"],
        data["awardee"]
    )

def convertToDistrictList(data):
    return DistrictList(
        data,
        data["abbreviation"],
        data["display_name"],
        data["key"],
        data["year"]
    )

def convertToDistrictRanking(data):
    return DistrictRanking(
        data,
        data["team_key"],
        data["rank"],
        data["rookie_bonus"],
        data["point_total"],
        data["event_points"]
    )

def convertToWLTRecord(data):
    return WLTRecord(
        data,
        data["losses"],
        data["wins"],
        data["ties"]
    )

def convertToWebcast(data):
    return Webcast(
        data,
        data["type"],
        data["channel"],
        data["file"]
    )
