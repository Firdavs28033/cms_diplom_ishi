#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2020 Firdavs28033

# Amiro.CMS version detection
# Rev 1

import cmseekdb.basic as cmseek
import re

def start(source):
    cmseek.statement('Detecting Amiro.CMS version using page source [Method 1 of 1]')
    regex = re.findall(r'_cv=(.*?)("|&|\')', source)[0]
    if regex != []:
        if regex[0] != '' and regex[0] != ' ':
            version = regex[0]
            cmseek.success('Amiro.CMS version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
            return version

    cmseek.error('Version detection failed!')
    return '0'