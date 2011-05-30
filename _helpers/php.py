# PHP Unit Test Helper

# This is meant to be called by /gentests.py
import json

library = open(os.path.join(path, lang[0], "dist", "pumpkinpy.php"), "r").read()

def isSupported(func):
   return os.path.isfile(os.path.join(path, lang[0], "src", func+".php"))

def genTest(func, kind, args):
   if kind == "stringfunc":
      return library+""" 
      $success = true;

      try {
         $result = %s(%s);
      }
      catch (Exception $e) {
         $result = null;
         $success = false;
      }

      echo(json_encode(array($success, $result)));
      
      """ % (func, ", ".join(map(json.dumps, args)))
   else:
      raise Exception("Unknown (by PHP tester) function type `%s`." % kind)



def genResult(code):
   p = subprocess.Popen(["php"], stdout = subprocess.PIPE, stdin = subprocess.PIPE)
   p.stdin.write(code)
   p.stdin.close()
   p.wait()
   return p.stdout.read()
