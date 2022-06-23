import os

# Для указания пути к файлу БД воспользумся путем до текущего модуля
# - Текущая папка
# current_path = os.path.dirname(os.path.realpath(file))


class Config:
    DEBUG = True
    SECRET_KEY = "randomstringstep"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/db_crm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False