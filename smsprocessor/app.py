import logging
from .config import SOURCE_FOLDER_ID
from .constants import VALID_EXTENSIONS, VALID_MIME_TYPE
from smsprocessor.common.exceptions import NotValidExtension, NotValidMimeType
from smsprocessor.services import (
    google_auth_service as gas,
    google_drive_service as gds
    )

logger = logging.getLogger(__name__)

def process_file(creds, file):
    file_name = file['name']
    if file['fileExtension'] not in VALID_EXTENSIONS:
        raise NotValidExtension(file_name)
    if file['mimeType'] not in VALID_MIME_TYPE:
        raise NotValidMimeType(file_name)
    print(f"{file_name} -> {gds.get_file_content(creds, file['id'])}")

def run():
    logger.info("STARTING APPLICATION")
    creds = gas.get_credentials()
    file_list = gds.get_file_list(creds, SOURCE_FOLDER_ID)
    for file in file_list:
        try:
            process_file(creds, file)
        except (NotValidExtension, NotValidMimeType) as e:
            logger.warn(e)
        except UnicodeDecodeError as e:
            logger.error(f"{file['name']} :: {e}")
    logger.info("APPLICATION FINALIZED")

    