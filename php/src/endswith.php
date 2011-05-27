<?php

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
