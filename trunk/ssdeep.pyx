cdef extern from "stdio.h": pass
cdef extern from "stdlib.h": pass
cdef extern from "string.h": pass
cdef extern from "errno.h": pass
cdef extern from "limits.h": pass
cdef extern from "sys/stat.h": pass
cdef extern from "unistd.h": pass
cdef extern from "ctype.h": pass
cdef extern from "inttypes.h": pass

cdef extern from "fuzzy.h":
    int fuzzy_compare(char *sig1, char *sig2)

cdef extern from *:
    char * fuzzy_hash(char *filename)
    char * fuzzy_hash_data(char *buf, int buf_len)

cdef extern from "Python.h":
    void Py_INCREF(object o)
    void Py_DECREF(object o)

class SsdeepException(Exception): pass

cdef class ssdeep:
    def __init__(self):
        pass

    def hash_file(self, filename):
        """hash_file(self, filename)

        compute the ssdeep fuzzy hash for the input filename. 
        returns a string with the hash value"""
        res = fuzzy_hash(filename)
        # Py_INCREF(res)
        if ' oops' in res:
            raise SsdeepException, res.replace(' oops', ' error')
        else: return res

    def hash_bytes(self, buf):
        """compute the ssdeep fuzzy hash for the data in the buffer"""
        cdef char* utext
        utext = buf
        res = fuzzy_hash_data(utext,len(buf))
        if ' oops' in res:
            raise SsdeepException, res,replace(' oops',' error')
        else: return res

    def compare(self, hash1, hash2):
        """compare(self, hash1, hash2)

        compare two ssdeep hashes to discover their similarities
        returns an integer 1-100 on the strength of the match. 0 means no match"""
        return fuzzy_compare(hash1, hash2)
