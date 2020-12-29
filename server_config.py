import csv
from typing import TextIO

# IN ORDER TO SET UP A TVTP SERVER FOLLOW THESE STEPS:
# Step 1: Subscribe and download The Very TrackPack from Steam Workshop
# Step 2: Copy the 764432700 folder from the Steam Workshops Folder to the mods folder
# 764432700 can usually be found here: <Your Steam Folder>/steamapps/workshop/content/228380/764432700
# 764432700 is the TVTP mod files, so this is the folder that needs to be copied.
# The mods folder can be found here: <Your Steam Folder>/steamapps/common/Wreckfest/mods
# Step 3: Add the mods to the server config file (ALREADY DONE BELOW)
# Step 4: Run this file in command prompt by typing python server_config.py
# Step 5: Go the the output file: full_server_config.txt and copy the whole text file. Paste this in the server_config.cfg file or in the initial_server_config file if you've not run a server before.
# The server_config file can be found here: <Your Steam Folder>/steamapps/common/Wreckfest
# Step 6: Double click the start_server Windows batch file
# Step 7: The server now should be running!!!


output_file: TextIO = open('full_server_config.txt', 'w')
output_file.write("")

# Name
output_file.write("server_name=\"^5KazyManazy's ^6TVTP Test ^5Server\"")
output_file.write("\n")
# Server Message
step1 = "^5Step 1: Google The Very TrackPack    "
step2 = "^6Step 2: Subscribe to The Very TrackPack on Steam Workshop and wait for download to complete    "
step3 = "^5Step 3: Got to the Misc Tab on Wreckfest, Go to Mods, Check the mark besides The Very TrackPack "
output_file.write("welcome_message=" + step1 + step2 + step3)
output_file.write("\n")
# Password (leave blank for none)
output_file.write("password=")
output_file.write("\n")
# Max Players
output_file.write("max_players=24")
output_file.write("\n")
output_file.write("\n")

#LAN only, 0 = use steam, 1 = LAN only (not on internet)
output_file.write("lan=0")
output_file.write("\n")

# Server Ports (These are the default, you will need to forward ports UDP 27015, UDP 27016, UDP 33540, TCP 27015 in your router)
output_file.write("steam_port=27015")
output_file.write("\n")
output_file.write("game_port=33540")
output_file.write("\n")
output_file.write("query_port=27016")
output_file.write("\n")
output_file.write("\n")

# OPTIONS

# Quickplay 0 = wont join from quick match, 1 = can join from quick match
output_file.write("exclude_from_quickplay=1")
output_file.write("\n")

# Clear Previous Privileges 0 = keep previous privileges, 1 = clear privileges (admins, mods)
output_file.write("clear_users=0")
output_file.write("\n")

# Give owner privileges 0 = first to join receives, doesn't receive owner priveleges
output_file.write("owner_disabled=1")
output_file.write("\n")

# Admin Start Timer 0 = automatic countdown, 1 = admin starts countdown
output_file.write("admin_control=0")
output_file.write("\n")

# Lobby countdown between 30 and 127 seconds
output_file.write("lobby_countdown=30")
output_file.write("\n")

# Percentage of players required for auto countdown
output_file.write("ready_players_required=50")
output_file.write("\n")

#Admin/Moderator
with open('admins.csv') as admin_csv_file:
    admin_csv_reader = csv.reader(admin_csv_file, delimiter=',')
    line_count = 0
    admin_list = ""
    for row in admin_csv_reader:
        if line_count == 2:
            admin_list = admin_list + row[1]
        elif line_count > 2:
            admin_list = admin_list + "," + row[1]
        line_count = line_count+1
    output_file.write("admin_steam_ids=" + admin_list)
    output_file.write("\n")
with open('moderators.csv') as moderators_csv_file:
    moderators_csv_reader = csv.reader(moderators_csv_file, delimiter=',')
    line_count = 0
    moderators_list = ""
    for row in moderators_csv_reader:
        if line_count == 2:
            moderators_list = moderators_list + row[1]
        elif line_count > 2:
            moderators_list = moderators_list + "," + row[1]
        line_count = line_count+1
    output_file.write("op_steam_ids=" + moderators_list)
    output_file.write("\n")

# enable track voting 0 = no voting, 1 = voting enabled
output_file.write("enable_track_vote=1")
output_file.write("\n")

# Set initial track
output_file.write("track=colosseum_event_02")
output_file.write("\n")

# Set initial game mode
output_file.write("gamemode=derby")
output_file.write("\n")

# Prepopulated Bots in Server
output_file.write("bots=16")
output_file.write("\n")

# Bot difficulty novice, amateur, expert
output_file.write("ai_difficulty=expert")
output_file.write("\n")

# Number of default teams in team modes
output_file.write("num_teams=2")
output_file.write("\n")

# Number of default laps in race mode
output_file.write("laps=2")
output_file.write("\n")

