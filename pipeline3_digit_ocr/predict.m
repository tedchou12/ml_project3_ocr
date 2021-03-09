matrix = load('training/matrix/data_processed.txt');
window = load('training/window/data_processed.txt');

% training inputs, X
X = matrix;
% training labels, y
y = window;


Theta_f = load('theta.txt');


% num = 10;

m = size(X, 1);

X = [ones(m, 1) X];
p = X * Theta_f';
[prob, p] = max(p, [], 2);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(p == y)) * 100);
