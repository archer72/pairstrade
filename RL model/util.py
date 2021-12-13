def get_data(symbols, dates_range, update):
    import os
    import pandas as pd
    cwd = os.getcwd()
    dir = cwd + "/data/"
    df = pd.DataFrame()
    symbols.append('spy')
    for symbol in symbols:
        print("symbol", symbol)
        filename = dir + symbol + '.csv'
        data = pd.read_csv(filename, index_col=["Date"], parse_dates=['Date'])
        if df.empty:
            if 'Close' in data:
                df[symbol] = data['Close']
            else:
                df[symbol] = data['Rate']
        else:
            if 'Close' in data:
                df[symbol] = data['Close']
            else:
                df[symbol] = data['Rate']
    return df[df.index.isin(dates_range)].sort_index()
