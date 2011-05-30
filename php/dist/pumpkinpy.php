<?php

class ValueError extends Exception {
   public function __construct($message, $code = 0, Exception $previous = null) {
      parent::__construct($message, $code, $previous);
   }
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

function partition($haystack, $needle) {
   $nedlen = strlen($needle);
   if ($nedlen === 0) {
      throw new ValueError("empty separator");
   }

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

function startswith($haystack, $needle) {
   $needlen = strlen($needle);
   if ($needlen === 0) {
      return TRUE;
   }
   $pos = strrpos($haystack, $needle);
   if ($pos === 0) {
      return TRUE;
   }
   return FALSE;
}