# Number of default minutes for deathmatch
output_file.write("time_limit=6")
output_file.write("\n")

# Number of default time interval with elimination race
output_file.write("elimination_interval=20")
output_file.write("\n")

# Set vehicle damage level normal, intense, or realistic
output_file.write("vehicle_damage=normal")
output_file.write("\n")

# car class restriction a, b, c, or d
output_file.write("car_class_restriction=a")
output_file.write("\n")

# specific car restriction (leave blank for none)
output_file.write("car_restriction=")
output_file.write("\n")

# Disable special vehicles 0 = special vehicles allowed, 1 = special vehicles NOT allowed
output_file.write("special_vehicles_disabled=0")
output_file.write("\n")

# Disable car reset 0 = cars can reset, 1 = cars can NOT reset
output_file.write("car_reset_disabled=0")
output_file.write("\n")

# Set car reset delay 1-20 seconds
output_file.write("car_reset_delay=5")
output_file.write("\n")

# Disable wrong way driving 0 = wrong way driving is slowed down, 1 = no limits to driving wrong way
output_file.write("wrong_way_limiter_disabled=1")
output_file.write("\n")

# Default weather setting
output_file.write("weather=")
output_file.write("\n")

# Set server update frequency low or high
output_file.write("frequency=high")
output_file.write("\n")

# A list of mods to be added. (764432700 is the TVTP)
output_file.write("mods=764432700")
output_file.write("\n")

# Save server messages to a log file
output_file.write("log=log.txt")
output_file.write("\n")



# valid_track_ids is populated with the names that will have to be entered into the track rotation.
# These names are already in the tracks.csv file, but if there is a misspelling in the csv file this will help find it.
# The location of the valid track ids can be found here: <Your Steam Folder>/steamapps/workshop/content/228380/764432700/data/property/event/...

all_track_ids = []
ids_file = open('valid_track_ids.txt', 'r')
for line in ids_file:
    curr_track_id = line.strip('\n')
    all_track_ids.append(curr_track_id)

with open('tracks.csv') as track_csv_file:
    track_csv_reader = csv.reader(track_csv_file, delimiter=',')
    line_count = 0
    for row in track_csv_reader:
        if line_count > 1:
            location = row[0].strip(" ")
            track_name = row[1].strip(" ")
            race_type = row[2].strip(" ")
            laps = row[3].strip(" ")
            minutes = row[4].strip(" ")
            num_teams = row[5].strip(" ")
            track_id = row[6].strip(" ")

            if race_type == "Banger Race":
                race_type = "racing"
            elif race_type == "Team Race":
                race_type = "team race"
            elif race_type == "Elimination Race":
                race_type = "elimination race"
            elif race_type == "Deathmatch":
                race_type = "derby deathmatch"
            elif race_type == "Team Deathmatch":
                race_type = "team derby"
            elif race_type == "Last Man Standing":
                race_type = "derby"
            else:
                print("ERROR: race_type " + race_type + "  LineNum: " + str(line_count+1))
                line_count = line_count + 1
                continue

            if race_type == "racing" and not laps.isnumeric():
                print("ERROR: race without valid laps  LineNum: " + str(line_count+1))
                line_count = line_count + 1
                continue
            if race_type == "team race" and (not laps.isnumeric() or not num_teams.isnumeric()):
                print("ERROR: team race without valid laps or number of teams  LineNum: " + str(line_count+1))
                line_count = line_count + 1
                continue
            if race_type == "derby deathmatch" and not minutes.isnumeric():
                print("ERROR: deathmatch without time limit  LineNum: " + str(line_count+1))
                line_count = line_count + 1
                continue
            if race_type == "team derby" and (not minutes.isnumeric() or not num_teams.isnumeric()):
                print("ERROR: team deathmatch without valid time limit or number of teams  LineNum: " + str(line_count+1))
                line_count = line_count + 1
                continue

            if track_id not in all_track_ids:
                print("ERROR: track id not found: " + track_id + "  LineNum: " + str(line_count+1))
                line_count = line_count + 1
                continue

            output_file.write("# Race " + str(line_count-1) + "\n")
            output_file.write("# Location: " + location + "\n")
            output_file.write("# Track Name: " + track_name + "\n")
            output_file.write("el_add=" + track_id + "\n")
            output_file.write("el_gamemode=" + race_type + "\n")
            output_file.write("el_num_teams=" + num_teams + "\n")
            output_file.write("el_laps=" + laps + "\n")
            output_file.write("el_elimination_interval=0" + "\n")
            output_file.write("el_car_reset_disabled=0" + "\n")
            output_file.write("el_wrong_way_limitel_disabled=1" + "\n")
            output_file.write("#el_car_class_restriction=a" + "\n")
            output_file.write("el_car_restriction=" + "\n")
            output_file.write("el_weather=" + "\n")
            output_file.write("\n")

        line_count = line_count + 1

output_file.close()