import pandas as pd
import h5py


def get_keys(data_path):
    with h5py.File(data_path, 'r') as f:
        return list(f)


if __name__ == '__main__':
    data_path = 'factor_1_window@1.h5'
    key_list = get_keys(data_path)
    key = key_list[0]
    # df_data1 = read_data(data_path, key)

    with h5py.File(data_path, 'r') as f:
        if key in f:
            array = f[key]['DATA'][:]

    timestamp = (
    pd.date_range(start=f'2023-01-01 09:30:00', end=f'2023-01-01 15:00:00', freq='1S')
    .to_series()
    .between_time('13:00:00', '11:30:00')
    )
    factor_series = pd.Series(array, index=timestamp)
