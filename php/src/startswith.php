<?php

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
