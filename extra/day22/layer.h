#ifndef __LAYER_H
#define __LAYER_H

#include <stdbool.h>
#include <stdio.h>

/**
 * Each layer specifies points in a three-dimensional cube which are all to be
 * turned on or off. The first layer is applied last and therefore has the
 * highest priority in determining which points are on or off at the end.
 */
struct layer
{
    struct layer *next;
    long x1, x2, y1, y2, z1, z2;
    bool on;
};

/**
 * Parse layers from input file stream. Input is assumed to be correctly
 * formatted.
 */
extern struct layer *parse_layers(FILE *in);

/**
 * Calculate how many points are on at the end.
 */
extern long solve(struct layer *layers);

#endif
