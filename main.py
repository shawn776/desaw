"""
Main handler for program
"""
#some module
import json,os,sys
#Main
class handler():
    def CommandExecute(self,command,**param):
        try:
            os.system("python lipro/%s.py %s" % (command,param))
            return True
        except:
            print('Command Not Found !')
            return False

handler = handler()
print('\t\t\tWelcome to main terminal!')
#Terminal loop for excute command
if __name__ == "__main__":
    while True:
        Command = input('')
        handler.CommandExecute(Command)
