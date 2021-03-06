# Legal boring crap follows. In simple english, you can use this
# code in your own project, be your project commercial or free.
# Just be sure to include the license and stuff. The "copyright"
# here is just for technical reasons.
#
# Copyright 2011, Philip Peterson.
#
# This file is part of Pumpkinpy.
# 
# Pumpkinpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Pumpkinpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Pumpkinpy.  If not, see <http://www.gnu.org/licenses/>.



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
