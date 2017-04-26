
import pandas as pd
import Attack_Calc as atk


def data_input():

    # import and fold data
    df = pd.read_csv('input_data/units.csv')
    # df = df[(df['faction'] == 'scum')]
    # df = df[(df['single model health'] >= 5)]
    df.sort_values(by=['name'], ascending=[True], inplace=True)
    rez_df = pd.DataFrame(columns=('name', 'cost', 'type', 'group', 'blk_ev', 'hid_blk_ev', 'wht_ev', 'hid_wht_ev',
                                   'health', 'blk_delta', 'wht_delta'))
    x = 0

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
                                                                     atk_reroll_def=row['reroll def'],
                                                                     focused=0)

        fcs_blk_ev, fcs_blk_var, \
        fcs_blk_x_array, fcs_blk_y_array = atk.results_calc(row['name'],
                                                            row['dice'].split(', '), ['black'],
                                                            surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                            attribute_array=attribute_array,
                                                            distance=0,
                                                            deadly=deadly,
                                                            number_of_attacks=1,
                                                            atk_reroll_attack=row['reroll attack'],
                                                            atk_reroll_def=row['reroll def'],
                                                            hidden=1)

        wht_ev, wht_var, wht_x_array, wht_y_array = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['white'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     focused=0)

        fcs_wht_ev, fcs_wht_var, \
        fcs_wht_x_array, fcs_wht_y_array =  atk.results_calc(row['name'],
                                                             row['dice'].split(', '), ['white'],
                                                             surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                             attribute_array=attribute_array,
                                                             distance=0,
                                                             deadly=deadly,
                                                             number_of_attacks=1,
                                                             atk_reroll_attack=row['reroll attack'],
                                                             atk_reroll_def=row['reroll def'],
                                                             hidden=1)

        rez_df.loc[x] = [row['name'], row['cost'], row['type'], row['group'], blk_ev, fcs_blk_ev, wht_ev, fcs_wht_ev,
                         row['single model health'], fcs_blk_ev - blk_ev, fcs_wht_ev - wht_ev]

        x += 1

    return rez_df


def create_stack_rank(rez_df):

    rez_df['total'] = (rez_df['blk_delta'] + rez_df['wht_delta'])

    rez_df.sort_values(by=['total'], ascending=[False], inplace=True)
    rez_df.to_csv('output_data/hidden_rank.csv')
