/* signed-min cross kernel: given X (n points) and signs s per triple (in the
   fixed combinations(n,3) order), return min over triples of s*cross.
   Also a variant that fills the pool (indices with s*cross <= thresh). */
#include <math.h>

double smin_cross(const double *xy, int n, const signed char *s) {
    double mn = 1e300;
    int t = 0;
    for (int i = 0; i < n - 2; i++) {
        double xi = xy[2*i], yi = xy[2*i+1];
        for (int j = i + 1; j < n - 1; j++) {
            double dx1 = xy[2*j] - xi, dy1 = xy[2*j+1] - yi;
            for (int k = j + 1; k < n; k++, t++) {
                double c = dx1 * (xy[2*k+1] - yi) - (xy[2*k] - xi) * dy1;
                double v = s[t] * c;
                if (v < mn) mn = v;
            }
        }
    }
    return mn;
}

int pool_fill(const double *xy, int n, const signed char *s, double thresh,
              int *out, int max_out) {
    int t = 0, cnt = 0;
    for (int i = 0; i < n - 2; i++) {
        double xi = xy[2*i], yi = xy[2*i+1];
        for (int j = i + 1; j < n - 1; j++) {
            double dx1 = xy[2*j] - xi, dy1 = xy[2*j+1] - yi;
            for (int k = j + 1; k < n; k++, t++) {
                double c = dx1 * (xy[2*k+1] - yi) - (xy[2*k] - xi) * dy1;
                if (s[t] * c <= thresh) {
                    if (cnt < max_out) out[cnt] = t;
                    cnt++;
                }
            }
        }
    }
    return cnt;
}
