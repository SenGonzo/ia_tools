
import pandas as pd
import matplotlib.pyplot as plt
import Attack_Calc as atk
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


def data_input():

    # import and fold data
    df = pd.read_csv('input_data/units.csv')
    df.sort_values(by=['name'], ascending=[True], inplace=True)
    pdf_pages = PdfPages('IA Statbook v0_1.pdf')

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

        wht_ev_focused, \
            wht_var_focused, \
            wht_x_array_focused, \
            wht_y_array_focused = atk.results_calc(row['name'], row['dice'].split(', '), ['white'],
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

        tab_data = [[blk_ev, blk_var],
                    [blk_ev_focused, blk_var_focused],
                    [blk_ev_hidden, blk_var_hidden],
                    [blk_ev_focused_hidden, blk_var_focused_hidden],
                    [wht_ev, wht_var],
                    [wht_ev_focused, wht_var_focused],
                    [wht_ev_hidden, wht_var_hidden],
                    [wht_ev_focused_hidden, wht_var_focused_hidden]]

        logo = plt.imread(str.format('pics/{}.png', row['name']))
        sns.set_style('darkgrid')
        fig = plt.figure(figsize=(11, 8.5))

        # plt1 = plt.subplot(gs[0, 1])
        plt1 = plt.subplot2grid((4, 5), (0, 1), colspan=2)
        ax1 = plt.gca()
        plt.setp(plt1.get_xticklabels(), visible=False)
        plt.setp(plt1.get_yticklabels(), visible=False)
        plt.plot(blk_y_array.tolist(), '-o')
        plt.ylabel('No Conditions', fontsize=12)
        for x, y in zip(np.arange(0, len(blk_y_array.tolist()) + 1), blk_y_array.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax1.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt2 = plt.subplot(gs[1, 1], sharex=plt1, sharey=plt1)
        plt2 = plt.subplot2grid((4, 5), (1, 1), colspan=2, sharex=plt1, sharey=plt1)
        ax2 = plt.gca()
        plt.setp(plt2.get_xticklabels(), visible=False)
        plt.setp(plt2.get_yticklabels(), visible=False)
        plt.plot(blk_y_array_focused.tolist(), '-o')
        plt.ylabel('Focused', fontsize=12)
        for x, y in zip(np.arange(0, len(blk_y_array_focused.tolist()) + 1), blk_y_array_focused.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax2.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt3 = plt.subplot(gs[2, 1], sharex=plt1, sharey=plt1)
        plt3 = plt.subplot2grid((4, 5), (2, 1), colspan=2, sharex=plt1, sharey=plt1)
        ax3 = plt.gca()
        plt.setp(plt3.get_xticklabels(), visible=False)
        plt.setp(plt3.get_yticklabels(), visible=False)
        plt.plot(blk_y_array_hidden.tolist(), '-o')
        plt.ylabel('Hidden', fontsize=12)
        for x, y in zip(np.arange(0, len(blk_y_array_hidden.tolist()) + 1), blk_y_array_hidden.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax3.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt4 = plt.subplot(gs[3, 1], sharex=plt1, sharey=plt1)
        plt4 = plt.subplot2grid((4, 5), (3, 1), colspan=2, sharex=plt1, sharey=plt1)
        ax4 = plt.gca()
        plt.setp(plt4.get_yticklabels(), visible=False)
        plt.plot(blk_y_array_focused_hidden.tolist(), '-o')
        plt.ylabel('Hidden and Focused', fontsize=12)
        for x, y in zip(np.arange(0, len(blk_y_array_focused_hidden.tolist()) + 1), blk_y_array_focused_hidden.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax4.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt5 = plt.subplot(gs[0, 2], sharex=plt1, sharey=plt1)
        plt5 = plt.subplot2grid((4, 5), (0, 3), colspan=2, sharex=plt1, sharey=plt1)
        ax5 = plt.gca()
        plt.setp(plt5.get_xticklabels(), visible=False)
        plt.setp(plt5.get_yticklabels(), visible=False)
        plt.plot(wht_y_array.tolist(), '-o')
        for x, y in zip(np.arange(0, len(wht_y_array.tolist()) + 1), wht_y_array.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax5.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt6 = plt.subplot(gs[1, 2], sharex=plt1, sharey=plt1)
        plt6 = plt.subplot2grid((4, 5), (1, 3), colspan=2, sharex=plt1, sharey=plt1)
        ax6 = plt.gca()
        plt.setp(plt6.get_xticklabels(), visible=False)
        plt.setp(plt6.get_yticklabels(), visible=False)
        plt.plot(wht_y_array_focused.tolist(), '-o')
        for x, y in zip(np.arange(0, len(wht_y_array_focused.tolist()) + 1), wht_y_array_focused.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax6.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt7 = plt.subplot(gs[2, 2], sharex=plt1, sharey=plt1)
        plt7 = plt.subplot2grid((4, 5), (2, 3), colspan=2, sharex=plt1, sharey=plt1)
        ax7 = plt.gca()
        plt.setp(plt7.get_xticklabels(), visible=False)
        plt.setp(plt7.get_yticklabels(), visible=False)
        plt.plot(wht_y_array_hidden.tolist(), '-o')
        for x, y in zip(np.arange(0, len(wht_y_array_hidden.tolist()) + 1), wht_y_array_hidden.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax7.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # plt8 = plt.subplot(gs[3, 2], sharex=plt1, sharey=plt1)
        plt8 = plt.subplot2grid((4, 5), (3, 3), colspan=2, sharex=plt1, sharey=plt1)
        ax8 = plt.gca()
        plt.setp(plt8.get_yticklabels(), visible=False)
        plt.plot(wht_y_array_focused_hidden.tolist(), '-o')
        for x, y in zip(np.arange(0, len(wht_y_array_focused_hidden.tolist()) + 1), wht_y_array_focused_hidden.tolist()):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax8.annotate('{}'.format(y), xy=(x, y), xytext=(10, -20), ha='right',
                        textcoords='offset points')

        # Build the Image

        plt_img = plt.subplot2grid((4, 5), (0, 0), rowspan=2)
        img = plt_img.imshow(logo)
        plt_img.axis('off')

        # Build the Table

        plt_table = plt.subplot2grid((4, 5), (3, 0), rowspan=2)
        the_table = plt_table.table(cellText=tab_data, colLabels=('Expected Damage', 'Variance'), loc='top')
        plt_table.axis('off')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(9)

        plt1.set_title('Attacking Black Dice', fontsize=12)
        plt5.set_title('Attacking White Dice', fontsize=12)

        plt1.margins(x=.01, y=.2)
        plt2.margins(x=.01, y=.2)
        plt3.margins(x=.01, y=.2)
        plt4.margins(x=.01, y=.2)
        plt5.margins(x=.01, y=.2)
        plt6.margins(x=.01, y=.2)
        plt7.margins(x=.01, y=.2)
        plt8.margins(x=.01, y=.2)

        fig.suptitle(row['name'].upper(), fontsize=16) # , ha='left', backgroundcolor='red')

        # plt.show()
        fig.set_size_inches(16, 9)
        #fig.savefig('test.pdf', bbox_inches='tight', facecolor='w')
        pdf_pages.savefig(fig)

    pdf_pages.close()

    return 0



