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

def get_tikTokFavoriteVideos(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        link_tt_fv = ''
        date_tt_fv = ''

        for site in data['Activity']:
            for site in data['Favorite Videos']:
                    for site in data['FavoriteVideoList']:
                            link_tt_fv = site['Link']
                            date_tt_fv = site['Date']
                
                            data_list.append((link_tt_fv, date_tt_fv))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Favorite Videos')
            report.start_artifact_report(report_folder, 'TikTok Favorite Videos')
            report.add_script()
            data_headers = ('Link', 'Date')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Favorite Videos'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Favorite Videos'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Favorite Videos data available')

__artifacts__ = {
        "tikTokFavoriteVideos": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokFavoriteVideos)
}
