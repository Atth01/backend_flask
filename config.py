from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/db_react'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your-secret-key'  # Ganti dengan kunci rahasia yang aman
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Token kadaluarsa setelah 1 jam
