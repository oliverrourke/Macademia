#include "mex.h"
#include <stdio.h>

void mexFunction( int nlhs, mxArray *plhs[],
                  int nrhs, const mxArray *prhs[] )
{
  double *x,*y;

  /* Create matrix for the return argument. */

  
  /* Assign pointers to each input and output. */
  x = mxGetPr(prhs[0]);
  plhs[0] = mxCreateDoubleMatrix(x[1],1, mxREAL);
  y = mxGetPr(plhs[0]);
  y[0] = x[0];
  int i = 1;
    for(i = 1;i<x[1];i++){
  y[i] = x[2]*y[i-1]*(1.0-y[i-1]);
    }
  
}