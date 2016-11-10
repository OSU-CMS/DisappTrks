#!/usr/bin/env python

import os

def getUser():
    dirs = {}
    cwd = os.getcwd()
    if "wulsin" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = ""
        user = "wulsin"
    elif "hart" in cwd:
        dirs['Andrew'] = ""
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = "wellsCondor/"
        user = "hart"
    elif "bfrancis" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = ""
        dirs['Wells']  = "wellsCondor/"
        user = "bfrancis"
    else:
        print "Error:  could not identify user as brancis, hart, or wulsin."
        os.exit(0)
    return dirs
