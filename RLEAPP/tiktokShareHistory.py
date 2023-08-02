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

def get_tikTokShareHistory(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktokShare_date = ''
        tiktokShare_type = ''
        tiktokShare_link = ''
        tiktokShare_method = ''

        for site in data['Activity']:
            for site in data['Share History']:
                    for site in data['ShareHistoryList']:
                            tiktokShare_date = site['Date']
                            tiktokShare_type = site['SharedContent']
                            tiktokShare_link = site['Link']
                            tiktokShare_method = site['Method']
                    
                
                            data_list.append((tiktokShare_date, tiktokShare_type, tiktokShare_link, tiktokShare_method))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Share History')
            report.start_artifact_report(report_folder, 'TikTok Share History')
            report.add_script()
            data_headers = ('Date', 'Content Type', 'URL', 'Method')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Share History'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Share History'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Share History data available')

__artifacts__ = {
        "tikTokShareHistory": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokShares)
}
