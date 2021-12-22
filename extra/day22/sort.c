#include <stdlib.h>

#include "sort.h"

/**
 * Comparator function for long integers.
 */
static int longcmp(const void *a, const void *b);

size_t sort_unique(long *array, size_t n)
{
    size_t i, j;

    qsort(array, n, sizeof(*array), longcmp);

    for (i = 1, j = 0; i < n; i++)
    {
        if (array[i] != array[j])
            array[++j] = array[i];
    }

    return j + 1;
}

int longcmp(const void *a, const void *b)
{
    long la = *(long *)a;
    long lb = *(long *)b;

    return la > lb ? 1 : (la < lb ? -1 : 0);
}
