#!/usr/bin/env python3
# settings.py
from os.path import join, dirname
from dotenv import load_dotenv
from Game_Files.database.db import Database
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# run migrations and seed
Database().migrateAndSeed()
