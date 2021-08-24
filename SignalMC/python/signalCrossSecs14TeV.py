#!/usr/bin/env python

import math
from OSUT3Analysis.Configuration.Measurement import Measurement

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections14TeVn2x1wino
# not clear if this includes CTEQ6.6, or just MSTW2008nlo90cl ?
chargino_neutralino_cross_sections = {
    # values : [pb]
    # errors : % -- will be converted to 1.0 +/- (%/100)
    '100' : {
        'value'     : 25134. * 1.0e-3,
        'scaleDown' : -1.3,
        'pdfDown'   : -3.3,
        'scaleUp'   : 0.42,
        'pdfUp'     : 3.4,
    },
    '200' : {
        'value'     : 2059.6 * 1.0e-3,
        'scaleDown' : -0.56,
        'pdfDown'   : -3.7,
        'scaleUp'   : 0.26,
        'pdfUp'     : 3.7
    },
    '300' : {
        'value'     : 451.45  * 1.0e-3,
        'scaleDown' : -0.53,
        'pdfDown'   : -4.1,
        'scaleUp'   : 0.63,
        'pdfUp'     : 4.3,
    },
    '400' : {
        'value'     : 144.26 * 1.0e-3,
        'scaleDown' : -0.33,
        'pdfDown'   : -4.6,
        'scaleUp'   : 0.86,
        'pdfUp'     : 4.9,
    },
    '500' : {
        'value'     : 56.42 * 1.0e-3,
        'scaleDown' : -0.27,
        'pdfDown'   : -4.9,
        'scaleUp'   : 1.0,
        'pdfUp'     : 5.5,
    },
    '600' : {
        'value'     : 25.05 * 1.0e-3,
        'scaleDown' : -0.49,
        'pdfDown'   : -5.3,
        'scaleUp'   : 0.86,
        'pdfUp'     : 6.2,
    },
    '700' : {
        'value'     : 12.11 * 1.0e-3,
        'scaleDown' : -0.56,
        'pdfDown'   : -5.5,
        'scaleUp'   : 0.68,
        'pdfUp'     : 7.1,
    },
    '800' : {
        'value'     : 6.19 * 1.0e-3,
        'scaleDown' : -0.7,
        'pdfDown'   : -6.,
        'scaleUp'   : 0.96,
        'pdfUp'     : 7.9,
    },
    '900' : {
        'value'     : 3.3 * 1.0e-3,
        'scaleDown' : -0.65,
        'pdfDown'   : -6.4,
        'scaleUp'   : 0.89,
        'pdfUp'     : 8.6,
    },
    '1000' : {
        'value'     : 1.83 * 1.0e-3,
        'scaleDown' : -1.,
        'pdfDown'   : -7.4,
        'scaleUp'   : 0.77,
        'pdfUp'     : 9.4,
    },
    '1100' : {
        'value'     : 1.04 * 1.0e-3,
        'scaleDown' : -1.2,
        'pdfDown'   : -7.9,
        'scaleUp'   : 0.48,
        'pdfUp'     : 10.,
    },
}

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections14TeVx1x1wino
# not clear if this includes CTEQ6.6, or just MSTW2008nlo90cl ?
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
    '1000' : {
        'value' : str ( 0.621866 * 1.0e-3 ),
        'error' : str ( 0.0771005 * 1.0e-3 ),
    },
    '1100' : {
        'value' : str ( 0.342626 * 1.0e-3 ),
        'error' : str ( 0.0427672 * 1.0e-3 ),
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

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVn2x1hino
# multiply by two for degenerate N1/N2
higgsino_n2c1 = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 5325.95 * 1.0e-3 * 2 ),
        'error' : str ( 191.047 * 1.0e-3 * math.sqrt(2) ),
    },
    '200' : {
        'value' : str ( 424.166 * 1.0e-3 * 2 ),
        'error' : str ( 20.1252 * 1.0e-3 * math.sqrt(2) ),
    },
    '300' : {
        'value' : str ( 90.8167 * 1.0e-3 * 2 ),
        'error' : str ( 5.48175 * 1.0e-3 * math.sqrt(2) ),
    },
    '400' : {
        'value' : str ( 28.423  * 1.0e-3 * 2 ),
        'error' : str ( 2.08121 * 1.0e-3 * math.sqrt(2) ),
    },
    '500' : {
        'value' : str ( 10.8865  * 1.0e-3 * 2 ),
        'error' : str ( 0.923598 * 1.0e-3 * math.sqrt(2) ),
    },
    '600' : {
        'value' : str ( 4.73741  * 1.0e-3 * 2 ),
        'error' : str ( 0.454855 * 1.0e-3 * math.sqrt(2) ),
    },
    '700' : {
        'value' : str ( 2.23385  * 1.0e-3 * 2 ),
        'error' : str ( 0.233891 * 1.0e-3 * math.sqrt(2) ),
    },
    '800' : {
        'value' : str ( 1.12392  * 1.0e-3 * 2 ),
        'error' : str ( 0.130506 * 1.0e-3 * math.sqrt(2) ),
    },
    '900' : {
        'value' : str ( 0.58695   * 1.0e-3 * 2 ),
        'error' : str ( 0.0707011 * 1.0e-3 * math.sqrt(2) ),
    },
}

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVx1x1hino
higgsino_c1c1 = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 2883.67 * 1.0e-3 ),
        'error' : str ( 126.968 * 1.0e-3 ),
    },
    '200' : {
        'value' : str ( 244.321 * 1.0e-3 ),
        'error' : str ( 13.8982 * 1.0e-3 ),
    },
    '300' : {
        'value' : str ( 52.569 * 1.0e-3 ),
        'error' : str ( 3.5507 * 1.0e-3 ),
    },
    '400' : {
        'value' : str ( 16.3405 * 1.0e-3 ),
        'error' : str ( 1.26734 * 1.0e-3 ),
    },
    '500' : {
        'value' : str ( 6.21625  * 1.0e-3 ),
        'error' : str ( 0.543279 * 1.0e-3 ),
    },
    '600' : {
        'value' : str ( 2.68388  * 1.0e-3 ),
        'error' : str ( 0.255607 * 1.0e-3 ),
    },
    '700' : {
        'value' : str ( 1.25981  * 1.0e-3 ),
        'error' : str ( 0.13226 * 1.0e-3 ),
    },
    '800' : {
        'value' : str ( 0.630966  * 1.0e-3 ),
        'error' : str ( 0.0708789 * 1.0e-3 ),
    },
    '900' : {
        'value' : str ( 0.328529  * 1.0e-3 ),
        'error' : str ( 0.0403214 * 1.0e-3 ),
    },
}

signal_cross_sections_higgsino = {}

for mass in higgsino_n2c1:
    cn = Measurement (higgsino_n2c1[mass]['value'], higgsino_n2c1[mass]['error'])
    cc = Measurement (higgsino_c1c1[mass]['value'], higgsino_c1c1[mass]['error'])

    total = cn + cc

    # convert errors from absolute to relative
    higgsino_n2c1[mass]['error'] = str (1.0 + (cn.uncertainty () / cn.centralValue ()))
    higgsino_c1c1[mass]['error'] = str (1.0 + (cc.uncertainty () / cc.centralValue ()))
    signal_cross_sections_higgsino[mass] = {
        'value' : str (total.centralValue ()),
        'error' : str (1.0 + (total.uncertainty () / total.centralValue ())),
    }
