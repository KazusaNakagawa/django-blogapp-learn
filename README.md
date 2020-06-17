# Django Blog
- django learn

## version
- Django 3.0.5
- Python 3.8.0
- Mac OS
## install
- virtualenv  
~~~
# install
$ sudo pip install virtualenv

# 仮想環境作成
$ virtualenv [<make nane>]

# 仮想環境に入る
$ source [<作成した名前>]/bin/activate

# 抜ける
$ deactivate
~~~

## 環境変数設定
シークレットにしたい変数を設定する
~~~
ex)
$ export SECRET_KEY='< input my key >'
~~~

### database : db.sqlite3
~~~
$ python manage.py makemigrations
$ python manage.py migrate
~~~