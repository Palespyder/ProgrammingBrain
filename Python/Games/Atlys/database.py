import pygame as pg
import sqlite3


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('data/AtlysDB.db')

    def create_player(self):
        pass

    def save_player(self):
        pass