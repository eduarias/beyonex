import os

import dotenv

dotenv.load_dotenv()

BROWSER = os.getenv('BROWSER', 'chrome')
REMOTE_BROWSER_URL = os.getenv('REMOTE_BROWSER_URL', False)
SERVER = os.getenv("SERVER", 'https://weathershopper.pythonanywhere.com/')
