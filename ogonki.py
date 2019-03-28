# -*- coding: utf-8 -*-
# skrypt naprawiający ogonki w plikach 'polecenie.md'
import argparse
import signal
import sys
import re

def ctr_c_handler(sig, frame):
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ctr_c_handler)

    parser = argparse.ArgumentParser(description='Naprawia ogonki w plikach z poleceniami')
    parser.add_argument('file', help='Plik do naprawy ogonkow', type=str)

    args = parser.parse_args()
    filename = args.file
    
    ogonki = {
        'a': 'ą',
        'e': 'ę'
    }

    ex = ' ˛[ae]'
    ext = filename.rfind('.')
    with open(filename, 'r', encoding="utf8") as f, open(f'{filename[:ext]}_ogonki.md', 'w', encoding="utf8") as fout: 
        for line in f:
            while True:
                m = re.search(ex, line)
                if m is None:
                    break
                
                i = m.start()
                line = line[:i] +  ogonki[line[i+2]] + line[m.end():]

            fout.write(line)


