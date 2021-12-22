#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "sort.h"

struct layer
{
    struct layer *next;
    long x1, x2, y1, y2, z1, z2;
    bool on;
};

int main(void)
{
    struct layer *layers = NULL, *l;
    size_t n_layers = 0, i, j, k;
    long *x_vals, *y_vals, *z_vals;

    while (true)
    {
        char s[sizeof("off")];

        l = malloc(sizeof(*l));
        fscanf(stdin, "%s x=%li..%li,y=%li..%li,z=%li..%li",
               s, &l->x1, &l->x2, &l->y1, &l->y2, &l->z1, &l->z2);

        if (feof(stdin))
            break;
        else
        {
            l->on = strcmp(s, "on") == 0;
            l->x2++, l->y2++, l->z2++;

            l->next = layers;
            layers = l;
            n_layers++;
        }
    }

    x_vals = malloc(sizeof(*x_vals) * n_layers * 2);
    y_vals = malloc(sizeof(*y_vals) * n_layers * 2);
    z_vals = malloc(sizeof(*z_vals) * n_layers * 2);

    for (l = layers, i = 0; l != NULL; l = l->next, i += 2)
    {
        x_vals[i] = l->x1, x_vals[i + 1] = l->x2;
        y_vals[i] = l->y1, y_vals[i + 1] = l->y2;
        z_vals[i] = l->z1, z_vals[i + 1] = l->z2;
    }

    size_t nx_vals = sort_unique(x_vals, n_layers * 2);
    size_t ny_vals = sort_unique(y_vals, n_layers * 2);
    size_t nz_vals = sort_unique(z_vals, n_layers * 2);
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
    fprintf(stdout, "%li\n", count);

    return EXIT_SUCCESS;
}
