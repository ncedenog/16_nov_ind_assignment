#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:57:22 2018

@author: nataliecedeno
"""

#%%
#Exercise 1
shopping_list = {"Guitar":1000,
               "Pick_box":5,
               "Guitar_string":10
               
               }
shopping_cart = ["Guitar", "Guitar_string" ]

def checkout(shopping_cart):
    
    final_price=0
    
    if shopping_cart == []:
        return None
    else:
        for item in shopping_cart:
            final_price = final_price +(shopping_list [item])
    return final_price
    
checkout (shopping_cart)

#%% 
#Exercise 2
    
prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}
#mycart = ["Guitar","Guitar Strings","Guitar Strings","Guitar"]
#mycart = ["Guitar"]
prices_in_cart = []

def checkout_blue(mycart):
    
    if "Insurance" in mycart:
            prices_in_cart.append(prices["Insurance"])
            
    for i in mycart:
    
        if "Insurance" in mycart:
            
            mycart.pop(mycart.index("Insurance"))
            
            print(mycart)
            
    if "Priority mail" in mycart:
            prices_in_cart.append(prices["Priority mail"])
            
    for i in mycart:
    
        if "Priority mail" in mycart:
            
            mycart.pop(mycart.index("Priority mail"))
            
            print(mycart)
        
    if mycart == []:
        return None
    
    else:
        
        for i in mycart: 

            prices_in_cart.append(prices[i])
            
            print(prices_in_cart)
                
    return sum(prices_in_cart)

checkout_blue(["Pick Box", "Guitar","Insurance","Insurance", "Priority mail", "Priority mail"])
#%%





