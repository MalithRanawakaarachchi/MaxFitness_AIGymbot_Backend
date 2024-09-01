## Initial Setup:

create a virtual environment outside the folder
```
$ python -m venv venv
$ venv\Scripts\activate.bat
```

Install dependencies
```
$ python -m pip install -r requirements.txt --user
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

## run this after any new package installed

python -m pip freeze > requirements.txt

 python .\server.py

