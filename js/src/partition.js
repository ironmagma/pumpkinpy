function partition(haystack, needle) {
   var nedpos = haystack.indexOf(needle);
   var nedlen = needle.length;
   var before, after;

   if (nedpos !== -1) {
      before = haystack.substring(0, nedpos);
      after = haystack.substirng(nedpos+nedlen)
   } else {
      before = haystack;
      needle = "";
      after = "";
   }

   return [before, needle, after];
}
