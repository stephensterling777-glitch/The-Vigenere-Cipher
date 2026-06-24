# The-Vigenere-Cipher

All the ciphers we've studied before have been what are called substitution cipher. That is, b might be encrypted as a, c could be x, and so on. One letter for one letter. However, in the 16th century, a man named Blaise de Vigenère upgraded the substitution ciphers to make them polyalphabetic. Here, c could be encrypted as either a or x or any other letter depending on it's position in the message. We do this by taking a key that is multiple letters long and consecutively applying it each letter in the message by shifting it.


For example, suppose our message is 'hello,' and our key is the word 'dog.' Applying the key would look like:

D  O  G  D  O  
H  E  L  L  O

Recall that d corresponds to 3, o to 14, and g to 6 since those are their positions in the alphabet (we start with a = 0). Thus, when we apply our key, we get ksroc. That is, 3 letters away from h is k. 14 letters away from e is s.  6 letters away from l is r, and so forth. Decryption is as easy as applying the additive inverse of the key. In the case of 'dog,' it would be 'xmu.' Here, 'x' is the inverse of 'd', 'm' is the inverse of 'o', and 'u' is the inverse of 'g.'

## How the Program Works:
1. User is asked to enter a message and then a key.
2. The program encrypts by default. To decrypt, change encrypt to decrypt inside the print function at the bottom.

