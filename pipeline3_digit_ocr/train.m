clear ; close all; clc

matrix = load('training/matrix/data_processed.txt');
window = load('training/window/data_processed.txt');

% training inputs, X
X = matrix;
% training labels, y
y = window;

% training size
m = size(X, 1);

% example for y = 0
% label = 0;
% y0 = y;
% y0(y0 == label) = 100;
% y0(y0 != 100) = 101;
% y0(y0 == 100) = 0;
% y0(y0 == 101) = 1;
% Theta0 = zeros(size(X)(2) + 1, 1);


% lambda
lambda = 0.5;

% calculate cost
% [J grad] = cost(Theta0, X, y0, lambda);
% n = size(X, 2);
% initial_theta = zeros(n + 1, 1);

n = size(X, 2);

X = [ones(m, 1) X];
% options = optimset('GradObj', 'on', 'MaxIter', 100);
% disp('^#');
% disp(size(X));
% disp(size((y0)));
% disp(size(lambda));
% disp(size(Theta0));
% disp(size(options));
% disp('$#');
% Theta0_f = fmincg(@(t)(cost(t, X, y0, lambda)), Theta0, options);
num_labels = 10;

Theta_f = zeros(num_labels, n + 1);

% disp(J);
% disp(size(Theta0_f));
for iter = 1:num_labels
  initial_theta = zeros(n + 1, 1);
  options = optimset('GradObj', 'on', 'MaxIter', 200);
  Theta_i = fmincg(@(t)(cost(t, X, (y == iter), lambda)), initial_theta, options);
  Theta_f(iter, :) = Theta_i;
end

fid = fopen('theta.txt', 'w+');
for i=1:size(Theta_f, 1)
    fprintf(fid, '%f ', Theta_f(i,:));
    fprintf(fid, '\n');
end
fclose(fid);

% disp(size(Theta_f));
