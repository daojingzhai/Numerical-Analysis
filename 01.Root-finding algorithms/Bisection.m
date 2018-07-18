function [root] = Bisection(x_min,x_max,func,err,Maxiter) 
    % Bisection method.
    % input function as func.
    % err is maximum allowed error.
    % Maxiter is allowed iteration number.
    if func(x_min)==0 
        root = x_min;
    end
    if func(x_max)==0 
        root = x_max;
    end
    iter = 1;
    while(func(x_min)*func(x_max)<0) && (x_max-x_min>err) && (iter<Maxiter)
        x_temp = (x_max + x_min)/2;
        iter = iter+1;
        if(func(x_temp)==0) 
            root = x_temp;
        end
        if(func(x_max)*func(x_temp)<0) 
            x_min = x_temp;
        else
            x_max = x_temp;
        end
    end
    
    if(iter>=Maxiter)
        disp('Warning:Maximum number of iterations exceeded!')
        return;
    end
    fprintf('root: %10f\n', x_temp);
end

