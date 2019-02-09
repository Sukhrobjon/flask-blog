import os

class Config:
    # TO-DO MOVE THE KEYS TO .BASH_PROFILE
    SECRET_KEY = '18426b92a85573844291a91f89f3e3e5'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')