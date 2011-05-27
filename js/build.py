from glob import glob
import os

path = os.path.dirname(os.path.abspath(__file__))

def readfiletrim(fpath):
   h = open(fpath, "r")
   c = h.read().strip()
   h.close()
   return c

allcontents = []

for x in glob(os.path.join(path, "src", "*.js")):
   allcontents.append(readfiletrim(x))

if not os.path.isdir(os.path.join(path, "dist")):
   os.mkdir(os.path.join(path, "dist"))

h = open(os.path.join(path, "dist", "pumpkinpy.js"), "w")
h.write("\n\n".join(allcontents)+"\n")
h.close()
