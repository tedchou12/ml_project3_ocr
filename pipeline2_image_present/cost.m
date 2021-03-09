function [J, grad] = cost(theta, X, y, lambda)

  m = size(X, 1);

  Theta0 = theta;

  Theta0_reg = Theta0;
  Theta0_reg(1) = 0;

  z = sigmoid(X * Theta0);
  temp = sum((-y .* log(z)) - ((1 - y) .* log(1 - z)));
  J = temp / m + ((lambda / (2 * m)) * sum(Theta0_reg .^ 2));
  grad = sum((z - y) .* X) / m + ((lambda / m) .* Theta0_reg');

  grad = grad(:);

end
