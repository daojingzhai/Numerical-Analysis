function [root] = Fixed_point_iteration(x0,func,err,Maxiter)  
% Fixed point iteration method
% iteration start from x0, err is allowed error.
% Maxiter is the number of maximum iterations.
    root = func(x0); 
    iter = 1;
    while(abs(root-func(root)>=err)||iter<Maxiter)
        root = func(root);
        iter = iter+1;
    end
    if(iter>=Maxiter)
        disp('Warning:Maximum number of iterations exceeded!')
        return;
    end
end  