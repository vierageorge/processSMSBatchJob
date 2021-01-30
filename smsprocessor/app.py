import logging
from datetime import datetime as dt
from .config import SOURCE_FOLDER_ID, EXPENSE_SHEET_ID, EXPENSE_SHEET_NAME
from .constants import CREDENTIALS_FILE
from smsprocessor.common.exceptions import NotValidExtension, NotValidMimeType
from smsprocessor.services.google_sheet_service import SheetAppender
from smsprocessor.common.utils import process_file
from smsprocessor.services import (
    google_auth_service as gas,
    google_drive_service as gds
    )

logger = logging.getLogger(__name__)

def run():
    logger.info("STARTING APPLICATION")
    expense_appender = SheetAppender(CREDENTIALS_FILE, EXPENSE_SHEET_ID, EXPENSE_SHEET_NAME)
    creds = gas.get_credentials()
    file_list = gds.get_file_list(creds, SOURCE_FOLDER_ID)
    for file in file_list:
        try:
            process_file(creds, file, expense_appender)
        except (NotValidExtension, NotValidMimeType) as e:
            logger.warn(e)
        except Exception as e:
            logger.error(f"{file['name']} :: {e}")
    logger.info(f"Appended {expense_appender.rows_appended} rows.")
    logger.info("APPLICATION FINALIZED")

    