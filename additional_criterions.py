# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:01:29 2022

@author: romas
"""

import math as m

import criterions as c

import random as r



def modal(p_arr, eff_arr):
    
    row = []
    
    row.append("Модальний")
    
    theta_max = max(p_arr)
    
    ind = p_arr.index(theta_max)
    
    best_solution = f"φ_{eff_arr[ind].index(max(eff_arr[ind]))+1}"
    
    for i in eff_arr[ind]:
        
        row.append(i)
    
    row.append(best_solution)
    
    return row

def minimal_entropy(p_arr, eff_arr):
    
    row = []
    
    row.append("Мінімальної ентропії")
    
    sums = []
    
    res_dict = {}
    
    i = 0
    
    
    while i < len(eff_arr[0]):
        
        res_temp = 0
        
        j = 0
        
        while j < len(eff_arr):
        
            res_temp += p_arr[j] * eff_arr[j][i]
            
            j += 1
            
        sums.append(res_temp)
        
        i += 1

    
    i = 0
    
    while i < len(eff_arr[0]):
        
        res = 0
        
        j = 0
        
        while j < len(eff_arr):
        
            temp_var = (p_arr[j] * eff_arr[j][i]) / sums[i]
            
            try:   
                
                res += temp_var * m.log(temp_var)
                
                print(temp_var * m.log(temp_var))
                
            except ValueError:
                
                res += 0
            
            j += 1 
            
        res = -res
        
        row.append(res)
        
        res_dict[f"φ_{i+1}"] = res
        
        print()
        
        i += 1
    
    sorted_dict = sorted(res_dict.items(), key=lambda x: x[1])
    
    best_solution = c.check_for_equals(sorted_dict)
    
    if len(best_solution) == 0:
        
        best_solution = sorted_dict[0][0]
    
    row.append(best_solution)
    
    return row

def combined(Bayes_val, eff_square, disp):
 
    lambda_arr = []
    
    
    i = 0
    
    while i < len(Bayes_val):
        
        Bayes_val[i] = Bayes_val[i]**2
        
        lambda_arr.append(Bayes_val[i]/eff_square[i])
        
        i += 1
        
    lambda_min = min(lambda_arr)
    
    lambda_max = max(lambda_arr)
    
    row_1 = combined_calculate(Bayes_val, disp, lambda_min, lambda_max, 0)
    
    row_2 = combined_calculate(Bayes_val, disp, lambda_min, lambda_max, 1)
    
    row_3 = combined_calculate(Bayes_val, disp, lambda_min, lambda_max, 2)
   
    
    return row_1, row_2, row_3

def combined_calculate(Bayes, d, lambda_min, lambda_max, num):
    
    row = []
    
    res_dict = {}
    
    if num == 0:
    
        lambda_used = 0 + (r.random() * (lambda_min - 0))
        
    elif num == 1:
        
        lambda_used = lambda_min + (r.random() * (lambda_max - lambda_min))

    elif num == 2:
        
        lambda_used = lambda_max + (r.random() * (1- lambda_max))
        
    row.append(f"Комбінований за λ = {lambda_used}")
    
    i = 0
    
    while i < len(Bayes):
        
        res = Bayes[i] * (1-lambda_used) - lambda_used * d[i]
        
        res_dict[f"φ_{i+1}"] = res
        
        row.append(res)
        
        i += 1
        
    sorted_dict = sorted(res_dict.items(), key=lambda x: x[1], reverse = True)
     
    best_solution = c.check_for_equals(sorted_dict)
     
    if len(best_solution) == 0:
         
        best_solution = sorted_dict[0][0]
     
    row.append(best_solution)
    
    return row
        