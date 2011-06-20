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

import sys, os, subprocess
from itertools import ifilter as filtered, imap as mapped, ifilterfalse, chain

path = os.path.dirname(os.path.abspath(__file__))

langs = {
   "php": "PHP",
   "js": "JavaScript"
}

funcs = [
   [
      "partition",
      "stringfunc",
      [
         ["Hello world! How are you doing today?", " "],
         ["Hello world! How are you doing today?", ","],
         ["Hello world! How are you doing today?", ""]
      ]
   ],
   [
      "rpartition",
      "stringfunc",
      [
         ["Hello world! How are you doing today?", " "],
         ["Hello world! How are you doing today?", ","],
         ["Hello world! How are you doing today?", ""]
      ]
   ],
   [
      "startswith",
      "stringfunc",
      [
         ["abcdefgh", ""],
         ["abcdefgh", "abc"],
         ["abcdefgh", "a"],
         ["abcdefgh", "abcdefghi"],
         ["abcdefgh", "bcdefgh"]
      ]
   ],
   [
      "endswith",
      "stringfunc",
      [
         ["abcdefgh", ""],
         ["abcdefgh", "fgh"],
         ["abcdefgh", "h"],
         ["abcdefgh", "abcdefg"],
         ["abcdefgh", "abcdefghi"],
      ]
   ],
   [
      "rstrip",
      "stringfunc",
      [
         ["  Johann went to the store today.    "],
         ["Johann went to the store today.    "],
         ["   Johann went to the store today."],
         ["   Johann went to the store today.    \0"]
      ]
   ]
]

####


def itercat(*iterators):
    """Concatenate several iterators into one."""
    for i in iterators:
        for x in i:
            yield x

allfuncs = iter([]) # Find functions for which there are no tests

for lang in langs.keys():
   myfuncs = filtered(lambda x: not x.startswith("$"), os.listdir(os.path.join(path, lang, "src"))) # filter out $preamble, etc. 
   myfuncs = mapped(lambda x: x.rpartition(".")[0], myfuncs)
   allfuncs = itercat(myfuncs, allfuncs)

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

allfuncs = unique_everseen(allfuncs)

funcnames = [i[0] for i in funcs]
allfuncs = filtered(lambda fun: not fun in funcnames, allfuncs) # Filter out unsupported items

for unsupportedfunc in allfuncs:
   print "[!] No test for", unsupportedfunc


####

results = []

veryverbose_on = "-vv" in sys.argv[1:] or "--very-verbose" in sys.argv[1:]
verbose_on = "-v" in sys.argv[1:] or "--verbose" in sys.argv[1:] or veryverbose_on


def vp(*args):
   global verbose_on
   if verbose_on:
      print " ".join(map(str, args))

def vvp(*args):
   global veryverbose_on
   if veryverbose_on:
      print " ".join(map(str, args))

print "Building all..."
for x, y in langs.items():
   vp("Building "+y)
   subprocess.check_call([os.path.join(".", x, "build.py")])
   
for function, kind, tests in funcs:
   for test in tests:
      if kind == "stringfunc":
         string_obj = test[0]
         args = test[1:]
         success = True
         try:
            result = string_obj.__getattribute__(function)(*args)
         except:
            success = False
            result = None
      else:
         raise Exception("Unknown function type `%s`." % kind)
      test.append([success, result])
         
all_results = [] # list of all test results, for generating table in readme, etc.

for lang in langs.items():
   vp("\nBeginning unit tests on", lang[1])
   execfile(os.path.join(path,"_helpers",lang[0]+'.py'))

   thislangsresults = [lang[0], lang[1], {}]
   mysupport = thislangsresults[2] # This is a dict that will describe support of each function.
   all_results.append(thislangsresults)

   for function, kind, tests in funcs:

      num_tests = len(tests)
      num_passed = 0

      for test in tests:
         if isSupported(function):

            args = test[:-1]
            code = genTest(function, kind, args)
            result = genResult(code)

            passedTest = False

            expected = json.dumps(test[-1])

            try:
               actual = json.dumps(json.loads(result))
               passedTest = True
            except Exception:
               actual = "(parse fail)"
               print "Could not parse JSON Output of function "+function+"."
               vvp("\tJSON: "+result)

            if actual!=expected:
               passedTest = False
               vp(lang[1]+" failed test in "+function+".")
               vvp("\tExpected: "+expected+"\n\tActual: "+actual+"\n\tArgs: "+json.dumps(args))

            if passedTest:
               num_passed += 1

         else:
            vp(lang[1], "does not support", function+".", "Skipping.")

      mysupport[function] = [num_passed, num_tests] 

# Display overall results of the tests

print "\nTest results: "
allsuccess = True

for result in all_results:
   support = result[2]
   for func, fract in support.items():
      if fract[0] != fract[1]:
         allsuccess = False
         print result[0], func, "(", fract[0], "/", fract[1], ")"


if allsuccess:
   print "All tests successful."

execfile("_helpers/_gentable.py")
