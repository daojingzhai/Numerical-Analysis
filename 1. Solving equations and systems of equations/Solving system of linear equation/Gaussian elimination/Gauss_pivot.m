function[X] = Gauss_pivot(A,b)
% AX = b;
% Input A and b, output solution X.
% The rank of A is dimension N and we have unique solution.
% Note: there are two main limitation for Gauss-Jordan Elimination
% 1. The progrom will fail when a_kk(k-1)~=0;
% 2. The program will fail when a_kk(k-1)<<1;
% Later on, I will use another Elimination method: Elimination with Maximal
% Column Pivoting.
%%  Augument
    N = length(A);
    if rank(A) < N
        fprintf('A is singular. no unique solution');
        return
    end
    X = zeros(N,1);
    M = [A b]; % Augmented matrix M.
    
%%  Transfer to Echelon Matrix via Row operation
%   In each loop, we will seek the largest element in the working column
%   and swap its row to the pivot. 
    for i = 1:N
        pivot = i-1 + find(M(i:N,i)==max(M(i:N,i))); 
        % find the largest element in the ith column, from ith row to Nth
        % row. Its index is pivot.
        M([i,pivot(1)],:) = M([pivot(1),i],:);
        % swap the pivot with the ith row
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