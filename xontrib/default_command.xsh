@events.on_transform_command
def default_command_transform(cmd):
    """Run a default command when no command is given"""
    if not cmd or cmd.strip() == "":
        return defaultcmd()
    return cmd

def defaultcmd():
    newcmd = "ls"
    if p'$PWD/.git'.exists():
        newcmd += " && git status -sb"
    return newcmd
