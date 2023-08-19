# Module Description: Parses TikTok data from "Download My Data"
# Author: @upintheairsheep
# Date: 2023-08-19
# Artifact version: 0
# Requirements: none

import datetime
import json
import os

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows

def get_tikTokBlocked(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktokBusername = ''
        tiktokBdate = ''

        for site in data['App Settings']:
            for site in data['Block']:
                    for site in data['BlockList']:
                            tiktokBlockedusername = site['UserName']
                            tiktokBlockeddate = site['Date']
                
                            data_list.append((tiktokBusername, tiktokBdate))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Blocked')
            report.start_artifact_report(report_folder, 'TikTok Blocked')
            report.add_script()
            data_headers = ('Username', 'Date')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Blocked'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Blocked'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Blocked data available')

__artifacts__ = {
        "tikTokBlocked": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokBlocked)
}
