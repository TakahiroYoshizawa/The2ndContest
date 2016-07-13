# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sklearn.linear_model as sklm
import skflow as sf
import os
import matplotlib.pyplot as plt


def read_csv():
    product = pd.read_csv("./data1/product.tsv",delimiter ="\t")
    store = pd.read_csv("./data1/store.tsv",delimiter ="\t")
    sales = pd.read_csv("./data2/sales.tsv",delimiter ="\t")
    test = pd.read_csv("./data3/test.tsv",delimiter ="\t")
    train = pd.read_csv("./data3/train.tsv",delimiter ="\t")

    product = product.fillna(0)
    store = store.fillna(0)
    sales = sales.fillna(0)
    test = test.fillna(0)
    train = train.fillna(0)

    return product, store, sales, test, train

def get_ts():

    pid_list = list(train["pid"].unique())
    area_list = list(train["area"].unique())
    location_list = list(train["location"].unique())
    nlawson_list = list(train["natural_lawson_store"].unique())
    print(pid_list)
    print(area_list)
    print(location_list)
    print(nlawson_list)
    sts = pd.DataFrame(None)
    k=1
    for pid in pid_list:
        train1 = train[train["pid"] == pid]
        for area in area_list:
            train1 = train1[train1["area"] == area]
            for loc in location_list:
                train1 = train1[train1["location"] == loc]
                for nls in nlawson_list:
                    ts = train1[train1["natural_lawson_store"] == nls]

    return sts

if __name__ == "__main__":
    product, store, sales, test, train = read_csv()
    df_list = [product, store, sales, test, train]
    ts = get_ts()
