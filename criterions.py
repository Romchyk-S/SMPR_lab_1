# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:44:01 2022

@author: romas
"""

import random as r

def check_for_equals(arr):
    
    keys_equal = []
    
    i = 0
    
    while i < 1:
        
        j = i+1
        
        while j < len(arr):
            
            if arr[i][1] == arr[j][1]:
                
                if arr[i][0] not in keys_equal:
                
                    keys_equal.append(arr[i][0])
                    
                if arr[j][0] not in keys_equal:
                
                    keys_equal.append(arr[j][0])
            
            j += 1
            
        i += 1        
                
        return keys_equal
    
def criteria_calculation(p_arr, eff_arr, criterion, Bayes_val):
    
    i = 0
    
    row = []
    
    eff_square = []
    
    res_dict = {}
    
    if criterion == "max_prob_dist":
        
        min_arr = []
        
        max_arr = []
        
        for e in eff_arr:
            
            min_arr.append(min(e))
            
            max_arr.append(max(e))
        
        a_1 = min(min_arr)
        
        a_2 = max(max_arr)
        
        a = r.randint(a_1, a_2)
        
        a = 5
        
    
    while i < len(eff_arr[0]):
        
        res = 0
        
        res_1 = 0
        
        j = 0
        
        while j < len(eff_arr):
            
            if criterion == "Bayes":
                
                if len(row) == 0:
                    
                    row.append("Баєс")
                    
                arr = Bayes(p_arr[j], eff_arr[j][i])
                
                res += arr[0]
                
                res_1 += arr[1]
                
            elif criterion == "min_disp":
                
                if len(row) == 0:
                    
                    row.append("Мінімуму дисперсії")
                
                res += dispersion_minimum(p_arr[j], eff_arr[j][i], Bayes_val[i])
                
            elif criterion == "min_disp_mod":
                
                if len(row) == 0:
                    
                    row.append("Мінімуму дисперсії модифікація")
                
                res += dispersion_minimum(p_arr[j], eff_arr[j][i], Bayes_val)
                
            elif criterion == "max_prob_dist":
                
                if len(row) == 0:
                    
                    row.append("Максимізації ймовірности")
                
                res += max_prob_dist(p_arr[j], eff_arr[j][i], a)
            
            j += 1
            
        
        row.append(res)    
        
        res_dict[f"φ_{i+1}"] = res
        
        if criterion == "Bayes":
            
            eff_square.append(res_1)

        i += 1
        
    
    if criterion == "Bayes" or criterion == "max_prob_dist":
        
        sorted_dict = sorted(res_dict.items(), key=lambda x: x[1], reverse = True)
        
    elif criterion == "min_disp" or  criterion == "min_disp_mod":
        
        sorted_dict = sorted(res_dict.items(), key=lambda x: x[1])
        
    

    best_solution = check_for_equals(sorted_dict)
    
    if len(best_solution) == 0:
        
        best_solution = sorted_dict[0][0]
    
    row.append(best_solution)
    
    if criterion == "Bayes":
    
        return res_dict, eff_square, row
    
    elif criterion == "min_disp":
        
        return res_dict, row
    
    else:
        
        return row
    
def Bayes(p, eff):
           
    res = p * eff
    
    res_1 = p * (eff**2)
    
    return res, res_1
    
def dispersion_minimum(p, eff, disp):
    
    res = (eff-disp)**2 * p
            
    return res

def max_prob_dist(p, eff, a):
    
    if eff >= a:
        
        return p
    
    else:
    
        return 0