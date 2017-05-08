# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:13:53 2016

@author: ABJ482
"""
import Attack_Calc as atk
import Data_manip as dtm
import Analysis_sketchpad as ansp
import squad_stats as ss
import Solver as so
import IA_Statbook as IAS

# from bokeh.plotting import figure, output_file, show, ColumnDataSource
# from bokeh.models import HoverTool


# ----- TO DO LIST

# Attack_calc: reroll multiple
# Attack_calc: double surges optimizer
# Attack_calc: odds of surge/extra surges ev/cdf: added to attack_checks need to figure out next steps

# ---- ATTACK CALC
# example input: atk.results_calc(['green', 'green'], ['black'], surge_array=[[2, 0, 0, 1], [0, 1, 0, 1]])
# return expected_val, var_role, x_array, y_array
# ev, var, x_array, y_array = atk.results_calc('',
#                                              ['red', 'red'], ['black'],
#                                              surge_array=[[0, 0, 0, 1], [0, 0, 0, 1]],
#                                              attribute_array=[0, 0, 0, 0, 0, 0],
#                                              distance=0,
#                                              deadly=False,
#                                              number_of_attacks=1,
#                                              atk_reroll_attack=1,
#                                              def_reroll_atk=0,
#                                              focused=0)
#
# print(ev, var, x_array, y_array)

# ---- SOURCE BOOK
IAS.data_input()

# ---- STACK RANK
# dtm.create_stack_rank(dtm.data_input())

# ---- SOLVER
# so.solver()

#---- SQUAD STATS
# ss.squad_compare(['regionals.csv', 'regionals_v2.csv', 'scum_scum.csv', 'scum_onar.csv'])

# ---- ONE OFF ANALYSIS
# ansp.create_stack_rank(ansp.data_input())

# output_file('line.html')
#
# source = ColumnDataSource(
#     data=dict(
#         x=x_array,
#         y=y_array
#     )
# )
#
# hover = HoverTool(
#     tooltips=[
#         ('Damage', '@x'),
#         ('Probability', '@y'),
#     ]
# )
#
# p = figure(plot_width=800, plot_height=600, tools=[hover])
# p.circle(x='x', y='y', source=source, size=10, color='navy', alpha=0.5)
# show(p)

