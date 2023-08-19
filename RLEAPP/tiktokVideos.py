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

def get_tikTokUploaded(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktokv_directurl = ''
        tiktokUploadeddate = ''
        tiktokUploadedLikes = ''


        for site in data['Video']:
            for site in data['Videos']:
                    for site in data['VideoList']:
                            tiktokUploadedusername = site['UserName']
                            tiktokUploadeddate = site['Date']
                
                            data_list.append((tiktokv_directurl, tiktokUploadeddate, tiktokUploadedLikes))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Uploaded Videos')
            report.start_artifact_report(report_folder, 'TikTok Uploaded Videos')
            report.add_script()
            data_headers = ('Direct URL', 'Date Uploaded', 'Like Count')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Uploaded Videos'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Uploaded Videos'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Uploaded Videos data available')

__artifacts__ = {
        "tikTokUploaded": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokUploaded)
}
