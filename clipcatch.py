
"""
jaspreetpanesar | 2022-12-03

While running, stores new clipboard entries in memory
to be ouput on termination.

output to file with -o switch, or using >
    py clipcatch.py > outputfile.txt

"""

import sys 
import time
from argparse import ArgumentParser
import pyperclip

c_DESCRIPTION = ""
c_HELPTEXT_OUTFILE = ""
c_HELPTEXT_POLLRATE = ""

class ClipTracker(object):

    def __init__(self, pollrate=0.1):
        self._store = []
        self.result = ""
        self.poll = pollrate

    def run(self):
        try:
            prevc = pyperclip.paste()
            while 1:
                time.sleep(self.poll)
                newc = pyperclip.paste()
                if prevc != newc:
                    self._store.append(newc)
                    prevc = newc
        except KeyboardInterrupt:
            pass
        self.resolve()

    def resolve(self):
        # TODO format if needed
        self.result = "\n".join(self._store)


def main(args):
    ct = ClipTracker()
    ct.run()
    if args.outfile is not None:
        # TODO check for existing/overriding
        raise NotImplemented
    else:
        print(ct.result)

def parse(args):
    agp = ArgumentParser(c_DESCRIPTION)
    agp.add_argument("--outfile", "-o", type=str, help=c_HELPTEXT_OUTFILE)
    agp.add_argument("--polling-rate", type=float, help=c_HELPTEXT_POLLRATE)
    return agp.parse_args(args)

if __name__ == "__main__":
    main(parse(sys.argv[1:]))

