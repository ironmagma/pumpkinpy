<?php

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

/*

function rpartition(haystack, needle) {
   nedlen = strlen(needle);
   nedpos = strrpos(haystack, needle);
    
   if (nedpos !== FALSE) {
      before = substr(haystack, 0, nedpos);
      after = substr(haystack, nedpos+nedlen);
   } else {
      before = "";
      needle = "";
      after = haystack;
   }
    
   return array(before, needle, after);
}

function endswith(haystack, needle) {
   needlen = strlen(needle);
   if (needlen === 0) {
      return TRUE;
   }
   pos = strrpos(haystack, needle);
   if (pos === strlen(haystack) - needlen) {
      return TRUE;
   }
   return FALSE;
}


function startswith(haystack, needle) {
   needlen = strlen(needle);
   if (needlen === 0) {
      return TRUE;
   }
   pos = strrpos(haystack, needle);
   if (pos === 0) {
      return TRUE;
   }
   return FALSE;
}

*/
