#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'O': 2,
    'H': 1,
}

bonds = {
    'O-O': 1,
    'O-H': 1,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('[O]O.log'),
}

geometry = Log('[O]O.log')

frequencies = Log('[O]O.log')

rotors = [
]
