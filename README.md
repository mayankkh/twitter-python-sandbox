Setup
-----

* Clone the repository
* Replace the credentials.py.orig with credentials.py and actual credentials.
* Install flask in a virtual environment

```
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```

* Install tweepy

```
$ flask/bin/pip install tweepy
```

Usage
-----
* Simple test script to post dummy tweets
* ./tweetbot.py

* Simple REST API to query twitter trends
* ./app.py
The app runs on 127.0.0.1:5000


