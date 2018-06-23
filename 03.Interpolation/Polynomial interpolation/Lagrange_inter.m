function y=Lagrange_inter(X,Y,x)
% Lagrange interpolation
% Data (X,Y)
m=length(X);
n=length(x);
for i=1:n
    v=1;
    s=0;
    for k=1:m
        p=1;
        for j =1:m
            if j~=k
                p=p*(x(i)-X(j))/(X(k)-X(j));
            end
        end
        s=p*Y(k)+s;
    end
    y(i)=s;
end
end
