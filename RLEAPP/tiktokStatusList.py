# Module Description: Parses TikTok data from "Download My Data"
# Author: @upintheairsheep
# Date: 2023-08-05
# Artifact version: 0
# Requirements: none

import datetime
import json
import os

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows

def get_tikTokStatus(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktokStatus_1 = ''
        tiktokStatus_2 = ''
        tiktokStatus_3 = ''
        tiktokStatus_4 = ''
        tiktokStatus_5 = ''
        tiktokStatus_6 = ''
        tiktokStatus_7 = ''


        for site in data['Activity']:
            for site in data['Status']:
                    for site in data['Status List']:
                            tiktokStatus_1 = site['Resolution']
                            tiktokStatus_2 = site['App Version']
                            tiktokStatus_3 = site['IDFA']
                            tiktokStatus_4 = site['GAID']
                            tiktokStatus_5 = site['Android ID']
                            tiktokStatus_6 = site['IDFV']
                            tiktokStatus_7 = site['Web ID']
                    
                
                            data_list.append((tiktokStatus_1, tiktokStatus_2, tiktokStatus_3, tiktokStatus_4, tiktokStatus_5, tiktokStatus_6, tiktokStatus_7))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Status')
            report.start_artifact_report(report_folder, 'TikTok Status')
            report.add_script()
            data_headers = ('Screen Resolution', 'App Version', 'IDFA', 'GAID', 'Android ID', 'IDFV', 'Web ID')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Status'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Status'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Status data available')

__artifacts__ = {
        "tikTokStatus": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokStatus)
}
