function [x] = Gauss_Seidel(A,b,x0,err,Maxiter)
    % Gauss-Seidel method
    % Ax = b
    % err is error
    % Maxiter is the maximum iteration times.
    D = diag(diag(A));%Find diagonal matrix of A
    L = -tril(A,-1);%Find lower triangular part of A
    U = -triu(A,1);%Find upper triangular part of A
    B = (D-L)\U; 
    f = (D-L)\b;
    x = B*x0+f; %x = bx+f
    iter = 0;
    while norm(x-x0, inf)>=err  % we use inf-norm 
        x0 = x;
        x = B*x0+f;
        iter = iter + 1;
        if(iter>=Maxiter)
            disp('Warning:Maximum number of iterations exceeded!')
            return;
        end
    end
end