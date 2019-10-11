%%

% Y1= ((X1)^0)b0 + ((X1)^1)b1 + ((X1)^2)b2 + ... + ((X1)^k)bk 
% Y2= ((X2)^0)b0 + ((X2)^1)b1 + ((X2)^2)b2 + ... + ((X2)^k)bk 
% .
% .
% .
% Yn= ((Xn)^0)b0 + ((Xn)^1)b1 + ((Xn)^2)b2 + ... + ((Xn)^k)bk 

% Y = |y1|
%     |y2|
%     |. |
%     |. |
%     |. |
%     |yn|

% X = |(X1)^0,(X1)^1, ...,(X1)^k|
%     |(X2)^0,(X2)^1, ...,(X2)^k|
%     .
%     .
%     . 
%     |(Xn)^0,(Xn)^1, ...,(Xn)^k|

% B = |b1|
%     |b2|
%     |. |
%     |. |
%     |. |
%     |bk|

% E = |e1|
%     |e2|
%     |. |
%     |. |
%     |. |
%     |en|

%%
% Y = XB + E
%%
%Deseja-se encontrar o vetor de estimativas dos quadrados mínimos,
% que minimize a função-custo:
%%
%Importa os dados
A = importdata('aerogerador.dat');

%Gera os vetores 'x' e 'y', com os dados limpos
x = A(:, 1);
y = A(:, 2);

format long
%%

n = size(A);
n = n(1);

X = cat(2, ones(n, 1), x, x.^2);

B = ((inv((X')*X))*((X')*y));
Y = X*B;
my = mean(y);
SQe = 0;
Syy = 0;
var = 1;
while var <= n
    SQe = (y(var) - Y(var)) ^ 2;
    Syy = (y(var) - my) ^ 2;
    var = var + 1;
end

R2 = 1 - (SQe / Syy);

scatter(x,y);
hold on
plot(x,Y);
xlabel('Velocidade do Vento - M/S')
ylabel('Potência Gerada - KWatts')
title('Regressão Entre Velocidade e Potência')
grid on
legend('Dados','Regressão Grau 2','Location','southeast');
