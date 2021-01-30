from smsprocessor.constants import VALID_EXTENSIONS, VALID_MIME_TYPE
from smsprocessor.config import SOURCE_FOLDER_ID, PROCESSED_FOLDER_ID
from .exceptions import NotValidExtension, NotValidMimeType
from smsprocessor.services import google_drive_service as gds
from dateutil.parser import parse


def process_file(creds, file, appender):
    file_name = file['name']
    if file['fileExtension'] not in VALID_EXTENSIONS:
        raise NotValidExtension(file_name)
    if file['mimeType'] not in VALID_MIME_TYPE:
        raise NotValidMimeType(file_name)

    (sender, timestamp_s, message) = gds.get_file_content(creds, file['id']).split('|')
    date_s = f'{file_name[0:4]}/{file_name[4:6]}/{file_name[6:8]}'
    date = parse(date_s, fuzzy=False)
    appender.append_to_sheet(date_s, message)
    gds.change_parent_directory(creds, file['id'], SOURCE_FOLDER_ID, PROCESSED_FOLDER_ID)