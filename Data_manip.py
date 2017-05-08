
import pandas as pd
import Attack_Calc as atk


def data_input():

    # import and fold data
    df = pd.read_csv('input_data/units.csv')
    # df = df[(df['faction'] == 'scum')]
    # df = df[(df['single model health'] >= 5)]
    df.sort_values(by=['name'], ascending=[True], inplace=True)
    rez_df = pd.DataFrame(columns=('name', 'faction', 'limit', 'cost', 'type', 'group', 'blk_grp_ev', 'blk_cost_eff', 'wht_grp_ev', 'wht_cost_eff',
                                   'health', 'hit_ef'))
    x = 0
    limit = 0

    for index, row in df.iterrows():
        print(row['name'])
        surge_1 = [int(i) for i in row['surge 1'].split(',')]
        surge_2 = [int(i) for i in row['surge 2'].split(',')]
        surge_3 = [int(i) for i in row['surge 3'].split(',')]
        surge_4 = [int(i) for i in row['surge 4'].split(',')]
        attribute_array = [row['damage att'], row['surge att'], row['acc att'], 0, 0, 0]
        if row['deadly'] == 1:
            deadly = True
        else:
            deadly = False

        blk_ev, blk_var, blk_x_array, blk_y_array = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['black'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'])

        wht_ev, wht_var, wht_x_array, wht_y_array = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['white'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'])

        blk_grp_ev = blk_ev * row['group']
        blk_cost_eff = blk_grp_ev / row['cost']

        wht_grp_ev = wht_ev * row['group']
        wht_cost_eff = wht_grp_ev / row['cost']

        hit_ef = row['group'] * row['single model health'] * 1.0000 / row['cost']

        if row['status'] == 'char':
            limit = 1
        elif row['status'] == 'elite':
            limit = 2
        else:
            limit = 4

        rez_df.loc[x] = [row['name'], row['faction'], limit, row['cost'], row['type'], row['group'], blk_grp_ev, blk_cost_eff, wht_grp_ev, wht_cost_eff,
                         row['single model health'] * row['group'], hit_ef]

        x += 1

    return rez_df


def create_stack_rank(rez_df):

    rez_df['blk_rank_weight'] = rez_df['blk_cost_eff'].rank(ascending=1)
    rez_df['wht_rank_weight'] = rez_df['wht_cost_eff'].rank(ascending=1)
    rez_df['hp_rank_weight'] = rez_df['hit_ef'].rank(ascending=1)
    rez_df['total'] = (rez_df['blk_rank_weight'] + rez_df['wht_rank_weight'] + rez_df['hp_rank_weight']) / \
                      (len(rez_df.index) * 3)
    rez_df['absolute_total'] = (rez_df['blk_grp_ev'] + rez_df['wht_grp_ev'] + rez_df['health']/2)

    rez_df.sort_values(by=['total'], ascending=[False], inplace=True)
    rez_df.to_csv('input_data/stack_rank.csv')
