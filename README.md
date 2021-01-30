# processSMSBatchJob

1. Run with `python -m smsprocessor`
2. A `service_account.json` file is required in the root of the project. This should be generated on the project on Google Console that's being used on the execution of the job.
3. Under `smsprocessor`, a `config.py` file with the following variables defined: SOURCE_FOLDER_ID, PROCESSED_FOLDER_ID, EXPENSE_SHEET_ID, EXPENSE_SHEET_NAME.