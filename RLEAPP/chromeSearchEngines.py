# Module Description: Parses Google Chrome Search Engines from Takeout
# Author: @upintheairsheep
# Date: 2023-07-13
# Artifact version: 0.0.0
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
        sEng_imageurlpostparams = ''
        sEng_isActive = ''
        sEng_imageurl = ''
        sEng_starterpackID = ''





        for site in data['Search Extensions']:
            
            sEng_suggestions_url = site['suggestions_url']
            sEng_favicon_url = site['favicon_url']
            sEng_safeAreplace = site['safe_for_autoreplace']
            sEng_date = site['date_created']
            sEng_url = site['url']
            sEng_ntpurl = site['new_tab_url']
            sEng_originUrl = site['originating_url']
            sEng_syncGUID = site['sync_guid']
            sEng_shortName = site['short_name']
            sEng_kWord = site['keyword']
            sEng_inputEnc = site['input_encodings']
            sEng_prePopID = site['prepopulate_id']
            sEng_lastModified = site['last_modified']
            sEng_imageurlpostparams = site['image_url_post_params']
            sEng_isActive = site['is_active']
            sEng_imageurl = site['image_url']
            sEng_starterpackID = site['starter_pack_id']
               
            data_list.append((sEng_shortName, sEng_kWord, sEng_date, sEng_lastModified, url, sEng_originUrl, sEng_syncGUID, sEng_favicon_url, sEng_suggestions_url, sEng_ntpurl, sEng_inputEnc, sEng_safeAreplace, sEng_prePopID, sEng_imageurlpostparams, sEng_isActive, sEng_imageurl, sEng_starterpackID))

        num_entries = len(data_list)
        if num_entries > 0:
            report = ArtifactHtmlReport('Chrome Search Engines')
            report.start_artifact_report(report_folder, 'Chrome Search Engines')
            report.add_script()
            data_headers = ('(Short) Name','Keyword','Date Created','Last Modified','URL Syntax','API URL', 'Sync GUID', 'Favicon URL', 'Suggestions URL', 'New Tab URL', 'Input Encodings', 'Safe Autoreplace?', 'Pre-populate ID', 'Image URL Post Parameters', 'Is Active?', 'Image URL', 'Starter Pack ID')

            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()
            
            tsvname = f'Chrome Search Engines'
            tsv(report_folder, data_headers, data_list, tsvname)
            
            tlactivity = f'Chrome Search Engines'
            timeline(report_folder, tlactivity, data_list, data_headers)
        else:
            logfunc('No Chrome Search Engines data available')
