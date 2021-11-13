# xontrib-default-command

This [Oh-My-Xonsh][omx] plugin for the [xonsh] shell runs a default command when you
press return on an empty command line.

By default, this command will run `ls`. If `$PWD` is a git project, it will also
run a short git status with `git status -s`.

## Customizing

You can redefine the `defaultcmd` function in your [rc.xsh] to do whatever you want.

For example, if you want a detailed `ls` and `git status`, you could do this instead:

```python
def defaultcmd():
    """Run a detailed ls and git status when no other command given"""
    newcmd = "ls -laFG"
    if p'$PWD/.git'.exists():
        newcmd += " && git status"
    return newcmd
```

## Installation

Install from PyPI via `xpip`:

```shell
xpip install xontrib-default-command
# or: xpip install -U git+https://github.com/oh-my-xonsh/xontrib-default-command
```

Then, add this to your [rc.xsh]:

```shell
xontrib load default-command
```

## Similar projects

- Zsh has an [auto-ls plugin](https://github.com/desyncr/auto-ls)


[xonsh]: https://xon.sh
[omx]: https://github.com/oh-my-xonsh
[rc.xsh]: https://xon.sh/xonshrc.html
