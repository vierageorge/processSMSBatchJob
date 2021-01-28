import logging
from smsprocessor.services import google_auth_service, google_drive_service
from .constants import FOLDER_ID

logger = logging.getLogger(__name__)

def run():
    logger.info("STARTING APPLICATION")
    creds = google_auth_service.get_credentials()
    google_drive_service.get_file_list(creds, FOLDER_ID)
    logger.info("APPLICATION FINALIZED")