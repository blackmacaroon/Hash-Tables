import bcrypt
import hashlib


#hashes have to be deterministic, pseudo random. 
        # for a given input, the output will always be the same
        # an output should always be the same size in the same range
        # predictable speed, no matter what you're hashing
        # not invertable - can't go backwards - for cryptography 