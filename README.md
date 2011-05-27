pumpkinpy
=========

`pumpkinpy` is a project to create ports of Python's standard library functions to other languages.

The reasoning for this is that Python's standard library contains a lot of very nifty functions, particularly
for string processing. This project does not mean or attempt to port the entirety of Python's functionality;
it only attempts to implement the most useful functions, and attempts to do so as faithfully as possible within
the constraints of the language of implementation.

Presently, support is as follows:

<!-- begin chart -->

<table>
   <caption>Supported Languages and Functions</caption>
   <thead>
      <tr>
         <td></td>
         <th>`partition`</th>
         <th>`rpartition`</th>
         <th>`startswith`</th>
         <th>`endswith`</th>
      </tr>
      <tr>
         <th>js</th>
         <td>&#10003;</td>
         <td>&#10007;</td>
         <td>&#10007;</td>
         <td>&#10007;</td>
      </tr>
      <tr>
         <th>php</th>
         <td>&#10003;</td>
         <td>&#10003;</td>
         <td>&#10003;</td>
         <td>&#10003;</td>
      </tr>
   </thead>
</table>

<!-- end chart -->
