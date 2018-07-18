function[X] = Gauss_Jordan(A,b)
% AX = b;
% Input A and b, output solution X.
% The rank of A is dimension N and we have unique solution.
% Note: In this program we improve the Gauss_jordan algorithm.

%%  Augument
    N = length(A);
    if rank(A) < N
        fprintf('A is singular. no unique solution');
        return
    end
    X = zeros(N,1);
    M = [A b]; % Augmented matrix M.
    
%%  Transfer to Echelon Matrix via Row operation
    for i = 1:N
        M(i,:) = M(i,:)/M(i,i);
        for k=i+1:N
            temp=M(k,i)/M(i,i);
            M(k,:)=M(k,:)-temp*M(i,:);
        end 
    end

%%  Transfer to Diagonal Matrix。
    for i = N:-1:1
        for k = 1:i-1
            temp = M(k,i)/M(i,i);
            M(k,:) = M(k,:)-temp*M(i,:);
        end
    end
    
%%  Solution
    X = M(:,N+1);
end