from smsprocessor.services import google_auth_service, google_drive_service

def run():
    creds = google_auth_service.get_credentials()
    google_drive_service.get_file_list(creds)