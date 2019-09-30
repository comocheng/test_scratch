#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 2,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'O-H': 1,
    'C-C': 1,
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

