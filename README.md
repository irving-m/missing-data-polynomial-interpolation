# missing-data-polynomial-interpolation-imputation
The code consists of two python users defined functions: lagrange, poly_fill. The latter uses the former within its body.
The Lagrange function is based on Lagrange's method of polynomial interpolation: it uses an arbitrary number of points (x,y) to find a unique polynomial that includes those points. After this, given an integer number, it calculates the polynomial value at that new point.
The poly_fill function loops through an entire pandas dataframe (preferably a time series), first by columns and then by rows.
If it finds an empty value, it starts creating two lists, one of the indices around the missing value, and another one of the actual values around the missing values. Since these two lists should be following the initial order of the pandas dataframe, they are equivalent to multiple pairs of values which can be used in the Lagrange function.
poly_fill loops through all rows, finds all missing data points (except those in the very begining and end) and imputes them with a Lagrange interpolation, given an integer that represents the number of points to be used for the interpolation. 
