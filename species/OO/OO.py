#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'O': 2,
    'H': 2,
}

bonds = {
    'O-O': 1,
    'O-H': 2,
}

linear = False

externalSymmetry = 2

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('OO.log'),
}

geometry = Log('OO.log')

frequencies = Log('OO.log')

rotors = [
     HinderedRotor(scanLog=Log('/Users/nathan/Code/test_scratch/species/OO/rotors/OO_36by10_0_1.log'), pivots=[1, 2], top=[2, 4], fit='best'),
]
