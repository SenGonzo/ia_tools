
import pandas as pd
import Attack_Calc as atk


def ig88_bestdice():

    rez_df = pd.DataFrame(columns=('dice', 'blk_ev', 'wht_ev'))
    dice = ['red', 'green', 'blue', 'yellow']
    x = 0
    for d1 in dice:
        for d2 in dice:
            dice_list = [d1, d2, 'green']

            blk_ev, blk_var, blk_x_array, blk_y_array = atk.results_calc('IG88',
                                                                         dice_list, ['black'],
                                                                         surge_array=[[2, 0, 0], [0, 1, 0]],
                                                                         attribute_array=[0, 0, 2, 0, 0, 0],
                                                                         distance=0,
                                                                         deadly=False,
                                                                         number_of_attacks=1,
                                                                         atk_reroll_attack=0,
                                                                         atk_reroll_def=0)

            wht_ev, wht_var, wht_x_array, wht_y_array = atk.results_calc('IG88',
                                                                         dice_list, ['white'],
                                                                         surge_array=[[2, 0, 0], [0, 1, 0]],
                                                                         attribute_array=[0, 0, 2, 0, 0, 0],
                                                                         distance=0,
                                                                         deadly=False,
                                                                         number_of_attacks=1,
                                                                         atk_reroll_attack=0,
                                                                         atk_reroll_def=0)
            rez_df.loc[x] = [dice_list, blk_ev, wht_ev]

            x += 1

    rez_df.sort_values(by=['blk_ev'], ascending=[False], inplace=True)
    rez_df.to_csv('output_data/ig88.csv')

    return rez_df


