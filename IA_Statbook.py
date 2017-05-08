
import pandas as pd
import matplotlib.pyplot as plt
import Attack_Calc as atk


def data_input():

    # import and fold data
    df = pd.read_csv('input_data/units_test.csv')
    df.sort_values(by=['name'], ascending=[True], inplace=True)

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

        blk_ev_focused, blk_var_focused, blk_x_array_focused, blk_y_array_focused = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['black'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     focused=1)

        blk_ev_hidden, blk_var_hidden, blk_x_array_hidden, blk_y_array_hidden = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['black'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     hidden=1)

        blk_ev_focused_hidden, blk_var_focused_hidden, blk_x_array_focused_hidden, blk_y_array_focused_hidden = \
                                                                     atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['black'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     focused=1,
                                                                     hidden=1)

        wht_ev, wht_var, wht_x_array, wht_y_array = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['white'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'])

        wht_ev_focused, wht_var_focused, wht_x_array_focused, wht_y_array_focused = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['white'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     focused=1)

        wht_ev_hidden, wht_var_hidden, wht_x_array_hidden, wht_y_array_hidden = atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['white'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     hidden=1)

        wht_ev_focused_hidden, wht_var_focused_hidden, wht_x_array_focused_hidden, wht_y_array_focused_hidden = \
                                                                     atk.results_calc(row['name'],
                                                                     row['dice'].split(', '), ['white'],
                                                                     surge_array=[surge_1, surge_2, surge_3, surge_4],
                                                                     attribute_array=attribute_array,
                                                                     distance=0,
                                                                     deadly=deadly,
                                                                     number_of_attacks=1,
                                                                     atk_reroll_attack=row['reroll attack'],
                                                                     atk_reroll_def=row['reroll def'],
                                                                     focused=1,
                                                                     hidden=1)
        blk_y_array.tolist()

        plt.figure(1)
        plt.subplot(211)
        plt.plot(blk_y_array.tolist(), '-o')
        plt.subplot(212)
        plt.plot(wht_x_array.tolist(), wht_y_array.tolist())

        plt.show()

    return 0



