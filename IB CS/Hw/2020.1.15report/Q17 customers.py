#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 08:44:07 2020

@author: hhshhd
"""

import numpy as np
customers = np.array([['lastname2','firstname2','address1b','address2b','adress3b','Cardiff','postcode2'],
                     ['lastname3','firstname3','address1c','address2c','adress3c','city3','postcode3'],
                     ['lastname4','firstname4','address1d','address2d','adress3d','city3','postcode4']])
total = 0 
for counter in range(len(customers)-1):
    if customers[counter][5] == 'Cardiff':
        total = total+1
print(total)
