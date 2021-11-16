#! /usr/bin/python3

banner = r'''
#
# _____.___.              __       ___.            ___________         _____  ________  ____ ___  _________                        __                
# \__  |   | ____  __ ___/  |_ __ _\_ |__   ____   \__    ___/___     /     \ \_____  \|    |   \ \_   ___ \_______   ____ _____ _/  |_  ___________ 
#  /   |   |/  _ \|  |  \   __\  |  \ __ \_/ __ \    |    | /  _ \   /  \ /  \  _(__  <|    |   / /    \  \/\_  __ \_/ __ \\__  \\   __\/  _ \_  __ \
#  \____   (  <_> )  |  /|  | |  |  / \_\ \  ___/    |    |(  <_> ) /    Y    \/       \    |  /  \     \____|  | \/\  ___/ / __ \|  | (  <_> )  | \/
#  / ______|\____/|____/ |__| |____/|___  /\___  >   |____| \____/  \____|__  /______  /______/    \______  /|__|    \___  >____  /__|  \____/|__|   
#  \/                                   \/     \/                           \/       \/                   \/             \/     \/                   

'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/bitsbb01/YT_to_m3u/main/assets/moose_na.m3u')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/bitsbb01/YT_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
