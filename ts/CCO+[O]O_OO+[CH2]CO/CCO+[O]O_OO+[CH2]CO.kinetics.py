#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('react_0', '/Users/nathan/Code/test_scratch/species/CCO/CCO.py', structure=SMILES('CCO'))
species('react_1', '/Users/nathan/Code/test_scratch/species/[O]O/[O]O.py', structure=SMILES('[O]O'))
species('prod_0', '/Users/nathan/Code/test_scratch/species/OO/OO.py', structure=SMILES('OO'))
species('prod_1', '/Users/nathan/Code/test_scratch/species/[CH2]CO/[CH2]CO.py', structure=SMILES('[CH2]CO'))
transitionState('TS', '/Users/nathan/Code/test_scratch/ts/CCO+[O]O_OO+[CH2]CO/CCO+[O]O_OO+[CH2]CO.py')

reaction(
    label = 'CCO+[O]O_OO+[CH2]CO',
    reactants = ['react_0', 'react_1'],
    products = ['prod_0', 'prod_1'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('CCO+[O]O_OO+[CH2]CO')
