function yi=Newtons_inter(x,y,xi)
% Newtons interpolation
% input data (X,Y)
n = length(x);
Y = zeros(n);
Y(:,1) = y';
for k=1:n-1
    for i=1:n-k
    Y(i,k+1)=(Y(i+1,k)-Y(i,k))/(x(i+k)-x(i));
    end
end
m = length(xi);
yi = zeros(1,m);

for j=1:m
    for i=1:n
        z = 1;
        for k=1:i-1
            z = z*(xi(j)-x(k));
        end
        yi(j) = yi(j)+Y(1,i)*z;
    end
end
end

