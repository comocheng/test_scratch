#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'O': 3,
    'C': 2,
    'H': 7,
}

bonds = {
    'O-O': 1,
    'C-H': 5,
    'C-C': 1,
    'C-O': 1,
    'O-H': 2,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('CCO+[O]O_OO+[CH2]CO.log'),
}

geometry = Log('CCO+[O]O_OO+[CH2]CO.log')

frequencies = Log('CCO+[O]O_OO+[CH2]CO.log')

rotors = []

