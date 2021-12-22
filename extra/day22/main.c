#include <stdio.h>
#include <stdlib.h>

#include "layer.h"

int main(void)
{
    fprintf(stdout, "%li\n", solve(parse_layers(stdin)));

    return EXIT_SUCCESS;
}
