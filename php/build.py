from glob import glob
import os, re

path = os.path.dirname(os.path.abspath(__file__))

def readfiletrim(fpath):
   h = open(fpath, "r")
   c = h.read()
   h.close()

   c = re.sub(c, "^<\?php\s*", "", re.IGNORECASE)
   c = c.strip()

   return c

allcontents = []

for x in glob(os.path.join(path, "src", "*.php")):
   allcontents.append(readfiletrim(x))

if not os.path.isdir(os.path.join(path, "dist")):
   os.mkdir(os.path.join(path, "dist"))

h = open(os.path.join(path, "dist", "pumpkinpy.php"), "w")
h.write("\n\n".join(allcontents)+"\n")
h.close()
