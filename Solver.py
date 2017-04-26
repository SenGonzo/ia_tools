import pandas as pd
import scipy.optimize as sp


def solver():

    df = pd.read_csv('input_data/stack_rank.csv')
    df = df[(df['faction'] == 'scum')]
    bounds = []

    c = -df['absolute_total']
    A = df['cost']
    b = [40]

    for index, row in df.iterrows():
        row_bound = [0, row['limit']]
        bounds.append(row_bound)

    res = sp.linprog(c, A_ub=A, b_ub=b, bounds=tuple(bounds), options={"disp": True})

    df['res'] = res['x']
    df = df[(df['res'] > 0)]
    print(df.head())

    return 0
