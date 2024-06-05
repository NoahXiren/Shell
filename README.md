# shell

A shell is a user interface that provides access to an operating system's services. It allows users to interact with the operating system's kernel and execute commands.
This is a basic shell made from python that supports common file system operations.

## Features

- `echo [text]` or `print [text]`: Prints the specified text.
- `pwd`: Displays the current directory.
- `cd [directory]`: Changes to the specified directory.
- `ls [directory]`: Lists files in the specified directory (or current directory if none is specified), with an index.
- `mkdir [directory]`: Creates a new directory.
- `rm [file]`: Removes the specified file.
- `rmdir [directory]`: Removes the specified empty directory.
- `check`: checks whether the file is in the current directory and whether it is executable or not.
- `help`: Displays available commands and their usage.
- `quit` or `exit`: Exits the shell.

## Example

```bash
$ echo Hello, World!
Hello, World!


$ pwd
/path/to/current/directory

$ ls
0: file1.txt
1: file2.txt
2: directory1

$ cd directory1

$ mkdir newdir

$ rm file1.txt

$ rmdir newdir

$ check new
found files:
 .\new.txt
.\new.txt - Executable: True


$ help
# Displays the help information

$ quit
# Exits the shell
```

## License

This project is licensed under the MIT [License](LICENSE).
