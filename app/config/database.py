import os
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

NAME_DB=os.getenv('NAME_DB')
PASS_DB=os.getenv('PASS_DB')
USER_DB=os.getenv('USER_DB')
HOST_DB=os.getenv('HOST_DB')

FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@localhost:5433/{NAME_DB}'