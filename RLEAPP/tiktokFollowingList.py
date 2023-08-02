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

def get_tikTokFollowing(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktokFollowingusername = ''
        tiktokFollowingdate = ''

        for site in data['Activity']:
            for site in data['Following List']:
                    for site in data['Following']:
                            tiktokFollowingusername = site['UserName']
                            tiktokFollowingdate = site['Date']
                
                            data_list.append((tiktokFollowingusername, tiktokFollowingdate))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Following')
            report.start_artifact_report(report_folder, 'TikTok Following')
            report.add_script()
            data_headers = ('Username', 'Date')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Following'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Following'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Following data available')

__artifacts__ = {
        "tikTokFollowing": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokFollowing)
}
