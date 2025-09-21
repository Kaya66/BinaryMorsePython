# Binary-Morse-Converter

Binary More Encode/Decode



<h2>Project Explination</h2>


in morse, you can write out any standard letters and numbers with a max of 5 dots or dashes.

in binary we have 8 digits that are addrssable in a byte.

split up a byte into 5 and 3.   00000 / 000

the 3 on the right tell you how many digits on the left you need to pay attention to.

The letter C written out in this method would be 01010100    01010 / 100

0 = dash / 1 = dot

the three digits on the right read out 4 so you read the 5 on the left starting left to right.  and read the first 4.

-.-.  = C

any trailing zero's past what you need to pay attention to can be safely ignored.

