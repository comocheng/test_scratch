# Coordinates for react_0 in Input Orientation (angstroms):
#   O    1.5619    0.4296   -0.0987
#   C    0.4882   -0.4734    0.1054
#   C    1.0584   -1.8732    0.0965
#   H   -0.0070   -0.2763    1.0618
#   H   -0.2611   -0.3690   -0.6862
#   H    1.7976   -1.9813    0.8889
#   H    0.2709   -2.6106    0.2486
#   H    1.5459   -2.0727   -0.8566
#   H    1.2216    1.3261   -0.0956
conformer(
    label = 'react_0',
    E0 = (-239.521, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(46.0419, 'amu')),
        NonlinearRotor(
            inertia = ([14.3001, 53.3929, 61.397], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([227.889, 266.207, 413.947, 810.27, 903.702, 1032.11, 1119.72, 1165.88, 1250.11, 1286.91, 1378.11, 1436.92, 1460.51, 1478.29, 1511.34, 2967.28, 2997.57, 3016.25, 3091.49, 3093.59, 3832.21], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Coordinates for react_1 in Input Orientation (angstroms):
#   O   -0.1575    0.4433    0.0000
#   O    0.9987   -0.1701   -0.0000
#   H   -0.8281   -0.2603    0.0000
conformer(
    label = 'react_1',
    E0 = (7.52053, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(32.9977, 'amu')),
        NonlinearRotor(
            inertia = ([0.804493, 14.573, 15.3775], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(frequencies=([1233, 1433.88, 3632.29], 'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Coordinates for prod_0 in Input Orientation (angstroms):
#   O   -0.5406    0.4672    0.0511
#   O    0.5723   -0.4202    0.0170
#   H   -1.2762   -0.1504   -0.0233
#   H    0.9166   -0.3250    0.9117
conformer(
    label = 'prod_0',
    E0 = (-132.965, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(34.0055, 'amu')),
        NonlinearRotor(
            inertia = ([1.64463, 18.4879, 19.0908], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(
            frequencies = ([374.421, 1027.92, 1332.22, 1441.04, 3776.44, 3778.22], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Coordinates for prod_1 in Input Orientation (angstroms):
#   O   -1.2475   -0.1762    0.9368
#   C   -0.2061   -0.5102    0.0372
#   C    0.3477   -1.8262    0.4184
#   H   -0.5714   -0.5417   -0.9979
#   H    0.5841    0.2576    0.0652
#   H    1.0041   -2.3563   -0.2529
#   H    0.2199   -2.1755    1.4306
#   H   -1.5499    0.7131    0.7435
conformer(
    label = 'prod_1',
    E0 = (-33.0914, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(45.034, 'amu')),
        NonlinearRotor(
            inertia = ([12.501, 49.8992, 58.9605], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([107.355, 262.35, 381.335, 439.664, 863.801, 955.505, 1054.55, 1129.3, 1213.43, 1251.5, 1400.48, 1447.29, 1480.84, 2895.33, 2946.29, 3129.48, 3240.8, 3831.89], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

