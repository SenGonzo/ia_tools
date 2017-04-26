
import pandas as pd


def squad_stats(squad_list='lists/list.csv'):
    stats_df = pd.read_csv('input_data/stack_rank.csv')
    list_df = pd.read_csv(squad_list)
    output_df = pd.DataFrame(columns=('name', 'cost', 'type', 'group', 'blk_grp_ev', 'wht_grp_ev', 'health'))
    x = 0

    for index, row in list_df.iterrows():
        for stats_index, stats_row in stats_df.iterrows():
            if row['name'] == stats_row['name']:
                output_df.loc[x] = [stats_row['name'], stats_row['cost'], stats_row['type'],
                                    stats_row['group'], stats_row['blk_grp_ev'],
                                    stats_row['wht_grp_ev'], stats_row['health']]
                x += 1

    output_df.loc[x] = ['Totals:', output_df['cost'].sum(axis=0), ' ',
                        output_df['group'].sum(axis=0), output_df['blk_grp_ev'].sum(axis=0),
                        output_df['wht_grp_ev'].sum(axis=0), output_df['health'].sum(axis=0)]

    return output_df


def squad_compare(squad_lists):

    totals_compare = pd.DataFrame(columns=('name', 'cost', 'type', 'group', 'blk_grp_ev', 'wht_grp_ev', 'health', 'combined_score'))

    x = 0

    for squad_list in squad_lists:
        squad = squad_stats('lists/' + squad_list)
        squad.to_csv('output_data/' + squad_list[:-4] + '_stats.csv')

        totals_compare.loc[x] = [squad_list[:-4], squad['cost'].iloc[-1], ' ', squad['group'].iloc[-1],
                                 squad['blk_grp_ev'].iloc[-1],
                                 squad['wht_grp_ev'].iloc[-1], squad['health'].iloc[-1],
                                 squad['blk_grp_ev'].iloc[-1] + squad['wht_grp_ev'].iloc[-1]
                                 + squad['health'].iloc[-1]/2]

        x += 1

    totals_compare.to_csv('output_data/squad_compare.csv')
