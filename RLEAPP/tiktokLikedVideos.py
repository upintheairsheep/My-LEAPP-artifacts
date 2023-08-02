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

def get_tikTokLikedVideos(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        link_tt_lk = ''
        date_tt_lk = ''

        for site in data['Activity']:
            for site in data['Like List']:
                    for site in data['ItemFavoriteList']:
                            link_tt_lk = site['Link']
                            date_tt_lk = site['Date']
                
                            data_list.append((link_tt_lk, date_tt_lk))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Liked Videos')
            report.start_artifact_report(report_folder, 'TikTok Liked Videos')
            report.add_script()
            data_headers = ('Link', 'Date')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Liked Videos'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Liked Videos'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Liked Videos data available')

__artifacts__ = {
        "tikTokLikedVideos": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokLikedVideos)
}
