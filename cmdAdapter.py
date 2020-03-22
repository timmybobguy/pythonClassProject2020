async def adapter_cmdloop(self, intro=None):
    """Repeatedly issue a prompt, accept input, parse an initial prefix
    off the received input, and dispatch to action methods, passing them
    the remainder of the line as argument.

    """
    self.preloop()

    # This is the same code as the Python 3.7.2 Cmd class, with the
    # following changes
    #  - Remove dead code caused by forcing use_rawinput=False.
    #  - Added a await in front of readline()
    if intro is not None:
        self.intro = intro
    if self.intro:
        self.stdout.write(str(self.intro) + "\n")
    stop = None
    while not stop:
        if self.cmdqueue:
            line = self.cmdqueue.pop(0)
        else:
            self.stdout.write(self.prompt)
            self.stdout.flush()
            line = await self._read_command_line(self.prompt)
            if not len(line):
                line = 'EOF'
            else:
                line = line.rstrip('\r\n')
        line = self.precmd(line)
        stop = self.onecmd(line)
        stop = self.postcmd(stop, line)
    self.postloop()
