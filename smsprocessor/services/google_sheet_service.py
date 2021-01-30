import gspread

class SheetAppender:
    def __init__(self, credentials_path, file_id, sheet_name):
        self.sheet_service = gspread.service_account(credentials_path)
        self.sheet_file = self.sheet_service.open_by_key(file_id)
        self.worksheet = self.sheet_file.worksheet(sheet_name)

    def append_to_sheet(self, date, message):
        self.worksheet.append_row([date,message], value_input_option='USER_ENTERED')