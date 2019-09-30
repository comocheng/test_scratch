#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 2,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'O-H': 1,
    'C-C': 1,
    'C-H': 5,
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

