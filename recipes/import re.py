#!/usr/bin/env python3
################################################################################
# File: import re.py                                                           #
# Author: John Calderaio                                                       #
# Project: Automate The Boring Stuff With Python                               #
# Created Date: 03-10-2022                                                     #
# -----                                                                        #
# Last Modified: 03-10-2022                                                    #
# Modified By: Johnny                                                          #
################################################################################
import re


def onlyAlphaNumeric(text):
    temp_str = re.sub(f"[^a-zA-Z0-9]", "", text).lower()
    print(temp_str)
    return temp_str == temp_str[::-1]


print(onlyAlphaNumeric("ab_a"))
