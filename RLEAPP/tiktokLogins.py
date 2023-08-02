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

def get_tikTokLogins(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'user_data.json': 
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []

        tiktoklogin_date = ''
        tiktoklogin_ip = ''
        tiktoklogin_hw = ''
        tiktoklogin_sw = ''
        tiktoklogin_net = ''
        tiktoklogin_car = ''

        for site in data['Activity']:
            for site in data['Login History']:
                    for site in data['LoginHistoryList']:
                            tiktoklogin_date = site['Date']
                            tiktoklogin_ip = site['IP']
                            tiktoklogin_hw = site['DeviceModel']
                            tiktoklogin_sw = site['DeviceSystem']
                            tiktoklogin_net = site['NetworkType']
                            tiktoklogin_car = site['Carrier']
                    
                
                            data_list.append((tiktoklogin_date, tiktoklogin_ip, tiktoklogin_hw, tiktoklogin_sw, tiktoklogin_net, tiktoklogin_car))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('TikTok Login History')
            report.start_artifact_report(report_folder, 'TikTok Login History')
            report.add_script()
            data_headers = ('Date', 'IP Adress', 'Device Model', 'Operating System', 'Network Type', 'Carrier')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()

            tsvname = f'TikTok Login History'
            tsv(report_folder, data_headers, data_list, tsvname)

            tlactivity = f'TikTok Login History'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No TikTok Login History data available')

__artifacts__ = {
        "tikTokLogins": (
            "TikTok Download Your Data Export",
            ('*/user_data.json'),
            get_tikTokLogins)
}
