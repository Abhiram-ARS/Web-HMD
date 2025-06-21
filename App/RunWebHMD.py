import art

print('=================================================================================')
print(art.text2art("Web-HMD", font="slant"),end='')
print("      Website Hashing for Modification Detection ")
print('=================================================================================\n\n')

enter=input("Press Enter to Launch")

from Backend.Launcher import Launcher

Launcher.launch()


