Brian Lee
brianslee@umail.ucsb.edu
3620101

Explanation of code:(Partial credit please?)
So, what I attempted to do with my code was to create three lists of int values of the characters in the ciphertext. One was the original ciphertext, the second was a work list which would have its values manipulated, and the last was the solution list which would hold the correct values.
From there, I would change every byte from the last byte of the second-to-last block to the first byte. I set a target value which stated which byte it was from the back of the block. For example, the last byte of the block would have a target value of 1 while the first byte of the block would have a target value of 16.
Then, I would begin making guesses from 0 to 255, and xor that guess with the original value of the ciphertext byte and the target, ie guess xor ciphertext[x] xor target. The result of that would be placed in the corresponding location in the temp work list. After that, I would try to see if the guess was valid, changing the values of subsequent bytes in the block to match the target, plaintext[x] xor ciphertext[x] xor target. Then, I'd convert the list into ciphertext and run it through the PadOracle function. If it returned True, the value at temp[x] would be placed in a guess list.
Once all guesses had been checked, I'l try to verify which guess was the correct one. I'd do this by changing the receding byte to a different value and restoring the values of the current byte of the temp and the subsequent bytes in the block to the values used in the first check. The one that remained valid after this check was placed in the corresponding location in the solution list.
This would go on until every byte in the range was processed.

I'm not entirely certain if my method was correct. If it was, I'm not certain where my implementation went wrong. This is simply my interpretation of how a padding oracle attack was supposed to work. given that the issue seems to be that my guess list is empty, there is either a problem with my first attempt at verifying correct guesses or a problem in how I obtain those guesses in the first place. This code is the one from lines 76 - 95. If it turns out to be the verification code, then my second verification method may also be incorrect as the code I used was similar.

I understand I will not be getting full credit for this portion, but I'm hoping that this explanation and analysis will mitigate the points loss to a certain extent. Thank you for your time and patience.
