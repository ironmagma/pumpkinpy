String.prototype.partition = function(needle) {
   var haystack = this;
   var nedpos = haystack.indexOf(needle);
   var nedlen = needle.length;
   var before, after;

   if (nedpos !== -1) {
      before = haystack.substring(0, nedpos);
      after = haystack.substring(nedpos+nedlen)
   } else {
      before = haystack;
      needle = "";
      after = "";
   }

   return [before, needle, after];
};