'''
Example data
{
    "Search Engines": [
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "date_created": 13170824505584527,
            "url": "http://translate.google.com/?source=osdd#auto|auto|{searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://translate.google.com/opensearch.xml?hl=en",
            "sync_guid": "ab0f078f-2f1c-42de-9553-e2f6f21718ae",
            "short_name": "Google Translate",
            "keyword": "translate.google.com",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170824505584527
},
        {
            "suggestions_url": "",
            "favicon_url": "https://ssl.gstatic.com/chat/startpage/favicon_f1bac5c7ba3154b58080de921eb6d5ea.ico",
            "safe_for_autoreplace": false,
            "date_created": 13181615702117751,
            "url": "https://hangouts.google.com/?hl=en&ht=0&hcb=0&lm1=1537142037498&hs=84&hmv=1&ssc=WyIiLDAsbnVsbCxudWxsLG51bGwsW10sbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLDg0LG51bGwsbnVsbCxudWxsLFsxNTM3MTQyMDM3NDk4XSxudWxsLG51bGwsW1tudWxsLG51bGwsW251bGwsIisxODg4NjkwNTM0NiJdXV0sbnVsbCxudWxsLHRydWUsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsW10sW10sbnVsbCxudWxsLG51bGwsW10sbnVsbCxudWxsLG51bGwsW10sbnVsbCxudWxsLFtdXQ..&action=chat&pn=%2B{searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "902232b9-3ab4-4a30-8ab0-2c6c519596bc",
            "short_name": "call",
            "keyword": "call",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13181615702117751
},
        {
            "suggestions_url": "",
            "favicon_url": "https://bingobaker.com/media/favicon.ae3c97b647e1.ico",
            "safe_for_autoreplace": true,
            "date_created": 13190949198277828,
            "url": "https://bingobaker.com/search?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "e27587db-26b7-47b2-9a1c-2cc974a90d9d",
            "short_name": "bingobaker.com",
            "keyword": "bingobaker.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13190949198277829
},
        {
            "suggestions_url": "https://it.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://it.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770744823824,
            "url": "https://it.wikipedia.org/w/index.php?title=Speciale:Ricerca&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://it.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "3c304939-a4d0-4f62-8aab-600b93e715fb",
            "short_name": "Wikipedia (it)",
            "keyword": "it.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770744823824
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_TRUE",
            "date_created": 13327018826763456,
            "starter_pack_id": 3,
            "url": "chrome://tabs/?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "ec205736-edd7-4022-a9a3-b431fc000003",
            "short_name": "Tabs",
            "keyword": "@tabs",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13327018826763456
},
        {
            "suggestions_url": "https://zh.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://zh.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770791906405,
            "url": "https://zh.wikipedia.org/w/index.php?title=Special:%E6%90%9C%E7%B4%A2&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://zh.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "1940f062-8f13-40f3-a52a-1b2c88a868a5",
            "short_name": "Wikipedia (zh)",
            "keyword": "zh.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770791906405
},
        {
            "suggestions_url": "https://grimoireoss-pa.clients6.google.com/suggest?q={searchTerms}&key=AIzaSyD1ZDuAdU_IZqa3Wscr053WydRT7FoJdmQ",
            "favicon_url": "https://www.gstatic.com/devopsconsole/images/oss/favicons/oss-32x32.png",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13329707187842025,
            "starter_pack_id": 0,
            "url": "https://cs.android.com/search?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://cs.android.com/xml/opensearch.xml",
            "sync_guid": "d7e26919-6a4d-4ea8-a188-bf2e5a5f5160",
            "short_name": "Code search",
            "keyword": "cs.android.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13329707187842025
},
        {
            "suggestions_url": "https://de.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://de.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770776084577,
            "url": "https://de.wikipedia.org/w/index.php?title=Spezial:Suche&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://de.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "e7465039-e7e9-4dfa-9895-4f8391a3281c",
            "short_name": "Wikipedia (de)",
            "keyword": "de.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770776084577
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": false,
            "date_created": 13181615566854727,
            "url": "mailto:{searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "298b8585-9dbb-422d-9b0b-ce14b2210e95",
            "short_name": "Email",
            "keyword": "email",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13181615566854727
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_TRUE",
            "date_created": 13327018826763423,
            "starter_pack_id": 1,
            "url": "chrome://bookmarks/?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "ec205736-edd7-4022-a9a3-b431fc000001",
            "short_name": "Bookmarks",
            "keyword": "@bookmarks",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13327018826763424
},
        {
            "suggestions_url": "https://wiki.archiveteam.org/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://wiki.archiveteam.org/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13330815546414565,
            "starter_pack_id": 0,
            "url": "https://wiki.archiveteam.org/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://wiki.archiveteam.org/opensearch_desc.php",
            "sync_guid": "151ac8c6-e1dc-4a5b-9c48-36bc1a8d7f0e",
            "short_name": "Archiveteam (en)",
            "keyword": "archiveteam.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13330815546414565
},
        {
            "suggestions_url": "https://wiki.archiveteam.org/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://wiki.archiveteam.org/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13333755812207338,
            "starter_pack_id": 0,
            "url": "https://wiki.archiveteam.org/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://wiki.archiveteam.org/opensearch_desc.php",
            "sync_guid": "fd517e94-3938-456c-9597-ca951405c6b3",
            "short_name": "Archiveteam (en)",
            "keyword": "wiki.archiveteam.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13333755812207339
},
        {
            "suggestions_url": "",
            "favicon_url": "https://github.githubassets.com/favicons/favicon.svg",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13297647847405868,
            "starter_pack_id": 0,
            "url": "https://github.com/search?q={searchTerms}&ref=opensearch",
            "new_tab_url": "",
            "originating_url": "https://github.com/opensearch.xml",
            "sync_guid": "b729411c-7ff3-4f9b-bbe3-0b6efba87d16",
            "short_name": "GitHub",
            "keyword": "github.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13297647847405868
},
        {
            "suggestions_url": "https://es.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=100|104|0",
            "favicon_url": "https://es.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770711796150,
            "url": "https://es.wikipedia.org/w/index.php?title=Especial:Buscar&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://es.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "7fb3ce09-0dbd-4364-9e6d-2a4c6bc09f09",
            "short_name": "Wikipedia (es)",
            "keyword": "es.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770711796150
},
        {
            "suggestions_url": "{google:baseSuggestURL}search?{google:searchFieldtrialParameter}client={google:suggestClient}&gs_ri={google:suggestRid}&xssi=t&q={searchTerms}&{google:inputType}{google:omniboxFocusType}{google:cursorPosition}{google:currentPageUrl}{google:pageClassification}{google:clientCacheTimeToLive}{google:searchVersion}{google:sessionToken}{google:prefetchQuery}sugkey={google:suggestAPIKeyParameter}",
            "image_url_post_params": "encoded_image={google:imageThumbnail},image_url={google:imageURL},sbisrc={google:imageSearchSource},original_width={google:imageOriginalWidth},original_height={google:imageOriginalHeight},processed_image_dimensions={google:processedImageDimensions}",
            "favicon_url": "https://www.google.com/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 0,
            "image_url": "{google:baseSearchByImageURL}upload",
            "starter_pack_id": 0,
            "url": "{google:baseURL}search?q={searchTerms}&{google:RLZ}{google:originalQueryForSuggestion}{google:assistedQueryStats}{google:searchFieldtrialParameter}{google:iOSSearchLanguage}{google:prefetchSource}{google:searchClient}{google:sourceId}{google:contextualSearchVersion}ie={inputEncoding}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "607460af-3651-4cc4-a3b6-ebd4d620f44e",
            "short_name": "Google",
            "keyword": "google.com",
            "input_encodings": "UTF-8",
            "alternate_urls": [
                        "{google:baseURL}#q={searchTerms}",
                        "{google:baseURL}search#q={searchTerms}",
                        "{google:baseURL}webhp#q={searchTerms}",
                        "{google:baseURL}s#q={searchTerms}",
                        "{google:baseURL}s?q={searchTerms}"
            ],
            "prepopulate_id": 1,
            "last_modified": 0
},
        {
            "suggestions_url": "",
            "favicon_url": "https://www.checkiday.com/apple-touch-icon.png",
            "safe_for_autoreplace": true,
            "date_created": 13180470725575722,
            "url": "https://www.checkiday.com/search.php?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "24e2b565-faf5-4e25-aadd-de313376a21b",
            "short_name": "checkiday.com",
            "keyword": "checkiday.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13180470725575723
},
        {
            "suggestions_url": "",
            "favicon_url": "https://cloud.google.com/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170385767597369,
            "url": "https://cloud.google.com/s/results?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://cloud.google.com/s/opensearch.xml",
            "sync_guid": "b1194b3f-a765-47c6-b8cd-d14767d6a612",
            "short_name": "Google Cloud",
            "keyword": "cloud.google.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13170385767597369
},
        {
            "suggestions_url": "https://ja.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://ja.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770765339980,
            "url": "https://ja.wikipedia.org/w/index.php?title=%E7%89%B9%E5%88%A5:%E6%A4%9C%E7%B4%A2&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://ja.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "e03803cf-0724-4aa4-9ac9-0f0dffe4bbf4",
            "short_name": "Wikipedia (ja)",
            "keyword": "ja.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770765339980
},
        {
            "suggestions_url": "http://www.Exploitee.rs/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://www.exploitee.rs/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13329447073705993,
            "starter_pack_id": 0,
            "url": "http://www.Exploitee.rs/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://exploitee.rs/opensearch_desc.php",
            "sync_guid": "bbff2351-dac5-42ed-80b6-5b5f75a61bb1",
            "short_name": "Exploitee.rs (en)",
            "keyword": "exploitee.rs",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13329447073705993
},
        {
            "suggestions_url": "",
            "favicon_url": "http://archive.fo/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13193039991813142,
            "url": "http://archive.fo/search/?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "http://archive.fo/opensearchdescription.xml",
            "sync_guid": "4c4a5bfa-60ed-4822-bf8c-505a2c3b4495",
            "short_name": "Archive.is",
            "keyword": "archive.today",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13193039991813143
},
        {
            "suggestions_url": "https://en.wikiquote.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://en.wikiquote.org/static/favicon/wikiquote.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170823599476783,
            "url": "https://en.wikiquote.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://en.wikiquote.org/w/opensearch_desc.php",
            "sync_guid": "7a580294-1d38-4daf-a7ed-bc8d913b5683",
            "short_name": "Wikiquote (en)",
            "keyword": "en.wikiquote.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170823599476784
},
        {
            "suggestions_url": "",
            "favicon_url": "https://bitbucket.org/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13187426267321638,
            "url": "https://bitbucket.org/repo/all/?name={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://bitbucket.org/opensearch.xml",
            "sync_guid": "87a1209f-5e1d-4721-bd04-e70ace909b0e",
            "short_name": "Bitbucket",
            "keyword": "websplat.bitbucket.org",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13187426267321638
},
        {
            "suggestions_url": "",
            "favicon_url": "https://static1.teacherspayteachers.com/tpt-frontend/releases/production/current/fbf2fa4d283a37a435dde24f48537e7d.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770654429371,
            "url": "https://www.teacherspayteachers.com/Browse/Search:{searchTerms}?ref=opensearch",
            "new_tab_url": "",
            "originating_url": "https://www.teacherspayteachers.com/search-site.xml",
            "sync_guid": "31a088fe-1a14-4b84-b601-41a4c0535cf1",
            "short_name": "Teachers Pay Teachers",
            "keyword": "teacherspayteachers.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13178770654429371
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "date_created": 13177576331806682,
            "url": "https://gaming.youtube.com/results?search_query={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://gaming.youtube.com/opensearch?locale=en_US",
            "sync_guid": "fc0419d8-9f3e-4145-9bcd-5235a8e9f66b",
            "short_name": "YouTube Gaming",
            "keyword": "gaming.youtube.com",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13177576331806682
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_TRUE",
            "date_created": 13327018826763445,
            "starter_pack_id": 2,
            "url": "chrome://history/?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "ec205736-edd7-4022-a9a3-b431fc000002",
            "short_name": "History",
            "keyword": "@history",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13327018826763445
},
        {
            "suggestions_url": "https://commons.wikimedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=6|12|14|100|106|0",
            "favicon_url": "https://commons.wikimedia.org/static/favicon/commons.ico",
            "safe_for_autoreplace": true,
            "date_created": 13180399962685993,
            "url": "https://commons.wikimedia.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://commons.wikimedia.org/w/opensearch_desc.php",
            "sync_guid": "6b6153d6-7e8f-4931-ac74-93fae51a714c",
            "short_name": "Wikimedia Commons",
            "keyword": "upload.wikimedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13180399962685993
},
        {
            "suggestions_url": "https://species.wikimedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://species.wikimedia.org/static/favicon/wikispecies.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170823674698518,
            "url": "https://species.wikimedia.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://species.wikimedia.org/w/opensearch_desc.php",
            "sync_guid": "763dc2e8-58d6-4fc4-9822-470db88ffd3c",
            "short_name": "Wikispecies (en)",
            "keyword": "species.wikimedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170823674698518
},
        {
            "suggestions_url": "https://en.wikibooks.org/w/api.php?action=opensearch&search={searchTerms}&namespace=4|102|110|112|0",
            "favicon_url": "https://en.wikibooks.org/static/favicon/wikibooks.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170823609454309,
            "url": "https://en.wikibooks.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://en.wikibooks.org/w/opensearch_desc.php",
            "sync_guid": "8c8fd477-428f-4a40-ab95-e1369bf633a1",
            "short_name": "Wikibooks (en)",
            "keyword": "en.wikibooks.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170823609454309
},
        {
            "suggestions_url": "https://www.facebook.com/search/opensearch/suggestions/?q={searchTerms}",
            "favicon_url": "https://www.facebook.com/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170362223096346,
            "url": "https://www.facebook.com/search/top/?q={searchTerms}&opensearch=1",
            "new_tab_url": "",
            "originating_url": "https://www.facebook.com/osd.xml",
            "sync_guid": "90636aac-00d9-48cb-af2a-5e81dc3dd39b",
            "short_name": "Facebook",
            "keyword": "facebook.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13170362223096346
},
        {
            "suggestions_url": "https://en.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://en.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178647337478473,
            "url": "https://en.wikipedia.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://en.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "d5d83ee7-c507-4191-9fd7-ccc8aee9b248",
            "short_name": "Wikipedia (en)",
            "keyword": "en.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178647337478473
},
        {
            "suggestions_url": "",
            "favicon_url": "https://store.steampowered.com/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178762697933071,
            "url": "https://store.steampowered.com/search/?snr=1_4_4__12&term={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "afe93368-7e50-4361-9e02-529c449d1a6d",
            "short_name": "store.steampowered.com",
            "keyword": "store.steampowered.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13178762697933071
},
        {
            "suggestions_url": "",
            "favicon_url": "https://abs.twimg.com/favicons/twitter.2.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13178771000709882,
            "starter_pack_id": 0,
            "url": "https://twitter.com/search?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://twitter.com/opensearch.xml",
            "sync_guid": "362d553c-8d27-4405-b3cc-50b3b50db836",
            "short_name": "Twitter",
            "keyword": "twitter.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13178771000709882
},
        {
            "suggestions_url": "https://pt.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://pt.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770751480968,
            "url": "https://pt.wikipedia.org/w/index.php?title=Especial:Pesquisar&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://pt.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "fb017ee9-519c-42b7-920c-e8cc253f9095",
            "short_name": "Wikipédia (pt)",
            "keyword": "pt.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770751480968
},
        {
            "suggestions_url": "https://fr.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://fr.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770781953750,
            "url": "https://fr.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Recherche&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://fr.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "7200ab91-2362-4d9a-8ca0-d07a7f58ab75",
            "short_name": "Wikipédia (fr)",
            "keyword": "fr.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770781953750
},
        {
            "suggestions_url": "",
            "favicon_url": "https://www.youtube.com/s/desktop/afaf5292/img/favicon_32x32.png",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13164333127000000,
            "starter_pack_id": 0,
            "url": "https://www.youtube.com/results?search_query={searchTerms}&page={startPage?}&utm_source=opensearch",
            "new_tab_url": "",
            "originating_url": "https://www.youtube.com/opensearch?locale=en_US",
            "sync_guid": "8c3c50d1-25c4-44a2-9e1e-2b24c5f29a79",
            "short_name": "YouTube Video Search",
            "keyword": "youtube.com",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13164333127000000
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "date_created": 13170302769239547,
            "url": "https://drive.google.com/drive/search?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://drive.google.com/opensearch.xml",
            "sync_guid": "6ab8b0b7-4604-463c-b81c-285757650413",
            "short_name": "Google Drive",
            "keyword": "drive.google.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13170302769239547
},
        {
            "suggestions_url": "https://ru.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://ru.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770738674084,
            "url": "https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://ru.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "ded386b4-9e2b-4c92-8dc5-ef55e2402113",
            "short_name": "Википедия (ru)",
            "keyword": "ru.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770738674084
},
        {
            "suggestions_url": "https://commons.wikimedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=6|12|14|100|106|0",
            "favicon_url": "https://commons.wikimedia.org/static/favicon/commons.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170823646309114,
            "url": "https://commons.wikimedia.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://commons.wikimedia.org/w/opensearch_desc.php",
            "sync_guid": "e735b4c5-2abb-4b98-97b3-e3630c73d946",
            "short_name": "Wikimedia Commons",
            "keyword": "commons.wikimedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170823646309114
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": false,
            "date_created": 13179700630866008,
            "url": "http://{searchTerms}.com",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "13edc6b2-0b9a-4282-836f-8ea32f1d2d7c",
            "short_name": "Quick Launch",
            "keyword": "ql",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13179700630866008
},
        {
            "suggestions_url": "https://pl.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://pl.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "date_created": 13178770796819486,
            "url": "https://pl.wikipedia.org/w/index.php?title=Specjalna:Szukaj&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://pl.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "b19bc46f-338b-4373-97f4-0b01eb33cf14",
            "short_name": "Wikipedia (pl)",
            "keyword": "pl.wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13178770796819487
},
        {
            "suggestions_url": "",
            "favicon_url": "https://blog.archive.org/wp-content/uploads/2023/03/ia-logo-sq-150x150.png",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13332637778815259,
            "starter_pack_id": 0,
            "url": "https://blog.archive.org/?s={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "a9174d92-0f96-4812-96f8-508055b03a1c",
            "short_name": "blog.archive.org",
            "keyword": "blog.archive.org",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13332637778815259
},
        {
            "suggestions_url": "https://en.wikipedia.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://en.wikipedia.org/static/favicon/wikipedia.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13209450774645235,
            "starter_pack_id": 0,
            "url": "https://en.wikipedia.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://en.wikipedia.org/w/opensearch_desc.php",
            "sync_guid": "fb0202c9-c336-45f3-8817-d66ccf7ce62b",
            "short_name": "Wikipedia (en)",
            "keyword": "wikipedia.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13209450774645235
},
        {
            "suggestions_url": "https://en.wikivoyage.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://en.wikivoyage.org/static/favicon/wikivoyage.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170823618864028,
            "url": "https://en.wikivoyage.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://en.wikivoyage.org/w/opensearch_desc.php",
            "sync_guid": "ef5c4f60-a94c-481b-b335-0e725dbc1dd3",
            "short_name": "Wikivoyage (en)",
            "keyword": "en.wikivoyage.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170823618864028
},
        {
            "suggestions_url": "",
            "favicon_url": "https://emojipedia.org/static/img/favicons/favicon-32x32.png",
            "safe_for_autoreplace": true,
            "date_created": 13180849640699494,
            "url": "https://emojipedia.org/search/?q={searchTerms}&utm_source=opensearch",
            "new_tab_url": "",
            "originating_url": "https://emojipedia.org/opensearch.osd",
            "sync_guid": "10abef37-7a06-4e25-ae1c-61a6d91cdbd1",
            "short_name": "Emojipedia",
            "keyword": "emojipedia.org",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13180849640699494
},
        {
            "suggestions_url": "https://en.wiktionary.org/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://en.wiktionary.org/static/favicon/wiktionary/en.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13170823634972182,
            "starter_pack_id": 0,
            "url": "https://en.wiktionary.org/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://en.wiktionary.org/w/opensearch_desc.php",
            "sync_guid": "9f40f05f-1fe2-4130-9199-3b4ca0135697",
            "short_name": "Wiktionary (en)",
            "keyword": "en.wiktionary.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170823634972182
},
        {
            "suggestions_url": "https://www.bing.com/osjson.aspx?query={searchTerms}&language={language}&PC=U316",
            "image_url_post_params": "imageBin={google:imageThumbnailBase64}",
            "favicon_url": "https://www.bing.com/sa/simg/bing_p_rr_teal_min.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 0,
            "image_url": "https://www.bing.com/images/detail/search?iss=sbiupload&FORM=CHROMI#enterInsights",
            "starter_pack_id": 0,
            "url": "https://www.bing.com/search?q={searchTerms}&PC=U316&FORM=CHROMN",
            "new_tab_url": "https://www.bing.com/chrome/newtab",
            "originating_url": "",
            "sync_guid": "93fd9976-b4df-442b-acf5-6236335992c1",
            "short_name": "Bing",
            "keyword": "bing.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 3,
            "last_modified": 13331590986907174
},
        {
            "suggestions_url": "https://www.facebook.com/search/opensearch/suggestions/?q={searchTerms}",
            "favicon_url": "https://www.facebook.com/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13184912745490489,
            "url": "https://www.facebook.com/search/top/?q={searchTerms}&opensearch=1",
            "new_tab_url": "",
            "originating_url": "https://www.facebook.com/osd.xml",
            "sync_guid": "6cc1ad8d-27ee-4dc1-8dd1-4f80ff8bf163",
            "short_name": "Facebook",
            "keyword": "acebook.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13184912745490489
},
        {
            "suggestions_url": "",
            "favicon_url": "http://download.cnet.com/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13180907287027902,
            "url": "http://download.cnet.com/1770-20_4-0-{startPage?}.html?query={searchTerms}&searchtype=downloads&tag=opensearch",
            "new_tab_url": "",
            "originating_url": "https://download.cnet.com/html/osdd/download.xml",
            "sync_guid": "79cb5f0e-4ca5-48c5-8759-cbb2b469558a",
            "short_name": "CNET Download",
            "keyword": "download.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13180907287027903
},
        {
            "suggestions_url": "",
            "favicon_url": "https://ca.ixl.com/ixl-favicon.png",
            "safe_for_autoreplace": true,
            "date_created": 13178770597152611,
            "url": "https://ca.ixl.com/search?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "c787ec0b-ace7-46fc-8dc6-e29025915d21",
            "short_name": "ixl.com",
            "keyword": "ixl.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13178770597152611
},
        {
            "suggestions_url": "https://search.yahoo.com/sugg/chrome?output=fxjson&appid=crmas_sfp&command={searchTerms}",
            "favicon_url": "https://search.yahoo.com/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 0,
            "starter_pack_id": 0,
            "url": "https://search.yahoo.com/search{google:pathWildcard}?ei={inputEncoding}&fr=crmas_sfp&p={searchTerms}",
            "new_tab_url": "https://search.yahoo.com?fr=crmas_sfp",
            "originating_url": "",
            "sync_guid": "fcb387e4-2eab-4acc-97e2-7612bd8dd8a8",
            "short_name": "Yahoo!",
            "keyword": "yahoo.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 2,
            "last_modified": 13331590986907179
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "date_created": 13177714639225660,
            "url": "https://www.google.com/maps/search/{searchTerms}?hl=en&source=opensearch",
            "new_tab_url": "",
            "originating_url": "https://www.google.com/maps/preview/opensearch.xml?hl=en",
            "sync_guid": "b5242dff-d649-4d41-88d0-8cca3a70a281",
            "short_name": "Google Maps",
            "keyword": "maps.google.com",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13177714639225661
},
        {
            "suggestions_url": "https://www.theiphonewiki.com/w/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "https://www.theiphonewiki.com/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13333004474663325,
            "starter_pack_id": 0,
            "url": "https://www.theiphonewiki.com/w/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://www.theiphonewiki.com/w/opensearch_desc.php",
            "sync_guid": "4febfec9-4170-4457-bcb2-7f33e62435e8",
            "short_name": "The iPhone Wiki (en)",
            "keyword": "theiphonewiki.com",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13333004474663325
},
        {
            "suggestions_url": "http://fileformats.archiveteam.org/api.php?action=opensearch&search={searchTerms}&namespace=0",
            "favicon_url": "http://fileformats.archiveteam.org/favicon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13331600423752243,
            "starter_pack_id": 0,
            "url": "http://fileformats.archiveteam.org/index.php?title=Special:Search&search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "http://fileformats.archiveteam.org/opensearch_desc.php",
            "sync_guid": "b78f6ade-ee89-4ba6-ae52-57cc10cc70f8",
            "short_name": "Just Solve the File Format Problem (en)",
            "keyword": "fileformats.archiveteam.org",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13331600423752243
},
        {
            "suggestions_url": "",
            "favicon_url": "https://i.deviantart.net/icons/da_favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13187583133639023,
            "url": "https://www.deviantart.com/popular-all-time/?section=&global=1&q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "f05fd90b-75e8-4395-829e-bdf383b6e24a",
            "short_name": "deviantart.com",
            "keyword": "deviantart.com",
            "input_encodings": "windows-1252",
            "prepopulate_id": 0,
            "last_modified": 13187583133639023
},
        {
            "suggestions_url": "https://grimoireoss-pa.clients6.google.com/suggest?q={searchTerms}&key=AIzaSyCqPSptx9mClE5NU4cpfzr6cgdO_phV1lM",
            "favicon_url": "https://www.gstatic.com/devopsconsole/images/oss/favicons/oss-32x32.png",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13332651899836903,
            "starter_pack_id": 0,
            "url": "https://source.chromium.org/search?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://source.chromium.org/xml/opensearch.xml",
            "sync_guid": "a6ce508a-aeb7-4552-a342-800bf4775c3d",
            "short_name": "Code search",
            "keyword": "codesearch.chromium.org",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13332651899836903
},
        {
            "suggestions_url": "",
            "favicon_url": "https://www.ziprecruiter.com/favicon.ico",
            "safe_for_autoreplace": true,
            "date_created": 13170890037250963,
            "url": "https://www.ziprecruiter.com/candidate/search?search={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://www.ziprecruiter.com/opensearchdescription.xml",
            "sync_guid": "f5135f0c-f863-46b1-bb72-0e74f7d31654",
            "short_name": "ZipRecruiter",
            "keyword": "ziprecruiter.com",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13170890037250964
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": false,
            "date_created": 13179700745577645,
            "url": "http://google.com/{google:unescapedSearchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "cca1ba6e-4bb4-4ca6-b380-2a6a0f59f186",
            "short_name": "Google Quick Launch",
            "keyword": "gql",
            "input_encodings": "",
            "prepopulate_id": 0,
            "last_modified": 13179700782482846
},
        {
            "suggestions_url": "http://ytcomment.kmcat.uk/q={searchTerms}",
            "favicon_url": "https://img-cdn.kmcat.uk/ytcommenticons/icon.ico",
            "safe_for_autoreplace": true,
            "is_active": "ACTIVE_STATUS_UNSPECIFIED",
            "date_created": 13329896092743022,
            "starter_pack_id": 0,
            "url": "http://ytcomment.kmcat.uk/q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "https://ytcomment.kmcat.uk/opensearch.xml",
            "sync_guid": "3505b5a3-8674-4fd9-ba81-422f7ff3c987",
            "short_name": "YTComment",
            "keyword": "ytcomment.kmcat.uk",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13329896092743022
},
        {
            "suggestions_url": "",
            "favicon_url": "",
            "safe_for_autoreplace": true,
            "date_created": 13169249121765964,
            "url": "http://www.secutracengineering.com/index.php?option=com_search&searchword={searchTerms}",
            "new_tab_url": "",
            "originating_url": "http://www.secutracengineering.com/component/search/?format=opensearch",
            "sync_guid": "ce66040f-dc45-48d0-a5a7-151c3beb991a",
            "short_name": "Secutrac Engineering",
            "keyword": "secutracengineering.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13169249121765964
},
        {
            "suggestions_url": "",
            "favicon_url": "https://www.nav-goo.com/images/favicon.png",
            "safe_for_autoreplace": true,
            "date_created": 13184559320102683,
            "url": "https://www.nav-goo.com/web?q={searchTerms}",
            "new_tab_url": "",
            "originating_url": "",
            "sync_guid": "a82b873c-9d8b-4195-ace2-d2fefbc27231",
            "short_name": "nav-goo.com",
            "keyword": "nav-goo.com",
            "input_encodings": "UTF-8",
            "prepopulate_id": 0,
            "last_modified": 13184559320102683
}
    ]
}
'''
__artifacts__ = {
        "chromeSearchEngines": (
            "Google Takeout Archive",
            ('*/Chrome/SearchEngines.json'),
            get_chromeExtensions)
}
