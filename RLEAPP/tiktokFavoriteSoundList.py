# Module Description: Parses TikTok data from "Download My Data"
# Author: @upintheairsheep
# Date: 2023-08-01
# Artifact version: 0
# Requirements: none

import datetime
import json
import os

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows

def get_tikTokFavoriteSound(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktokfavsoundlink = ''
        tiktokfavsounddate = ''

        for site in data['Activity']:
            for site in data['Favorite Sounds']:
                    for site in data['FavoriteSoundList']:
                            tiktokfaveffectlink = site['Link']
                            tiktokfaveffectdate = site['Date']
                
                            data_list.append((tiktokfavsoundlink, tiktokfavsounddate))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Favorite Sounds')
            report.start_artifact_report(report_folder, 'TikTok Favorite Sounds')
            report.add_script()
            data_headers = ('Link', 'Date')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Favorite Sounds'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Favorite Sounds'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Favorite Sounds data available')

__artifacts__ = {
        "tikTokFavoriteSoundList": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokFavoriteSound)
}
