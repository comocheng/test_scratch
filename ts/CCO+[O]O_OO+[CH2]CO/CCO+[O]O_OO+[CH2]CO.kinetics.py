#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
frequencyScaleFactor = 0.982
useHinderedRotors = False
useBondCorrections = False

species('react_0', '/scratch/harms.n/autotst-2.0-QMScratch/species/CCO/CCO.py', structure=SMILES('CCO'))
species('react_1', '/scratch/harms.n/autotst-2.0-QMScratch/species/[O]O/[O]O.py', structure=SMILES('[O]O'))
species('prod_0', '/scratch/harms.n/autotst-2.0-QMScratch/species/OO/OO.py', structure=SMILES('OO'))
species('prod_1', '/scratch/harms.n/autotst-2.0-QMScratch/species/[CH2]CO/[CH2]CO.py', structure=SMILES('[CH2]CO'))
transitionState('TS', '/scratch/harms.n/autotst-2.0-QMScratch/ts/CCO+[O]O_OO+[CH2]CO/CCO+[O]O_OO+[CH2]CO.py')

reaction(
    label = 'CCO+[O]O_OO+[CH2]CO',
    reactants = ['react_0', 'react_1'],
    products = ['prod_0', 'prod_1'],
    transitionState = 'TS',
    tunneling = 'Eckart',
)

statmech('TS')
kinetics('CCO+[O]O_OO+[CH2]CO')
