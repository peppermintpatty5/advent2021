#include <stdlib.h>
#include <string.h>

#include "layer.h"
#include "sort.h"

struct layer *parse_layers(FILE *in)
{
    struct layer *layers = NULL;

    while (true)
    {
        struct layer *l;
        char s[sizeof("off")];

        l = malloc(sizeof(*l));
        fscanf(in, "%s x=%li..%li,y=%li..%li,z=%li..%li",
               s, &l->x1, &l->x2, &l->y1, &l->y2, &l->z1, &l->z2);

        if (feof(in))
            break;
        else
        {
            l->on = strcmp(s, "on") == 0;
            l->x2++, l->y2++, l->z2++;
            l->next = layers;
            layers = l;
        }
    }

    return layers;
}

long solve(struct layer *layers)
{
    size_t i, j, k, n;
    struct layer *l;
    long *x_vals, *y_vals, *z_vals;

    /* count the number of layers */
    n = 0;
    for (l = layers; l != NULL; l = l->next)
        n++;

    x_vals = malloc(sizeof(*x_vals) * n * 2);
    y_vals = malloc(sizeof(*y_vals) * n * 2);
    z_vals = malloc(sizeof(*z_vals) * n * 2);

    for (l = layers, i = 0; l != NULL; l = l->next, i += 2)
    {
        x_vals[i] = l->x1, x_vals[i + 1] = l->x2;
        y_vals[i] = l->y1, y_vals[i + 1] = l->y2;
        z_vals[i] = l->z1, z_vals[i + 1] = l->z2;
    }

    size_t nx_vals = sort_unique(x_vals, n * 2);
    size_t ny_vals = sort_unique(y_vals, n * 2);
    size_t nz_vals = sort_unique(z_vals, n * 2);
    long count = 0;
    for (i = 0; i < nx_vals - 1; i++)
    {
        fprintf(stderr, "iteration %zu / %zu\n", i + 1, nx_vals - 1);
        for (j = 0; j < ny_vals - 1; j++)
        {
            for (k = 0; k < nz_vals - 1; k++)
            {
                long x = x_vals[i],
                     y = y_vals[j],
                     z = z_vals[k],
                     x2 = x_vals[i + 1],
                     y2 = y_vals[j + 1],
                     z2 = z_vals[k + 1];
                for (l = layers; l != NULL; l = l->next)
                {
                    if (l->x1 <= x && x < l->x2 &&
                        l->y1 <= y && y < l->y2 &&
                        l->z1 <= z && z < l->z2)
                    {
                        if (l->on)
                            count += (x2 - x) * (y2 - y) * (z2 - z);
                        break;
                    }
                }
            }
        }
    }

    return count;
}
