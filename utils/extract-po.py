#!/usr/bin/env python

import io
import sys 


def extract_translations():
    """ Extract translation for updateiconcache. """

    with io.open(sys.argv[1]) as orig_po, \
         io.open(sys.argv[2], 'w+', newline='\n') as new_po:

        lines = []
        relevant = True

        for line in orig_po.readlines():
            lines.append(line)

            if line.strip() == '':
                if relevant:
                    relevant = False
                    for wline in lines:
                        new_po.write(wline)
                lines = []
                continue

            if line.startswith('#:'):
                if 'gtk/updateiconcache.c' in line:
                    relevant = True

        if relevant:
            for wline in lines:
                new_po.write(wline)


if __name__ == '__main__':
    extract_translations()
