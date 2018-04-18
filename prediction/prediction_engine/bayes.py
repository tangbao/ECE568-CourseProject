from os import cpu_count

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

from prediction_engine.get_data import get_long_term_data


class Bayes(object):

    @staticmethod
    def predict(X: np.ndarray, y: np.ndarray, x: np.ndarray):
        pipe = make_pipeline(
            StandardScaler(),
            PolynomialFeatures(7),
            BayesianRidge(normalize=False)
        )  # type: Pipeline

        grid_search = GridSearchCV(
            pipe,
            param_grid={
                'polynomialfeatures__degree': list(range(40))
            },
            n_jobs=cpu_count(),
            verbose=3
        )

        pipe.fit(X, y)

        return pipe.predict(x)


if __name__ == '__main__':
    x, y = get_long_term_data('GOOG')

    plt.plot(x, y, 'r-')
    plt.plot(x, Bayes.predict(x, y, x), 'b-')

    plt.show()

    # print(Bayes.predict(x, y, x))
