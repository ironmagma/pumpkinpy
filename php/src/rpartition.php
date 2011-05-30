<?php

function rpartition($haystack, $needle) {
   $nedlen = strlen($needle);

   if ($nedlen === 0) {
      throw new ValueError("empty separator");
   }

   $nedpos = strrpos($haystack, $needle);
    
   if ($nedpos !== FALSE) {
      $before = substr($haystack, 0, $nedpos);
      $after = substr($haystack, $nedpos+$nedlen);
   } else {
      $before = "";
      $needle = "";
      $after = $haystack;
   }
    
   return array($before, $needle, $after);
}
