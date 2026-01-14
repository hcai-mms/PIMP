# Psychological Informed Music Player

This github contains a dataset collected and the tool to track music listening sessions.

## How-to setup a Last.FM Tracking

### Step 1: Register your application and get API Key and Secret

Check here and follow the steps: https://www.last.fm/api/webauth

### Step 2: 
Add your credentials to the environment variables:

'''
LASTFM_API_KEY = "YOUR API KEY"
LASTFM_API_SECRET = "YOUR API SECRET"
'''

## Dataset Files Description

notebook_explore_data.ipynb: Notebook of explorations of the data done for the paper can be viewed for reproducability.

<b>/data/id_user:</b> User ID with user answers of registration survey

<b>/data/id_tracks:</b> Extracted track information from LFM2b page while recording session

<b>/data/id_states:</b> Recorded states of the user at the start and end of each session

<b>/data/id_sessions:</b> user id, state ids, songs ids, and completion status of songs

## Paper

Please cite this paper:

Hausberger, Anna, Emilia Parada-Cabaleiro, and Markus Schedl. "Why Context Matters: Exploring How Musical Context Impacts User Behavior, Mood, and Musical Preferences." Proceedings of the 33rd ACM Conference on User Modeling, Adaptation and Personalization. 2025.

https://dl.acm.org/doi/full/10.1145/3699682.3728354

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

