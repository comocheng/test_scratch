#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'O': 1,
    'C': 2,
    'H': 5,
}

bonds = {
    'C-C': 1,
    'O-H': 1,
    'C-O': 1,
    'C-H': 4,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('[CH2]CO.log'),
}

geometry = Log('[CH2]CO.log')

frequencies = Log('[CH2]CO.log')

rotors = [
     HinderedRotor(scanLog=Log('/Users/nathan/Code/test_scratch/species/[CH2]CO/rotors/[CH2]CO_36by10_0_1.log'), pivots=[1, 2], top=[2, 3, 4, 5, 6, 7], fit='best'),
     HinderedRotor(scanLog=Log('/Users/nathan/Code/test_scratch/species/[CH2]CO/rotors/[CH2]CO_36by10_1_2.log'), pivots=[2, 3], top=[3, 6, 7], fit='best'),
]
