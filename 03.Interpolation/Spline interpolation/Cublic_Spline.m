function y=Cublic_Spline(X,Y,x,s1,s2)
% Cublic Spline Interpolation algorithm
% imput samples (X,Y)
% s1 ans s2 is derivatives of the first and last point
% x is the plot interval

n=length(Y);
h = zeros(n-1,1);
for i=1:n-1
    h(i)=X(i+1)-X(i);
end
A=[Y,zeros(n,n-1)];
for i=2:n
    for j=2:i
        A(i,j)=(A(i,j-1)-A(i-1,j-1))/(X(i)-X(i-j+1));
    end
end
u=zeros(n,1);
v=zeros(n,1);
d=zeros(n,1);
for i=2:n-1
    u(i)=h(i-1)/(h(i-1)+h(i));
    v(i)=h(i)/(h(i-1)+h(i));
    d(i)=6*A(i+1,3);
end
u(n)=1;
v(1)=1;
d(1)=6/h(1)*(A(2,2)-s1);
d(n)=6/h(n-1)*(s2-A(n,2));
B = 2*eye(n)+[[zeros(n-1,1),diag(v(1:n-1))];zeros(1,n)]+[zeros(1,n);[diag(u(2:n)),zeros(n-1,1)]];
m = B\d;
xn=length(x);
y=zeros(xn,1);
for i=1:xn
    for j=1:n
        if X(j)<=x(i) && x(i)<=X(j+1)
            y(i)=m(j)*(X(j+1)-x(i))^3/(6*h(j)) ...
               + m(j+1)*(x(i)-X(j))^3/(6*h(j)) ...
            + (Y(j)-m(j)*h(j)^2/6)*(X(j+1)-x(i))/h(j) ...
            + (Y(j+1)-m(j+1)*h(j)^2/6)*(x(i)-X(j))/h(j);
            break;
        end
    end
end
end


