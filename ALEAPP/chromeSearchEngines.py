# Module Description: Parses Google Chrome Search Engines from Takeout
# Author: @upintheairsheep
# Date: 2023-07-13
# Artifact version: 0.0.1-canary
# Requirements: none

import datetime
import json
import os

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows

def get_chromeSearchEngines(files_found, report_folder, seeker, wrap_text):
    
    for file_found in files_found:
        file_found = str(file_found)
        if not os.path.basename(file_found) == 'SearchEngines.json': # skip -journal and other files
            continue

        with open(file_found, encoding = 'utf-8', mode = 'r') as f:
            data = json.loads(f.read())
        data_list = []
        
        sEng_suggestions_url = ''
        sEng_favicon_url = ''
        sEng_safeAreplace = ''
        sEng_date = ''
        sEng_url = ''
        sEng_ntpurl = ''
        sEng_originUrl = ''
        sEng_syncGUID = ''
        sEng_shortName = ''
        sEng_kWord = ''
        sEng_inputEnc = ''
        sEng_prePopID = ''
        sEng_lastModified = ''




        for site in data['Search Extensions']:
            
            ext_name = site['name']
            ext_version = site['version']
            ext_ID = site['id']
            ext_enabled = site['enabled']
            incoginito_enabled = site['incognito_enabled']
            remote_install = site['remote_install']
               
            data_list.append((ext_name, ext_version, ext_ID, ext_enabled, incoginito_enabled, remote_install))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('Chrome Search Engines')
            report.start_artifact_report(report_folder, 'Chrome Search Engines')
            report.add_script()
            data_headers = ('Name','Version','ID','Enabled','Incognito Enabled','Remote Install')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()
            
            tsvname = f'Chrome Search Engines'
            tsv(report_folder, data_headers, data_list, tsvname)
            
            tlactivity = f'Chrome Search Engines'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No Chrome Search Engines data available')

__artifacts__ = {
        "chromeSearchEngines": (
            "Google Takeout Archive",
            ('*/Chrome/SearchEngines.json'),
            get_chromeExtensions)
}
