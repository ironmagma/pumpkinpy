#!/usr/bin/env python
from glob import glob
import os, re

path = os.path.dirname(os.path.abspath(__file__))

def readfiletrim(fpath):
   h = open(fpath, "r")
   c = h.read()
   h.close()

   c = re.sub("^<\?php\s*", "", c, re.IGNORECASE)
   c = c.strip()

   return c

allcontents = []

for x in sorted(glob(os.path.join(path, "src", "*.php"))):
   allcontents.append(readfiletrim(x))

if not os.path.isdir(os.path.join(path, "dist")):
   os.mkdir(os.path.join(path, "dist"))

h = open(os.path.join(path, "dist", "pumpkinpy.php"), "w")
h.write("<?php\n\n"+"\n\n".join(allcontents)+"\n")
h.close()

