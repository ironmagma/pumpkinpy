import sys, os, subprocess

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
   ]
]

results = []

veryverbose_on = "-vv" in sys.argv[1:] or "--very-verbose" in sys.argv[1:]
verbose_on = "-v" in sys.argv[1:] or "--verbose" in sys.argv[1:] or veryverbose_on

path = os.path.dirname(os.path.abspath(__file__))

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
         
for lang in langs.items():
   vp("\nBeginning unit tests on", lang[1])
   execfile(os.path.join(path,"_helpers",lang[0]+'.py'))
   for function, kind, tests in funcs:
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

         else:
            vp(lang[1], "does not support", function+".", "Skipping.")
