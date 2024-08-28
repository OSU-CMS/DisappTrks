#!/usr/bin/env python3

import math
from OSUT3Analysis.Configuration.Measurement import Measurement

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13x6TeVn2x1wino
# aNNLO+NNLL in Resummino https://arxiv.org/pdf/2304.11915
chargino_neutralino_cross_sections = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 24917.2 * 1.0e-3 ),
        'error' : str ( 740.936 * 1.0e-3 ),
    },
    '200' : {
        'value' : str ( 2016.0 * 1.0e-3 ),
        'error' : str ( 58.733 * 1.0e-3 ),
    },
    '300' : {
        'value' : str ( 436.634  * 1.0e-3 ),
        'error' : str ( 15.3975 * 1.0e-3 ),
    },
    '400' : {
        'value' : str ( 137.834 * 1.0e-3 ),
        'error' : str ( 5.84063 * 1.0e-3 ),
    },
    '500' : {
        'value' : str ( 53.2405 * 1.0e-3 ),
        'error' : str ( 2.64758 * 1.0e-3 ),
    },
    '600' : {
        'value' : str ( 23.3072 * 1.0e-3 ),
        'error' : str ( 1.34653 * 1.0e-3 ),
    },
    '700' : {
        'value' : str ( 11.1063 * 1.0e-3 ),
        'error' : str ( 0.743621 * 1.0e-3 ),
    },
    '800' : {
        'value' : str ( 5.62384 * 1.0e-3 ),
        'error' : str ( 0.438769 * 1.0e-3 ),
    },
    '900' : {
        'value' : str ( 2.9798 * 1.0e-3 ),
        'error' : str ( 0.272676 * 1.0e-3 ),
    },
    '1000' : {
        'value' : str ( 1.63418 * 1.0e-3 ),
        'error' : str ( 0.177529 * 1.0e-3 ),
    },
    '1100' : {
        'value' : str ( 0.921113 * 1.0e-3 ),
        'error' : str ( 0.119926 * 1.0e-3 ),
    },
    '1200' : {
        'value' : str ( 0.53052 * 1.0e-3 ),
        'error' : str ( 0.0842752 * 1.0e-3 ),
    },
}

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13x6TeVn2x1wino
# aNNLO+NNLL in Resummino https://arxiv.org/pdf/2304.11915
chargino_chargino_cross_sections = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 12838.1 * 1.0e-3 ),
        'error' : str ( 513.923 * 1.0e-3 ),
    },
    '200' : {
        'value' : str ( 1012.26 * 1.0e-3 ),
        'error' : str ( 35.4766 * 1.0e-3 ),
    },
    '300' : {
        'value' : str ( 215.458  * 1.0e-3 ),
        'error' : str ( 8.75624 * 1.0e-3 ),
    },
    '400' : {
        'value' : str ( 66.9628 * 1.0e-3 ),
        'error' : str ( 3.23204 * 1.0e-3 ),
    },
    '500' : {
        'value' : str ( 25.4927 * 1.0e-3 ),
        'error' : str ( 1.44275 * 1.0e-3 ),
    },
    '600' : {
        'value' : str ( 11.0143 * 1.0e-3 ),
        'error' : str ( 0.725663 * 1.0e-3 ),
    },
    '700' : {
        'value' : str ( 5.18784 * 1.0e-3 ),
        'error' : str ( 0.398582 * 1.0e-3 ),
    },
    '800' : {
        'value' : str ( 2.6006 * 1.0e-3 ),
        'error' : str ( 0.234445 * 1.0e-3 ),
    },
    '900' : {
        'value' : str ( 1.36707 * 1.0e-3 ),
        'error' : str ( 0.145547 * 1.0e-3 ),
    },
    '1000' : {
        'value' : str ( 0.745121 * 1.0e-3 ),
        'error' : str ( 0.0948022 * 1.0e-3 ),
    },
    '1100' : {
        'value' : str ( 0.418273 * 1.0e-3 ),
        'error' : str ( 0.0643228 * 1.0e-3 ),
    },
    '1200' : {
        'value' : str ( 0.240557 * 1.0e-3 ),
        'error' : str ( 0.0450304 * 1.0e-3 ),
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

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13x6TeVhinosplit
# aNNLO+NNLL in Resummino https://arxiv.org/pdf/2304.11915
# multiply by two for degenerate N1/N2
higgsino_n2c1 = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 6229.35 * 1.0e-3 * 2 ),
        'error' : str ( 185.265 * 1.0e-3 * math.sqrt(2) ),
    },
    '200' : {
        'value' : str ( 504.02 * 1.0e-3 * 2 ),
        'error' : str ( 14.683 * 1.0e-3 * math.sqrt(2) ),
    },
    '300' : {
        'value' : str ( 109.167 * 1.0e-3 * 2 ),
        'error' : str ( 3.84871 * 1.0e-3 * math.sqrt(2) ),
    },
    '400' : {
        'value' : str ( 34.4632 * 1.0e-3 * 2 ),
        'error' : str ( 1.46005 * 1.0e-3 * math.sqrt(2) ),
    },
    '500' : {
        'value' : str ( 13.3129 * 1.0e-3 * 2 ),
        'error' : str ( 0.661957 * 1.0e-3 * math.sqrt(2) ),
    },
    '600' : {
        'value' : str ( 5.82839 * 1.0e-3 * 2 ),
        'error' : str ( 0.336897 * 1.0e-3 * math.sqrt(2) ),
    },
    '700' : {
        'value' : str ( 2.77757 * 1.0e-3 * 2 ),
        'error' : str ( 0.185965 * 1.0e-3 * math.sqrt(2) ),
    },
    '800' : {
        'value' : str ( 1.4066 * 1.0e-3 * 2 ),
        'error' : str ( 0.109758 * 1.0e-3 * math.sqrt(2) ),
    },
    '900' : {
        'value' : str ( 0.745364 * 1.0e-3 * 2 ),
        'error' : str ( 0.0682122 * 1.0e-3 * math.sqrt(2) ),
    },
    '1000' : {
        'value' : str ( 0.40882 * 1.0e-3 * 2 ),
        'error' : str ( 0.0444191 * 1.0e-3 * math.sqrt(2) ),
    },
}

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13x6TeVhinosplit
# aNNLO+NNLL in Resummino https://arxiv.org/pdf/2304.11915
higgsino_c1c1 = {
    # values and errors are in pb; errors are absolute, converted to relative below
    '100' : {
        'value' : str ( 3328.8 * 1.0e-3 ),
        'error' : str ( 129.701 * 1.0e-3 ),
    },
    '200' : {
        'value' : str ( 282.34 * 1.0e-3 ),
        'error' : str ( 9.78659 * 1.0e-3 ),
    },
    '300' : {
        'value' : str ( 61.2041 * 1.0e-3 ),
        'error' : str ( 2.45521 * 1.0e-3 ),
    },
    '400' : {
        'value' : str ( 19.1958 * 1.0e-3 ),
        'error' : str ( 0.914351 * 1.0e-3 ),
    },
    '500' : {
        'value' : str ( 7.35264 * 1.0e-3 ),
        'error' : str ( 0.412511 * 1.0e-3 ),
    },
    '600' : {
        'value' : str ( 3.19172 * 1.0e-3 ),
        'error' : str ( 0.209581 * 1.0e-3 ),
    },
    '700' : {
        'value' : str ( 1.50946 * 1.0e-3 ),
        'error' : str ( 0.116121 * 1.0e-3 ),
    },
    '800' : {
        'value' : str ( 0.759528 * 1.0e-3 ),
        'error' : str ( 0.0688722 * 1.0e-3 ),
    },
    '900' : {
        'value' : str ( 0.400664 * 1.0e-3 ),
        'error' : str ( 0.0432108 * 1.0e-3 ),
    },
    '1000' : {
        'value' : str ( 0.219273 * 1.0e-3 ),
        'error' : str ( 0.0285098 * 1.0e-3 ),
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
