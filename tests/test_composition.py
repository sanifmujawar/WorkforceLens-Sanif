from pathlib import Path
import pandas as pd
import pytest
from retainwise.composition import compare_composition
from streamlit.testing.v1 import AppTest


def sample():
    rows=[]
    for dept,ot,n,k in [('A','No',20,2),('A','Yes',10,4),('B','No',10,2),('B','Yes',20,10)]:
        rows += [{'Department':dept,'OverTime':ot,'Attrition_Flag':int(i<k)} for i in range(n)]
    return pd.DataFrame(rows)


def test_common_mix():
    r=compare_composition(sample(),'Department')
    assert r['eligible_n']==60
    rates=r['standardised'].set_index('OverTime').rate_pct
    assert rates['No']==pytest.approx(15)
    assert rates['Yes']==pytest.approx(45)
    assert r['gap_pp']==pytest.approx(30)
    assert r['cells'].groupby('OverTime').weight.sum().tolist()==[1,1]


def test_small_and_missing_cells_excluded():
    df=sample()
    extra=pd.DataFrame([{'Department':'C','OverTime':'No','Attrition_Flag':0}]*20+[{'Department':'C','OverTime':'Yes','Attrition_Flag':1}]*9+[{'Department':'D','OverTime':'Yes','Attrition_Flag':1}]*15)
    r=compare_composition(pd.concat([df,extra]),'Department')
    assert r['eligible_n']==60
    assert set(r['cells'].Department)=={'A','B'}


def test_no_overlap():
    r=compare_composition(sample().query("OverTime == 'No'"),'Department')
    assert r['eligible_n']==0 and r['gap_pp'] is None
    assert r['standardised'].empty


def test_app_both_partitions():
    app=AppTest.from_file(Path(__file__).resolve().parents[1] / 'app.py').run(timeout=30)
    assert not app.exception
    app.selectbox[0].select('TenureBand').run(timeout=30)
    assert not app.exception
    assert any('Common-mix gap' in m.label for m in app.metric)
