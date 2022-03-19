import csv
import os
import re

if __name__ == '__main__':
    print('Wifi password exporter')
    print('Now exporting...')
    folder = os.path.join(os.getcwd(), 'wifipwchker')
    if not os.path.exists(folder):
        os.mkdir(folder)
    cmd = f'netsh wlan export profile folder="{folder}" key=clear'
    with os.popen(cmd) as f:
        f.read() #To ensure that the cmd is completed
    flist = os.listdir(folder)
    namePtrn = re.compile('<name>(.*?)<\/name>')
    pwdPtrn = re.compile('<keyMaterial>(.*?)<\/keyMaterial>')
    configs = list()
    for file in flist:
        fpath = os.path.join(folder, file)
        with open(fpath, 'r') as f:
            xml = f.read()
            name = namePtrn.search(xml)
            pwd = pwdPtrn.search(xml)
            if name and pwd:
                configs.append((name.group(1), pwd.group(1)))
        os.remove(fpath)
    os.rmdir(folder)
    output = os.path.join(os.getcwd(), 'WifiPasswordList.csv')
    with open(output, 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['SSID', 'Password'])
        writer.writerows(configs)
    print(f'Wifi password is exported to "{output}".')
    input('Press enter to exit...')
