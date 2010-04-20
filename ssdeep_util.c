#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <sys/stat.h>
#include <unistd.h>
#include <ctype.h>
#include <inttypes.h>

#include "fuzzy.h"

char *
fuzzy_hash(char *filename) {
        FILE *input;
        int i;
        char *hash;

        hash = (char *)malloc(FUZZY_MAX_RESULT);
        if (NULL == hash)
                return("malloc oops");
        input = fopen(filename, "rb");
        if (NULL == input)
                return("fopen oops");
        i = fuzzy_hash_file(input, hash);
        fclose(input);
        if (0 == i)
                return(hash);
        else
                return("fuzzy_hash_file oops");
}

char *
fuzzy_hash_data(char *buf, uint32_t buf_len) {
        char *hash;
        int i;

        hash = (char *)malloc(FUZZY_MAX_RESULT);
        if (NULL == hash)
                return ("malloc oops");

        i = fuzzy_hash_buf((unsigned char *)buf, buf_len,hash);
        if (0 == i)
                return (hash);
        else
                return ("fuzzy_hash_data oops");
}
