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

function endswith($haystack, $needle) {
   $needlen = strlen($needle);
   if ($needlen === 0) {
      return TRUE;
   }
   $pos = strrpos($haystack, $needle);
   if ($pos === strlen($haystack) - $needlen) {
      return TRUE;
   }
   return FALSE;
}
