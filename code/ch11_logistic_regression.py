"""Chapter 11, going further: a logistic regression of cancellation on member features."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

m = pd.read_csv("../data/quokka_members.csv")
formula = ("cancelled ~ C(contract) + C(plan, Treatment('Standard'))"
           " + attends_classes + visits_last_90d")
model = smf.logit(formula, data=m).fit(disp=False)
odds = pd.DataFrame({"odds_ratio": np.exp(model.params),
                     "p_value": model.pvalues}).round(3)
print(odds)
