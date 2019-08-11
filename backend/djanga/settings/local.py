from decouple import config
from dj_database_url import parse as db_url

from .local_base import *  # noqa

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///{}'.format(base_dir_join('db.sqlite3')),
        cast=db_url,
    )
}
