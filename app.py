"""WorkforceLens: pooled and composition-standardised descriptive comparisons."""
import streamlit as st
from retainwise.data import load_data
from retainwise.composition import compare_composition

st.set_page_config(page_title='WorkforceLens | Sanif Mujawar', layout='wide')
st.title('WorkforceLens')
st.caption('Sanif Mujawar | An attributed adaptation of RetainWise')
st.write('How does workforce composition change the observed overtime-attrition comparison?')
st.info('Fictional practice records. These are descriptive comparisons, not causal effects or individual predictions.')
field = st.selectbox('Compare a common group mix', ['Department', 'TenureBand'], format_func=lambda x: {'Department':'Department', 'TenureBand':'Company tenure band'}[x])
df = load_data()
r = compare_composition(df, field)
a,b,c = st.columns(3)
a.metric('Fictional records', f'{len(df):,}')
b.metric('Observed attrition', f"{100*df.Attrition_Flag.mean():.1f}%")
c.metric('Eligible for common-mix comparison', f"{r['eligible_n']:,} / {r['total_n']:,}")
st.subheader('1. All-record comparison')
st.dataframe(r['all_crude'], hide_index=True)
st.caption('Rates are percentages; n is the denominator. Small cells are withheld.')
if r['gap_pp'] is None:
    st.warning('No stratum contains at least ten records in both overtime groups. A common-mix comparison is unavailable.')
else:
    st.subheader('2. Compare the same eligible records')
    st.write("The crude rates use each overtime group's observed mix. Standardised rates give both groups the same pooled stratum weights.")
    left,right=st.columns(2)
    with left:
        st.write('Crude rates in eligible strata')
        st.dataframe(r['eligible_crude'],hide_index=True)
    with right:
        st.write('Common-mix rates (%)')
        st.dataframe(r['standardised'],hide_index=True)
    crude=r['eligible_crude'].set_index('OverTime')['rate_pct']
    st.metric('Common-mix gap: overtime Yes minus No',f"{r['gap_pp']:.2f} percentage points")
    st.write(f"Eligible crude gap: {crude['Yes']-crude['No']:.2f} percentage points. Compare it with the common-mix gap before interpreting the all-record result.")
    plot=r['cells'].pivot(index=field,columns='OverTime',values='rate_pct')
    st.subheader('3. Within-stratum rates (%)')
    st.bar_chart(plot,stack=False)
    with st.expander('Inspect denominators, rates and weights'):
        st.dataframe(r['cells'],hide_index=True)
    st.caption('Only strata meeting the minimum size in both groups appear. Missing strata are excluded, never treated as zero.')
with st.expander('Method, provenance and limitations'):
    st.markdown('Department and tenure mix are alternative descriptive views. Common weights do not remove all confounding. Tenure may reflect time at risk; this is not a causal adjustment. No annual attrition, intervention effect or discrimination finding is established.')
    st.markdown('[Project and provenance](https://github.com/sanifmujawar/WorkforceLens-Sanif) | [Original RetainWise](https://github.com/chasimarshad-bot/RetainWise-Employee-Attrition-Insights)')
    st.write('Data publisher: Pavan Subhash, Kaggle; fictional IBM practice dataset. Source and derivative terms are retained in data/SOURCE.md. Suppression does not guarantee anonymity.')
