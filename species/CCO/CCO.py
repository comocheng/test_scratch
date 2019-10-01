#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'O': 1,
    'C': 2,
    'H': 6,
}

bonds = {
    'C-C': 1,
    'C-H': 5,
    'O-H': 1,
    'C-O': 1,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('CCO.log'),
}

geometry = Log('CCO.log')

frequencies = Log('CCO.log')

rotors = [
     HinderedRotor(scanLog=Log('/Users/nathan/Code/test_scratch/species/CCO/rotors/CCO_36by10_0_1.log'), pivots=[1, 2], top=[2, 3, 4, 5, 6, 7, 8], fit='best'),
     HinderedRotor(scanLog=Log('/Users/nathan/Code/test_scratch/species/CCO/rotors/CCO_36by10_1_2.log'), pivots=[2, 3], top=[3, 6, 7, 8], fit='best'),
]
