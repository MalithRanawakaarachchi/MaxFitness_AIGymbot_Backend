## Initial Setup:

create a virtual environment
```
$ python -m venv venv
$ venv\Scripts\activate.bat
```
Install dependencies
```
$ python -m pip install -r requirements.txt
```
Install nltk package
```
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## train the bot
python train.py

## run the chat application
python chat.py

## run the web server application
python server.py