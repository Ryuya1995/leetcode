import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn import linear_model


def poly_regression(x, y):
    # x,y: numpy array

    # x =x.reshape(-1,1)
    poly = PolynomialFeatures(degree=3)
    x = poly.fit_transform(x)  # eg,x= [x1,x2] -> [1,x1,x2,x1x1,x1x2,x2x2]
    clf = linear_model.LinearRegression(fit_intercept=False)
    clf.fit(x, y)
    regress_coefs = clf.coef_

    # model = Pipeline([('poly', PolynomialFeatures(degree=3)),
    #                   ('linear', LinearRegression(fit_intercept=False))])
    # model = model.fit(x[:, np.newaxis], y)
    # regress_coefs = model.named_steps['linear'].coef_
    # regress_intercept = model.named_steps['linear'].intercept_

    # print(clf.predict(x))
    # print(y)
    print('残差平方和: %.2f' % np.mean((clf.predict(x) - y) ** 2))
    return regress_coefs


# x = np.arange(5)
# y = 3 - 2 * x + x ** 2 - x ** 3
if __name__ == '__main__':
    x = np.arange(20).reshape(10,2)
    y = 3 - 2 * x[:,0] + x[:,1]

    print(poly_regression(x, y))
