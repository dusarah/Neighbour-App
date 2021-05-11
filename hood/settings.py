import os
os.environ["SETTINGS_MODULE"] = 'settings'
DATABASE_HOST = '10.0.0.1'

TOKEN_API = os.environ.get("TOKEN_API")
#export SETTINGS_MODULE = 'myproject.settings.testing_settings'
from python_settings import settings
from . import settings as my_local_settings

settings.configure(my_local_settings) # configure() receives a python module
assert settings.configured # now you are set
print(settings.DATABASE_HOST) # Will print '10.0.0.1'
print(settings.DATABASE_NAME) # Will print 'DATABASENAME'

from python_settings import LazySetting
from my_awesome_library import HeavyInitializationClass # Heavy to initialize object

LAZY_INITIALIZATION = LazySetting(HeavyInitializationClass, "127.0.0.1:4222")
# LazySetting(Class, *args, **kwargs)
object_initialized = settings.LAZY_INITIALIZATION # Will return an instance of your object
from .base_settings import *


TOKEN_API = os.environ.get("TOKEN_API")

