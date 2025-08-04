# import os
#
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# load_dotenv()
#
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_NAME = os.getenv("DB_NAME")
#
# DATABASE_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
#
# engine = create_engine(DATABASE_URL, echo=True)
#
# SessoinLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()