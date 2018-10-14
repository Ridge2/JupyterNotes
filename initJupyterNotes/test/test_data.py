from initJupyterNotes.data import get_fremont_data
import pandas as pd

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['West Side', 'East Side', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
