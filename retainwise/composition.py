"""Descriptive direct standardisation over common, sufficiently sized strata."""
import pandas as pd
from .analysis import MIN_GROUP, rate_table
from .data import TENURE_ORDER


def compare_composition(df, field):
    if field not in ('Department', 'TenureBand'):
        raise ValueError('Choose Department or TenureBand')
    cells = df.groupby([field, 'OverTime'], observed=True)['Attrition_Flag'].agg(n='size', attrited='sum').reset_index()
    counts = cells.pivot(index=field, columns='OverTime', values='n').reindex(columns=['No', 'Yes']).fillna(0)
    eligible = counts.index[(counts >= MIN_GROUP).all(axis=1)]
    if field == 'TenureBand':
        eligible = pd.Index([name for name in TENURE_ORDER if name in eligible])
    safe = cells[cells[field].isin(eligible)].copy()
    cohort = df[df[field].isin(eligible)]
    result = {'total_n': len(df), 'eligible_n': len(cohort), 'eligible_strata': list(eligible),
              'all_crude': rate_table(df, 'OverTime', ['No', 'Yes']),
              'eligible_crude': rate_table(cohort, 'OverTime', ['No', 'Yes']),
              'cells': safe, 'standardised': pd.DataFrame(columns=['OverTime', 'rate_pct']), 'gap_pp': None}
    if safe.empty:
        return result
    weights = safe.groupby(field, observed=True)['n'].sum() / len(cohort)
    safe['weight'] = safe[field].map(weights).astype(float)
    safe['rate_pct'] = 100 * safe['attrited'] / safe['n']
    safe['weighted_rate'] = safe['weight'] * safe['rate_pct']
    adjusted = safe.groupby('OverTime', observed=True)['weighted_rate'].sum().reindex(['No', 'Yes'])
    result['standardised'] = adjusted.rename('rate_pct').reset_index()
    result['gap_pp'] = float(adjusted['Yes'] - adjusted['No'])
    result['cells'] = safe.drop(columns='weighted_rate')
    return result
