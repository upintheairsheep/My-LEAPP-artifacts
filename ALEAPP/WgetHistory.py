import codecs
import csv
from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, is_platform_windows
def get_WgetHistory(files_found, report_folder, seeker, wrap_text):
    data_list = []
    file_found = str(files_found[0])
    counter = 1
    with codecs.open(file_found, 'r', 'utf-8-sig') as csvfile:
        for row in csvfile:
            data_list.append((counter, row))
            counter += 1
            
    if len(data_list) > 0:
        report = ArtifactHtmlReport('WGET History')
        report.start_artifact_report(report_folder, f'WGET History')
        report.add_script()
        data_headers = ('Order', 'Command')
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()
        
        tsvname = f'WGET History'
        tsv(report_folder, data_headers, data_list, tsvname)
        
    else:
        logfunc(f'No WGET History file available')
    
__artifacts__ = {
        "WGET History": (
                "WGET History",
                ('*/.wget-hsts'),
                get_WgetHistory)
}
