import csv
from typing import TextIO

all_track_ids = []
ids_file = open('valid_track_ids.txt', 'r')
for line in ids_file:
    curr_track_id = line.strip('\n')
    all_track_ids.append(curr_track_id)

with open('tracks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    output_file: TextIO = open('tracks.txt', 'w')
    output_file.write("")
    for row in csv_reader:
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
                print("ERROR: race_type " + race_type + "  LineNum: " + str(line_count + 2))
                continue

            if race_type == "racing" and not laps.isnumeric():
                print("ERROR: race without valid laps  LineNum: " + str(line_count + 1))
                continue
            if race_type == "team race" and (not laps.isnumeric() or not num_teams.isnumeric()):
                print("ERROR: team race without valid laps or number of teams  LineNum: " + str(line_count + 1))
                continue
            if race_type == "derby deathmatch" and not minutes.isnumeric():
                print("ERROR: deathmatch without time limit  LineNum: " + str(line_count + 1))
                continue
            if race_type == "team derby" and (not minutes.isnumeric() or not num_teams.isnumeric()):
                print("ERROR: team deathmatch without valid time limit or number of teams  LineNum: " + str(
                    line_count + 1))
                continue

            if track_id not in all_track_ids:
                print("ERROR: track id not found: " + track_id + "  LineNum: " + str(line_count + 1))
                continue

            output_file.write("# Race " + str(line_count - 1) + "\n")
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

    print("tracks.py finished running. \n")
