#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
bisection.py: contains functions for bisection search
"""


# --- funcs ---
def bisection(func, xmin, xmax, tol=1e-4, maxit=50, *args):  # bisection function
    """Finds roots of a function using biection method

    bisection(func, xmin, xmax, tol = 1e-4, maxit = 50, *args):
    Finds roots of a function (func=0) using biection method
    Input:
    - func: an anonymous function
    - xmin, xmax: lower and upper limits of the interval
    - tol : error tolerance (%) (default = 0.0001%)
    - maxit: maximum number of iterations (default = 50)
    - *args: any extra arguments to func (optional)
    Output:
    - xr: the root
    - fx: value of func at the root
    - err: relative approximate error (%)
    - iter: number of iterations
    """

    small = 1e-20  # a small number
    f1 = func(xmin, *args)  # func value at xmin
    f2 = func(xmax, *args)  # func value at xmax
    if f1 * f2 > 0:  # chech the sign change between xmin and xmax
        print('Function does not change sign between xmin and xmax. Change the [xmin, xmax] interval')
        return
    elif f1 == 0:  # if f1=0, xmin is the root -> return f1
        iter = 0
        err = 0
        fx = 0
        return f1, fx, err, iter
    elif f2 == 0:  # if f2=0, xmax is the root -> return f2
        iter = 0
        err = 0
        fx = 0
        return f2, fx, err, iter

    iter = 0  # initial value of iteration count
    err = 1000  # initial value of relative approximate error (%)
    xl = xmin  # lower limit of the interval
    xu = xmax  # upper limit of the interval
    xr = xl  # set initial value for the root

    while err > tol and iter < maxit:  # while err is greater than the tolerance
        # and iter < maxit continue the loop
        iter = iter + 1  # increment iter
        xr_old = xr  # save the previous copy of xr for error calculation
        xr = 0.5 * (xl + xu)  # xr is midpoint between xl and xr
        err = abs((xr - xr_old) / (xr + small)) * 100  # relative approximate error (%)
        # (a small number is added to the
        # denominator to avoid /0 in case xr=0)

        f1 = func(xl, *args)  # func value at xl
        f2 = func(xr, *args)  # func value at xu
        ff = f1 * f2
        if ff < 0:
            xu = xr
        elif ff > 0:
            xl = xr
        else:
            err = 0  # if ff=0, xr is the root -> set err=0 to end the while loop

    root = xr
    fx = func(root, *args)
    if iter == maxit:  # show a warning if the function is terminated due to iter=maxit
        print('Warning: bisection function is terminated because iter=maxit;')
        print('         error < tolerance stopping criterion may not be satisfied')

    return xr, fx, err, iter  # returns xr, fx, err, iter
