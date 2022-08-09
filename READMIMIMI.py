import sys
import subprocess 

def proverka(password, klient_password):
    if klient_password == password:
        print('доступ получен')
        sys.exit()
    elif klient_password != password:
        print('в доступе отклонен')
        subprocess.run('calc', shell=True)
        proverka(password, klient_password)
proverka('fff', input())