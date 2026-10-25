# Composition comparison method

For each stratum s and overtime group g, compute n(s,g), attrited(s,g) and rate(s,g) = attrited / n. Only strata with both No and Yes n >= 10 enter the standardised comparison. Weights w(s) are the stratum's pooled n divided by the total eligible n. Each group's standardised rate is sum(w(s) * rate(s,g)). The gap is Yes minus No, in percentage points.

The eligible crude comparison uses exactly the same eligible records with each group's observed composition. The all-record crude comparison is shown separately. Coverage reports how many original records entered the standardised calculation. No outcome cell below ten is released. Excluded strata and missing groups cannot silently receive zero rates.

Department and tenure band are alternative descriptive partitions. Tenure is measured in the same snapshot as attrition and may itself relate to time at risk or the outcome. Standardising by tenure is a sensitivity description, not an appropriate causal identification claim. No confidence intervals, hypothesis tests, forecasting or individual scoring are implemented.

Synthetic tests check exact weighted results, missing-group exclusion, small-cell withholding and no-overlap handling. Current source results are calculated at runtime from reviewed v1 data. Sanif should discuss why the gap changes or persists rather than assuming reweighting resolves confounding.
