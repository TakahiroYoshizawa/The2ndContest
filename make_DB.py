# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3 as s3

def read_tsv():
    train = pd.read_csv("./data3/train.tsv",delimiter ="\t")
    train = train.fillna(0)

    return train

def make_sqlite():
    connection = s3.connect("./Test.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE hoge (id INTEGER PRIMARY KEY AUTOINCREMENT, foo TEXT(100) NOT NULL, bar REAL NULL);''')

if __name__ == '__main__':
    train = read_tsv()
