import os

# Для указания пути к файлу БД воспользумся путем до текущего модуля
# - Текущая папка
# current_path = os.path.dirname(os.path.realpath(file))


class Config:
    DATABASE = 'mysql+pymysql://root:root@127.0.0.1/restapi'
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False