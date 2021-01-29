import logging
from datetime import datetime as dt
from googleapiclient.discovery import build

#TODO: Change this into a class.

logger = logging.getLogger(__name__)

def get_file_list(creds, folder_id):
    files_query = f"'{folder_id}' in parents"
    drive_service = build('drive', 'v3', credentials=creds, cache_discovery=False)

    results = drive_service.files().list(q = files_query, fields="files(id, name, fileExtension, mimeType)").execute()
    items = results.get('files', [])

    if not items:
        logger.info('No files found.')
    else:
        logger.info(f'Found {len(items)} files.')
    return items

def get_file_content(creds, file_id):
    drive_service = build('drive', 'v3', credentials=creds, cache_discovery=False)
    result = drive_service.files().get_media(fileId=file_id).execute()
    return result.decode('utf-8')

def change_parent_directory(creds, file_id, old_parent, new_parent_id):
    drive_service = build('drive', 'v3', credentials=creds, cache_discovery=False)
    drive_service.files().update(fileId=file_id, addParents=new_parent_id, removeParents=old_parent, fields='id, parents').execute()