# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:33:39 2022

@author: romas
"""

import criterions as c

import additional_criterions as ac

import get_data as gd

import prettytable as pt


criterions_res = pt.PrettyTable()

criterions_res.field_names = ["Критерій", "φ_1", "φ_2", "φ_3", "φ_4", "Оптимальне рішення"]



probabilities, efficacy = gd.get_data_from_file("variant.txt")

print("Вхідні дані:")

print(probabilities)

print(efficacy)

print()


Bayes_order, eff_square, row = c.criteria_calculation(probabilities, efficacy, "Bayes", [])

criterions_res.add_row(row)


Bayes_values = list(Bayes_order.values())

min_disp_order, row = c.criteria_calculation(probabilities, efficacy, "min_disp", Bayes_values)

criterions_res.add_row(row)

dispersion = list(min_disp_order.values())


Bayes_average = (1/len(efficacy[0])) * sum(Bayes_values)

row = c.criteria_calculation(probabilities, efficacy, "min_disp_mod", Bayes_average)

criterions_res.add_row(row)


Bayes_max = max(Bayes_values)

row = c.criteria_calculation(probabilities, efficacy, "min_disp_mod", Bayes_max)

criterions_res.add_row(row)


row = c.criteria_calculation(probabilities, efficacy, "max_prob_dist", [])

criterions_res.add_row(row)


row = ac.modal(probabilities, efficacy)

criterions_res.add_row(row)


row = ac.minimal_entropy(probabilities, efficacy)

criterions_res.add_row(row)


row_1, row_2, row_3 = ac.combined(Bayes_values, eff_square, dispersion)

criterions_res.add_row(row_1)

criterions_res.add_row(row_2)

criterions_res.add_row(row_3)

print(criterions_res)
