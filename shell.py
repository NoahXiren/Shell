# libraries
import os
import subprocess


# class
class Shell:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            command = input("$ ")

            if command.lower() in ['quit', 'exit']:
                self.running = False
            else:
                self.working_commands(command)


    def working_commands(self,command):
        commands = self.Parse_Command(command)
        if  not commands:
            return
        
        cmd = commands[0]
        args =  commands[1:]

        
        # echo/print – prints any text after the echo/print
        if cmd == "echo" or cmd =="print":
            print(' '.join(args))
        

        # pwd – displays all the files in the current directory
        elif cmd == "pwd":
            print(os.getcwd())  


        # cd – moves to the specified directory
        elif cmd == "cd":
            if len(args) == 0:
                print('cd: MIssing Arguments')
            else:
                try:
                    os.chdir(args[0])
                except FileNotFoundError:
                    print(f'cd: no such file or directory in your computer: {args[0]}')
        

        # list files of directory
        elif cmd == "ls":
            try:
                directory = args[0] if args else '.'
                files = os.listdir(directory)
                for  index, file in enumerate(files):
                    print(f'{index}: {file}')

            except FileNotFoundError:
                print(f'ls: cannot access {args[0]}: sorry..  no such file in the directory or no directory')
            except NotADirectoryError:
                print(f'ls: cannot access {args[0]}: sorry.. that is not a directory')


        # make new directory
        elif cmd == "mkdir":
            try:
                os.mkdir(args[0])
            except IndexError:
                print('mkdir: Missing Arguments')
            except FileExistsError:
                print(f'mkdir: sorry cannot create {args[0]}: file exists')


        # remove  a file
        elif cmd == "rm":
            try:
                os.remove(args[0])
            except IndexError:
                print('rm: Missing Arguments')
            except FileNotFoundError:
                print(f'rm: cannot remove {args[0]}: no such file exits')
            except IsADirectoryError:
                print(f'rm: cannot remove {args[0]}: It  is a directory')

        # removing a directory
        elif cmd == "rmdir":
            try:
                os.rmdir(args[0])
            except IndexError:
                print('rmdir: Missing Arguments')
            except NotADirectoryError:
                print(f'rmdir: cannot remove {args[0]}: not a directory')

        # HELP COMMAND
        elif cmd == "help":
            self.print_help()

    
        # open a file from another directory without changing current directory
        elif cmd == 'open':  
            if len(args) == 0:
                print('open: Missing Arguments')
            else:
                filepath = args[0]
                try: 
                    with open(filepath, 'r') as file:
                        desc = file.read()
                        print(desc)
                except FileNotFoundError:
                    print(f'open: file not found: {filepath}')
                except IsADirectoryError:
                    print(f'open: {filepath} is a directory')
                except IOError as e:
                    print(f'open: IOError occurred - {e}')
            

        # run a file from your current directory
        elif cmd =='run':
            
            if len(args) == 0:
                print('run: Missing Arguments')
            else:
                filepath = args[0]
                try:
                    if os.path.isfile(filepath) and os.access(filepath, os.X_OK):
                        subprocess.run(['python', filepath])
                except FileNotFoundError:
                    print(f'run: file not found: {args[0]}')
                except Exception as e:
                    print(f'ERROR: error has occurred while running the file: {e}')               

        
        # run a file by giving its location 
        elif cmd =='run-local':
            if len(args) == 0:
                print('run-local: Missing Arguments')
            else:
                try:
                    subprocess.run(['python', args[0]])
                except FileNotFoundError:
                    print(f'run-local: file not found: {args[0]}')
                except Exception as e:
                    print(f"An error occurred while running the file: {e}")


        # checking if the given file is executable or not
        elif cmd == "executable":
            try:
                self.check_file_executable(args[0])
            except FileNotFoundError:
                print('cexe: file not found')
            except IsADirectoryError:
                print('cexe: is a directory')
            except Exception as e:
                print(f"An error occurred: {e}")


        # in the case of command not found(unknown command)
        else:
            print(f'{cmd}: command not found')

    

    # check_file is executable or not
    def check_file_executable(self, filepath):
        if os.path.isfile(filepath) and os.access(filepath, os.X_OK):
            print(f"the file '{filepath}' is executable")
        elif os.path.isfile(filepath):
            print(f" The file '{filepath}' is executable")
        else:
            print(f"the file '{filepath}' is not executable")

        
    # splits command string into list of components
    def Parse_Command(self, command):
        components = []
        component = ''
        in_quotes = False

        for char in command:
            if char == '"':
                in_quotes = not in_quotes

            elif char == ' ' and not in_quotes:
                if component:
                    components.append(component)
                    component = ''

            else:
                component += char

                
        if component:
            components.append(component)

        return components
    

    # print help command
    def print_help(self):
        print("""
    Commands that are available:
        echo/print [text] - prints text
        pwd - displays the current directory(path)
        cd [directory] - changes to the specified directory
        ls [directory] - list of files in the directory
        mkdir [directory] - creates a new directory
        rm [file] - Removes file
        rmdir [directory] removes an empty directory
        cexe [file] - checks if the file is executable
        open [file] - open a file from another directory without changing current
        run [file] - runs a python file from the current directory
        help - displays the information(this one the one you are reading)
        quit/exit - exits the program
              """)
        

if __name__ == "__main__":
    shell = Shell()
    shell.run()