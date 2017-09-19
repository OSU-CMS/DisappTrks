#!/usr/bin/env python

from OSUT3Analysis.Configuration.Measurement import Measurement

#values and errors taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVx1x1wino and
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVn2x1wino

chargino_neutralino_cross_sections = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 22670.1 * 1.0e-3 ),
        'error' : str ( 973.967 * 1.0e-3 ),
    },
    '200' : {
        'value' : str ( 1807.39 * 1.0e-3 ),
        'error' : str ( 101.316 * 1.0e-3 ),
    },
    '300' : {
        'value' : str ( 386.936 * 1.0e-3 ),
        'error' : str ( 26.3602 * 1.0e-3 ),
    },
    '400' : {
        'value' : str ( 121.013 * 1.0e-3 ),
        'error' : str ( 9.61659 * 1.0e-3 ),
    },
    '500' : {
        'value' : str ( 46.3533 * 1.0e-3 ),
        'error' : str ( 4.16461 * 1.0e-3 ),
    },
    '600' : {
        'value' : str ( 20.1372 * 1.0e-3 ),
        'error' : str ( 2.04438 * 1.0e-3 ),
    },
    '700' : {
        'value' : str ( 9.51032 * 1.0e-3 ),
        'error' : str ( 1.04092 * 1.0e-3 ),
    },
    '800' : {
        'value' : str ( 4.75843 * 1.0e-3 ),
        'error' : str ( 0.564061 * 1.0e-3 ),
    },
    '900' : {
        'value' : str ( 2.49667 * 1.0e-3 ),
        'error' : str ( 0.314019 * 1.0e-3 ),
    },
}

chargino_chargino_cross_sections = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 11611.9 * 1.0e-3 ),
        'error' : str ( 518.613 * 1.0e-3 ),
    },
    '200' : {
        'value' : str ( 902.569 * 1.0e-3 ),
        'error' : str ( 53.7411 * 1.0e-3 ),
    },
    '300' : {
        'value' : str ( 190.159 * 1.0e-3 ),
        'error' : str ( 13.4438 * 1.0e-3 ),
    },
    '400' : {
        'value' : str ( 58.6311 * 1.0e-3 ),
        'error' : str ( 4.7276 * 1.0e-3 ),
    },
    '500' : {
        'value' : str ( 22.1265 * 1.0e-3 ),
        'error' : str ( 1.94904 * 1.0e-3 ),
    },
    '600' : {
        'value' : str ( 9.49913 * 1.0e-3 ),
        'error' : str ( 0.912324 * 1.0e-3 ),
    },
    '700' : {
        'value' : str ( 4.4387 * 1.0e-3 ),
        'error' : str ( 0.457123 * 1.0e-3 ),
    },
    '800' : {
        'value' : str ( 2.21197 * 1.0e-3 ),
        'error' : str ( 0.245196 * 1.0e-3 ),
    },
    '900' : {
        'value' : str ( 1.15301 * 1.0e-3 ),
        'error' : str ( 0.135822 * 1.0e-3 ),
    },
}

signal_cross_sections = {}

for mass in chargino_neutralino_cross_sections:
    cnX = chargino_neutralino_cross_sections[mass]
    ccX = chargino_chargino_cross_sections[mass]

    cn = Measurement (cnX['value'], cnX['error'])
    cc = Measurement (ccX['value'], ccX['error'])

    total = cn + cc

    # convert errors from absolute to relative
    chargino_neutralino_cross_sections[mass]['error'] = str (1.0 + (cn.uncertainty () / cn.centralValue ()))
    chargino_chargino_cross_sections[mass]['error'] = str (1.0 + (cc.uncertainty () / cc.centralValue ()))
    signal_cross_sections[mass] = {
        'value' : str (total.centralValue ()),
        'error' : str (1.0 + (total.uncertainty () / total.centralValue ())),
    }
