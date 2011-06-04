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
