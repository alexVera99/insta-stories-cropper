from ftplib import error_reply
import subprocess

from numpy import outer

class BashExecutor:
    def __init__(self) -> None:
        pass
    
    def executeCommand(self, command: str):
        '''
        Executes the bash command contained in the command variable.
        
        INPUTS
        command: it contains a functioning bash command. Example: "ls ."
        '''
        bashCmd = command.split(" ")
        
        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = process.communicate()
        
        output = output.decode()
        
        if error != None:
            error = error.decode()
        
        return (output, error)
    
def main():
    bash_code_executor = BashExecutor()
    output, error = bash_code_executor.executeCommand("ls fda")
    
    print(output, error)
    
if __name__ == '__main__':
    main()