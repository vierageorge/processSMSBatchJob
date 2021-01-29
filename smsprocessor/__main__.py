import logging
from datetime import datetime as dt
from smsprocessor import app
from os import path

LOG_PATH = path.join('logs', f"{dt.now().strftime('%Y%m%d')}.log")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename=LOG_PATH,
                    filemode='a', format='[%(levelname)s] %(asctime)s %(name)s %(message)s')
    app.run()