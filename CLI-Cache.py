import cmd


# This is a simple command-line interface (CLI) cache example using the cmd
#  module in Python.
class SimpleShell(cmd.Cmd):
    prompt = '> '
    intro = "Welcome to the Simple Shell! Type help or ? to list commands."

    def do_greet(self, name):
        """Greet the user by name."""
        print(f"Hello, {name}!")

    def do_exit(self, _):
        """Exit the shell."""
        print("Goodbye!")
        return True


if __name__ == '__main__':
    SimpleShell().cmdloop()
