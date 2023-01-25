from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

debug = True
secret_key = 'django-insecure-i*s6)jr!@)l%g7p06hmdt-9=9wx!j4r^%33i=@)iomy+_&-lq)'
database = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
