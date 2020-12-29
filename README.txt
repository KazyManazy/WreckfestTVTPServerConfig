Requirements:
Make sure at least python 3 is installed on your computer by doing the following:
1. Open command prompt by typing CMD in Windows Search Bar
2. Type python into the Command Prompt
3. If you see at least python3.XX.XX, you are done. (XX.XX is just the version and any version of python3 should work)
4. If you do not see python3. then you need to download python here: https://www.python.org/downloads/
5. Once this is downloaded type python back into the command prompt and you should see python3.XX.XX come up.
6. Make sure the mods are ready to use by doing the following:
IN ORDER TO SET UP A TVTP SERVER FOLLOW THESE STEPS:
Step 1: Subscribe and download The Very TrackPack from Steam Workshop
Step 2: Copy the 764432700 folder from the Steam Workshops Folder to the mods folder
764432700 can usually be found here: <Your Steam Folder>/steamapps/workshop/content/228380/764432700
764432700 is the TVTP mod files, so this is the folder that needs to be copied.
The mods folder can be found here: <Your Steam Folder>/steamapps/common/Wreckfest/mods
Step 3: Add the mods to the server config file (ALREADY DONE IN server_config.py)
Step 4: Run the server_config.py in command prompt by typing python server_config.py in the folder it is located.
More directions about how to navigate to the correct folder are in the NOTES below.
Step 5: Go the the output file: full_server_config.txt and copy the whole text file. Paste this in the server_config.cfg file or in the initial_server_config file if you've not run a server before.
The server_config file can be found here: <Your Steam Folder>/steamapps/common/Wreckfest
Step 6: Double click the start_server Windows batch file
The windows batch file can be found here: <Your Steam Folder>/steamapps/common/Wreckfest
Step 7: The server now should be running!!!

NOTES:
- These scripts only work with base game tracks and TVTP tracks.
- Examples of appropriate CSV files can be found here: https://docs.google.com/spreadsheets/d/1yuHh_otIhdrnrsIlpe1cXa0KekiNJMbX5vFDmECWGfY/edit#gid=0
- Basic command prompt commands:
The command prompt shows your current folder, or directory at the left hand side of the screen.
dir - outputs all the files and folders in the current folder
cd <FOLDER NAME> - changes the current folder to the new folder
cd .. - goes back one folder (for example. C:\Users\myself>cd .. would change to C:\Users>
python <FILE NAME> - runs the python file

Files:

tracks.csv
Description: Can be opened in Google Sheets, Microsoft Excel, etc.  This is a sheet that contains all the tracks to be
put into the rotation with their valid server names. (Not the same names as in Wreckfest Track Options in game)

valid_tracks_ids.txt
Description: Contains a list of all the valid track names that can usually be found at the following addresses:
<Your Steam Folder>/steamapps/workshop/content/228380/764432700/data/property/event/ (TVTP Tracks)
<Your Steam Folder>/steamapps/common/Wreckfest/data/property/event (Base Game)
If any tracks are added to the TVTP, they will need to be found in the folders at the previous address and added to the
valid_tracks_ids.txt file, each on a new line

tracks.py
Description: Creates a tracks.txt file from tracks.csv that can be copied and pasted into the event rotation.
Run it by doing the following:
1. Open the command prompt.
2. Navigate to the folder this file is in on the command prompt.
3. Type python track.py into the command prompt.
4. The tracks.txt file should have been created or updated.

tracks.txt
Description: Once tracks.py is run, this file can be copied and pasted into the track rotation at the bottom of the
server_config.cfg file.

admins.csv
moderators.csv
banned.csv
Description: All of these files include steamIDs that will populate lists in the server config file.
In order to get the Steam ID follow these steps:
1. Find the user's Steam Profile web URL on their profile page.
2. Copy and paste the URL at this address https://steamid.io/lookup
3. The SteamID is labeled steamID64

server_config.py
Description: Creates the server_config.txt file that can be copied and pasted over the enter server_config.cfg file for
running the server.
Run it by doing the following:
1. Open the command prompt.
2. Navigate to the folder this file is in on the command prompt.
3. Type python server_config.py into the command prompt.
4. The server_config.txt file should have been created or updated.

server_config.txt
Description: Once server_config.py is run this file can be copy and pasted to replace the server_config.cfg file.

