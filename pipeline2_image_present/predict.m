content1 = load('valid/matrix/1.txt');
content2 = load('valid/matrix/2.txt');
content3 = load('valid/matrix/3.txt');
content4 = load('valid/matrix/4.txt');
content5 = load('valid/matrix/5.txt');
content6 = load('valid/matrix/6.txt');
content7 = load('valid/matrix/7.txt');
content8 = load('valid/matrix/8.txt');
content9 = load('valid/matrix/9.txt');
content10 = load('valid/matrix/10.txt');

% training inputs, X
X = [content1; content2; content3; content4; content5; content6; content7; content8; content9; content10];
% training labels, y
y = [ones(size(content1)(1), 1) * 1; ones(size(content2)(1), 1) * 2; ones(size(content3)(1), 1) * 3; ones(size(content4)(1), 1) * 4; ones(size(content5)(1), 1) * 5; ...
    ones(size(content6)(1), 1) * 6; ones(size(content7)(1), 1) * 7; ones(size(content8)(1), 1) * 8; ones(size(content9)(1), 1) * 9; ones(size(content10)(1), 1) * 10];



Theta_f = load('theta.txt');


% num = 10;

m = size(X, 1);

X = [ones(m, 1) X];
p = X * Theta_f';
[prob, p] = max(p, [], 2);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(p == y)) * 100);
