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

def get_tikTokHashtags(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        hashtagname = ''
        hashtaglink = ''

        for site in data['Activity']:
            for site in data['Hashtag']:
                    for site in data['HashtagList']:
                            hashtagname = site['HashtagName']
                            hashtaglink = site['HashtagLink']
                
                            data_list.append((hashtagname, hashtaglink))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Hashtags Used')
            report.start_artifact_report(report_folder, 'TikTok Hashtags Used')
            report.add_script()
            data_headers = ('Hashtag Name', 'URL')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Hashtags Used'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Hashtags Used'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Hashtags data available')

__artifacts__ = {
        "tikTokHashtags": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokHashtags)
}
