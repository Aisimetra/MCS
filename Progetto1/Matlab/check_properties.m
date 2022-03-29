%Properties for each matrix
function [prop] = check_properties(matrix)
    mat = load(matrix);
    A = mat.Problem.A;
    
	prop = {isdiag(A)};
    prop(end + 1) = {istriu(A)};
    prop(end + 1) = {istril(A)};
    prop(end + 1) = {ishermitian(A)};
    prop(end + 1) = {isbanded(A, 1, 1)};
    prop(end + 1) = {isreal(A)};
    
    
end