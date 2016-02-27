# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:37:30 2016

@author: jmcontreras
"""

#1: shuffle the cards

# IMPORT MODULES

import os
import numpy as np
import pandas as pd


# DECLARE VARIABLES

main_dir = '/Users/jmcontreras/GitHub/risk/'
ters_file = os.path.join(main_dir, 'territories.csv')
n_players = 3


# DEFINE FUNCTIONS

def assign_territories(ters, n_players):
    '''Assign each territory to a player. If even assignment is not possible,
    assign extra territories to the players who go last.'''
    # Count number of territories
    n_ters = ters.shape[0]
    # Create non-random assignment
    ters_assignment = np.tile(np.arange(n_players) + 1,
                              round(n_ters / n_players))[-n_ters:]
    # Randomly assign territories to players
    ters['player'] = np.random.permutation(ters_assignment)
    # Initialize army counts
    ters['armies'] = ters['stars']
    # Return territory DF
    return ters


# ASSIGN TERRITORIES

ters = pd.read_csv(ters_file)
n_ters = ters.shape[0]
ters = assign_territories(ters, n_ters)


# DETERMINE NUMBER OF REINFORCEMENTS

# DETERMINE NUMBER OF REINFORCEMENTS

for p in range(1, n_players + 1):
    base = 3
    ter_bonus =
    continent_bonus = 
    card_bonus =