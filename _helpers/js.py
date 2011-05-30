# JavaScript Unit Test Helper

# This is meant to be called by /gentests.py

import json

library = open(os.path.join(path, lang[0], "dist", "pumpkinpy.js"), "r").read()

def isSupported(func):
   return os.path.isfile(os.path.join(path, lang[0], "src", func+".js"))

def genTest(func, kind, args):
   if kind == "stringfunc":
      return """
      var success = true;
      var result;
      try {
         result = %s.%s(%s);
      } catch(e) {
         success = false;
         result = null;
      }
      print(JSON.stringify([success, result]))
      """ % (json.dumps(args[0]), func, ", ".join(map(json.dumps, args[1:])))
   else:
      raise Exception("Unknown (by JS tester) function type `%s`." % kind)

def genResult(code):
   code = library+code
   p = subprocess.Popen(["js", "-e", code], stdout = subprocess.PIPE)
   p.wait()
   return p.stdout.read()
