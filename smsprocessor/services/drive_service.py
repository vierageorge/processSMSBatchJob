import logging
from datetime import datetime as dt
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

logger = logging.getLogger(__name__)
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.metadata']

class DriveService():
    def __init__(self, credentials_path):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scopes=SCOPES)
        self.service = build('drive', 'v3', credentials=credentials, cache_discovery=False)

    def get_file_list(self, folder_id):
        files_query = f"'{folder_id}' in parents"
        results = self.service.files().list(q = files_query, fields="files(id, name, fileExtension, mimeType)").execute()
        items = results.get('files', [])

        if not items:
            logger.info('No files found.')
        else:
            logger.info(f'Found {len(items)} files.')
        return items

    def get_file_content(self, file_id):
        result = self.service.files().get_media(fileId=file_id).execute()
        return result.decode('utf-8')

    def change_parent_directory(self, file_id, old_parent, new_parent_id):
        self.service.files().update(fileId=file_id, addParents=new_parent_id, removeParents=old_parent, fields='id, parents').execute()