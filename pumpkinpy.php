<?php

function partition($haystack, $needle) {
   $nedlen = strlen($needle);
   $nedpos = strpos($haystack, $needle);

   if ($nedpos !== FALSE) {
      $before = substr($haystack, 0, $nedpos);
      $after = substr($haystack, $nedpos+$nedlen);
   } else {
      $before = $haystack;
      $needle = "";
      $after = "";
   }

   return array($before, $needle, $after);
}

function rpartition($haystack, $needle) {
   $nedlen = strlen($needle);
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

