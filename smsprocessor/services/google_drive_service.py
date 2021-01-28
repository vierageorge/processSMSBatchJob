import logging
from datetime import datetime as dt
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

def get_file_list(creds, folder_id):
    files_query = f"'{folder_id}' in parents"
    drive_service = build('drive', 'v3', credentials=creds, cache_discovery=False)

    results = drive_service.files().list(q = files_query, fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        logger.info('No files found.')
    else:
        logger.info(f'Found {len(items)} files.')
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    return items