The function is used to send automatic message to the Skype user or particular chat in defined time every business day. Folow next steps to be able to use the script.

Create virtual enviroment:
mkdir venv37
pip install virtualenv
virtualenv --python=/usr/bin/python3 venv37

Activate virtual environment:
source ~/venv37/bin/activate

Install the required libs via:
pip install -r requirements.TXT

Create hidden .env file with login and password and chat_id info:
SK_LOGIN=[login]
SK_PASS=[password]
SK_CHAT_ID=[chat_id]

Launch the script:
python3 sk.py

