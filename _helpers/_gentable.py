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


# Support table generator

# This is meant to be called by /gentests.py

all_funcs = list(
               sorted(
                  unique_everseen(
                     itercat(*[i[2] for i in all_results])
                  ),
                  key = lambda x: x[::-1] # sort by the reverse of the function name.
                                          # this groups things like rpartition and partition
               )
            )

bigtable =  """<table>
   <caption>Supported Languages and Functions</caption>
   <thead>
         <tr>
            <td></td>"""

for x in all_funcs:
   bigtable += """
            <th>`%s`</th>""" % x


bigtable +=  """
         </tr>"""

print all_results

for x in all_results:
   bigtable += """
         <tr>"""
   bigtable += """
            <th>%s</th>""" % x[0]
   for y in all_funcs:
      print x[2][y][0],"vs",x[2][y][1]
      bigtable += """
            <td>%s</td>""" % ("&#10003;" if (x[2][y][0]==x[2][y][1]) else "&#10007;")
   bigtable += """
         </tr>"""

bigtable += """
   </thead>
</table>"""

print "Writing table to README..."

readmepath = os.path.join(path, "README.md")

readmeh = open(readmepath, "r") # readme handle (not read meh :P)
readme = readmeh.read()
readmeh.close()

readmeh = open(readmepath, "w") 
newreadme = "".join(readme.partition("<!-- begin chart -->")[:2])+bigtable+"".join(readme.rpartition("<!-- end chart -->")[1:])
readmeh.write(newreadme)
readmeh.close()
