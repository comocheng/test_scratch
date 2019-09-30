#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 2,
    'O': 3,
}

bonds = {
    'C-O': 2,
    'O-O': 2,
    'O-H': 4,
    'C-C': 2,
    'C-H': 10,
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

