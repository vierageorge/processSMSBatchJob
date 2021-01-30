import logging
from datetime import datetime as dt
from .config import SOURCE_FOLDER_ID, EXPENSE_SHEET_ID, EXPENSE_SHEET_NAME
from .constants import CREDENTIALS_FILE
from smsprocessor.common.exceptions import NotValidExtension, NotValidMimeType
from smsprocessor.services.sheet_appender_service import SheetAppenderService
from smsprocessor.common.utils import process_file
from smsprocessor.services.drive_service import DriveService

logger = logging.getLogger(__name__)

def run():
    logger.info("STARTING APPLICATION")
    expense_appender = SheetAppenderService(CREDENTIALS_FILE, EXPENSE_SHEET_ID, EXPENSE_SHEET_NAME)
    drive_service = DriveService(CREDENTIALS_FILE)
    file_list = drive_service.get_file_list(SOURCE_FOLDER_ID)
    for file in file_list:
        try:
            process_file(drive_service, file, expense_appender)
        except (NotValidExtension, NotValidMimeType) as e:
            logger.warn(e)
        except Exception as e:
            logger.error(f"{file['name']} :: {e}")
    logger.info(f"Appended {expense_appender.rows_appended} rows.")
    logger.info("APPLICATION FINALIZED")

    