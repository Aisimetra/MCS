%function [x, err, timerVal] = solve_linear(matrix)
    
function [x, err, timerVal, memory_in_mb] = solve_linear(matrix)

    %INPUT:
    %matrix = name of the matrix
    
    %OUPUT:
    %x = solution of the system
    %err = relative error
    %memory_in_mb = memory in mb to solve the linear system

    %Load sparse matrix
    matrix = load(matrix);
    A = matrix.Problem.A;
    %spy(A);
    
    %Exact solution
    matrix_size = size(A);
    xe = ones(matrix_size(1), 1);

    %Compute value of b
    b = A * xe;
    
    %Start calculating time and memory
    tic;
   
    %Solve linear system
    x = A\b;
    
    [user,~] = memory;
    timerVal = toc;

    %1 MB = 1048576 Bytes
    memory_in_mb = user.MemUsedMATLAB / 1048576;
    
    %Relative error
    err = norm(x - xe, 2) / norm(xe, 2);
    
end