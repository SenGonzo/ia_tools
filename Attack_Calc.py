# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:06:25 2016

@author: ABJ482
"""

import numpy as np
import itertools


def count_occurrences(word, sentence):
    return sentence.lower().split().count(word)


def dice_blob(dice_array):
    # Matrix [Damage, Surge, Accuracy]
    blue_matrix = np.array([[1, 0, 2, 0, 0, 0], [0, 1, 2, 0, 0, 0], [1, 0, 5, 0, 0, 0], [1, 1, 3, 0, 0, 0],
                            [2, 0, 3, 0, 0, 0],  [2, 0, 4, 0, 0, 0]])
    green_matrix = np.array([[0, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [2, 0, 2, 0, 0, 0], [2, 0, 1, 0, 0, 0],
                             [2, 0, 3, 0, 0, 0],  [1, 1, 2, 0, 0, 0]])
    red_matrix = np.array([[1, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0],
                           [3, 0, 0, 0, 0, 0],  [3, 0, 0, 0, 0, 0]])
    yellow_matrix = np.array([[0, 1, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0], [0, 1, 2, 0, 0, 0], [1, 0, 2, 0, 0, 0],
                              [1, 1, 1, 0, 0, 0],  [2, 0, 1, 0, 0, 0]])
    black_matrix = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 2, 0, 0],
                             [0, 0, 0, 2, 0, 0], [0, 0, 0, 3, 0, 0]])
    white_matrix = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0],
                             [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]])
    i = 0
    test_mat = []

    for dice in dice_array:
        if dice == 'green':
            individual_dice_array = green_matrix
        elif dice == 'blue':
            individual_dice_array = blue_matrix
        elif dice == 'red':
            individual_dice_array = red_matrix
        elif dice == 'yellow':
            individual_dice_array = yellow_matrix
        elif dice == 'black':
            individual_dice_array = black_matrix
        elif dice == 'white':
            individual_dice_array = white_matrix
        else:
            continue

        test_mat.append(individual_dice_array)

    dice_perm = np.array(list(itertools.product(*test_mat)))
    dice_rez = np.zeros((dice_perm.shape[0], 6))

    for row in dice_perm:
        for item in row:
            dice_rez[i, 0] += item[0]
            dice_rez[i, 1] += item[1]
            dice_rez[i, 2] += item[2]
            dice_rez[i, 3] += item[3]
            dice_rez[i, 4] += item[4]
            dice_rez[i, 5] += item[5]
        i += 1

    return dice_rez, dice_perm


def surge_results(surges, blocks, surge_array, distance=0, accuracy=1):
    surge_array = np.array(surge_array)
    surge_counter = 0
    value_add = [0, 0]
    # surge_array[damage, peirce, accuracy]

    if surges > surge_array.shape[0]:
        surges = surge_array.shape[0]

    surge_zeros = np.zeros((surge_array.shape[0], 1))
    surge_array = np.append(surge_array, surge_zeros, 1)

    for s in surge_array:
        s[4] = s[0] + min(blocks, s[1])
        if s[2] + accuracy < distance:
            s[4] = 0

    surge_array = np.flipud(surge_array[surge_array[:, 4].argsort()])
    extra_surges = 0

    for s in surge_array:
        surge_counter += s[3]
        if surge_counter > surges:
            surge_counter -= s[3]
            continue
        else:
            value_add[0] += s[4]
            value_add[1] += s[2]

        if s[4] == 0:
            extra_surges += 1

    return value_add, extra_surges


def atk_checks(name, row, surge_array, deadly, attribute_array, distance):
    # Checks of deadly and cancel
    if row[5] > 0 and deadly is True and row[1] - row[4]:
        row[1] -= 1
    elif row[5] > 0:
        row[0] = 0
        return row

    # Adds constant attributes that are not determined by role/surges
    row += attribute_array

    # built in pierce
    if name == 'elite alliance ranger' or name.find('potw') >= 0:
        row[3] = max(0, row[3] - 1)

    if name == 'luke skywalker (saber)':
        row[3] = max(0, row[3] - 3)

    if name == 'elite trandoshan hunter' and distance <= 1:
        row[0] += 2

    if name == 'trandoshan hunter' and distance <= 1:
        row[0] += 1

    # Checks for available Surges and assigns them based on highest single target damage
    val_add, extra_surges = surge_results(row[1] - row[4], row[3], surge_array, distance=distance, accuracy=row[2])

    if row[1] - row[4] > 0:
        row[0] = max(row[0] + val_add[0] - row[3], 0)
    else:
        row[0] = max(row[0] - row[3], 0)

    # Checks if attack has accuracy
    if row[2] + val_add[1] < distance:
        row[0] = 0
    return row


def reroll(name, result, dice_result, dice_pool,
           surge_array, deadly, attribute_array, distance,
           atk_reroll_attack=0, atk_reroll_def=0,
           def_reroll_atk=0, def_reroll_def=0):

    dice_counter = 0
    rez_box = np.zeros((dice_pool.shape[0] + 1, 2))
    rez_box[0, 0] = result
    rez_box[0, 1] = 99
    temp_new_df_results = np.zeros((6, 2))
    for row in temp_new_df_results:
        row[0] = result
        row[1] = 99

    # attack reroll only
    for dice in dice_pool:
        new_atk_rez_array = np.zeros((6, 1))

        if dice not in ('green', 'blue', 'yellow', 'red') or \
                (dice in ('black', 'white') and name in ['elite weequay pirate', 'weequay pirate']):
            dice_counter += 1
            continue

        dice_result_copy = dice_result.copy()
        new_roll = dice_blob([dice])[0]
        roll_counter = 0

        for roll in new_roll:
            dice_result_copy[dice_counter] = roll
            new_rez = np.array([0, 0, 0, 0, 0, 0])
            new_rez2 = np.array([0, 0, 0, 0, 0, 0])

            for row in dice_result_copy:
                new_rez[0] += row[0]
                new_rez[1] += row[1]
                new_rez[2] += row[2]
                new_rez[3] += row[3]
                new_rez[4] += row[4]
                new_rez[5] += row[5]

                new_rez2 = new_rez.copy()

            new_atk_rez_array[roll_counter] = atk_checks(name, new_rez2, surge_array, deadly, attribute_array,
                                                         distance)[0]
            roll_counter += 1

        rez_box[dice_counter+1, 0] = np.average(new_atk_rez_array)
        rez_box[dice_counter+1, 1] = dice_counter

        for row in new_atk_rez_array:
            temp_row = [row[0], dice_counter]
            temp_new_df_results = np.append(temp_new_df_results, [temp_row], axis=0)

        dice_counter += 1

    rez_box = np.flipud(rez_box[rez_box[:, 0].argsort()])
    new_df_results = temp_new_df_results[temp_new_df_results[:, 1] == rez_box[0, 1]]

    return rez_box[0, 0], new_df_results


def results_calc(name, atk_array, def_array='none',
                 surge_array=(0, 0, 0, 1), attribute_array=(0, 0, 0, 0, 0, 0),
                 distance=0, deadly=False, number_of_attacks=1,
                 atk_reroll_attack=0, atk_reroll_def=0,
                 def_reroll_atk=0, def_reroll_def=0,
                 focused=0, hidden=0):

    # atk_array = the dice used in the attack pool eg. 'red','blue'
    # def_array = the dice used in the defense pool eg. 'black','white'
    # surge_array = surges available in the format of (damage, pierce, accuracy) eg. [2,0,0],[0,0,3]
    # attributes = constant attributes that are not determined by role/surges in the format of
    #              (damage, surge, accuracy, block, evade, cancel)
    # distance = number of spaces away target is
    # deadly = can the model surge for deadly T/F
    # number_of_attacks = number of attacks using attributes above

    i = 0

    # Front Line
    if name in ['echo base trooper', 'elite echo base trooper'] and distance <= 1:
        atk_array = ['red', 'green']

    # Flyby
    if name in ['elite jet trooper', 'elite jet trooper (tc)'] and distance <= 2:
        atk_array = ['blue', 'green', 'blue']

    # Overload
    if name in ['rebel saboteur', 'rebel saboteur (tc)', 'elite rebel saboteur', 'elite rebel saboteur (tc)']:
        surge_array = np.append(surge_array, surge_array, axis=0)

    # adding green dice for focused
    if focused == 1:
        atk_array.extend(['green'])

    # adding surge for hidden
    if hidden == 1:
        attribute_array[1] += 1

    dice_array = np.append(atk_array, def_array)
    del_array = []
    big_temp_roll = [np.array([0, 100])]
    del_counter = 0

    for dice in dice_array:
        if dice not in ('green', 'blue', 'yellow', 'red', 'white', 'black'):
            del_array.append(del_counter)
        del_counter += 1

    dice_array = np.delete(dice_array, del_array)
    dice_result, dice_perm = dice_blob(dice_array)

    for row in dice_result:
        row = atk_checks(name, row, surge_array, deadly, attribute_array, distance)

        if atk_reroll_attack > 0 or atk_reroll_def > 0 or def_reroll_atk > 0 or def_reroll_def > 0:
            row[0], temp_roll = reroll(name, row[0], dice_perm[i], dice_array, surge_array, deadly, attribute_array,
                                       distance, atk_reroll_attack, atk_reroll_def, def_reroll_atk, def_reroll_def)

            big_temp_roll = np.append(big_temp_roll, temp_roll, axis=0)
        i += 1

    if atk_reroll_attack > 0 or atk_reroll_def > 0 or def_reroll_atk > 0 or def_reroll_def > 0:
        big_temp_roll = big_temp_roll[big_temp_roll[:, 1] != 100]
        dice_result = big_temp_roll

    top_damage = int(np.amax(dice_result[:, 0]))
    damage_array = np.zeros((top_damage + 1, 1))

    # np.savetxt("qar.csv", dice_result, delimiter=",")

    for row in dice_result:
        damage_array[int(row[0])] += 1

    pdf = damage_array.copy()
    pdf2 = damage_array.copy()
    damage_array = np.flipud(damage_array)
    running_sum = 0
    denom = np.sum(damage_array)

    # Creates cumulative density function of damage
    for row in damage_array:
        running_sum += row[0]
        row[0] = running_sum/denom

    # Creates probability density function of damage
    pdf_counter = 0
    for row in pdf:
        row[0] /= denom
        pdf2[pdf_counter, 0] = pdf_counter
        pdf_counter += 1

    pdf = np.append(pdf2, pdf, 1)

    expected_val = 0
    var_role = 0

    for row in pdf:
        expected_val += row[0] * row[1]

    for row in pdf:
        var_role += (row[0] - expected_val)**2 * row[1]

    damage_array = np.array(np.flipud(damage_array))
    base_array = np.array(np.arange(0, top_damage + 1))

    # Creates arrays for multiple attacks graph
    squad_cdf = np.zeros((np.amax(base_array)*number_of_attacks
                          + 1 - np.amin(base_array)*number_of_attacks, 2), float)

    if number_of_attacks > 1:
        squad_row = np.zeros((np.amax(base_array)*number_of_attacks
                              + 1 - np.amin(base_array)*number_of_attacks, 2), float)
        s_counter = 0
        for srow in squad_row:
            srow[0] = np.amin(base_array)*number_of_attacks + s_counter
            s_counter += 1

        for row in pdf:
            for other_row in pdf:
                for srow in squad_row:
                    if srow[0] == row[0] + other_row[0]:
                        srow[1] += row[1] * other_row[1]

        squad_cdf = squad_row.copy()
        squad_cdf = np.flipud(squad_cdf)

        running_sum = 0

        for row in squad_cdf:
            running_sum += row[1]
            row[1] = running_sum

    # scales expected value to number of attacks
    expected_val *= number_of_attacks

    if number_of_attacks > 1:
        x_array = squad_cdf[:, 0],
        y_array = squad_cdf[:, 1]
    else:
        x_array = np.reshape(base_array, base_array.shape[0]),
        y_array = np.reshape(damage_array, damage_array.shape[0])

    print('{:03.2f}'.format(expected_val), '{:04.2f}'.format(var_role))

    return round(expected_val, 2), round(var_role, 3), np.round(x_array[0], decimals=4), np.round(y_array, decimals=4)
