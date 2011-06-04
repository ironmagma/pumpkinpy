/*

Legal boring crap follows. In simple english, you can use this
code in your own project, be your project commercial or free.
Just be sure to include the license and stuff. The "copyright"
here is just for technical reasons.

Copyright 2011, Philip Peterson.

This file is part of Pumpkinpy.

Pumpkinpy is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pumpkinpy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pumpkinpy.  If not, see <http://www.gnu.org/licenses/>.

*/

String.prototype.partition = function (needle) {

   var nedlen = needle.length;

   if (nedlen === 0) {
      throw new ValueError("empty separator");
   }

   var haystack = this;
   var nedpos = haystack.indexOf(needle);
   var before, after;

   if (nedpos !== -1) {
      before = haystack.substring(0, nedpos);
      after = haystack.substring(nedpos+nedlen);
   } else {
      before = haystack;
      needle = "";
      after = "";
   }

   return [before, needle, after];
};
