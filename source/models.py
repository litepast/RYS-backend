from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from config import mysql_connection

engine = create_engine(mysql_connection)
Base = automap_base()
Base.prepare(autoload_with=engine)
Albums_table = Base.classes.albums

