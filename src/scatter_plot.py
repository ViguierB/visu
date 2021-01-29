import matplotlib.pyplot as plt
import prompt
import pandas as pd

def scatter_plot(filename):
    dfb = pd.read_csv(filename, sep=r'\s*;\s*',
                         header=0, encoding='utf-8', engine='python')
    dfb.drop(dfb.index[:1], inplace=True)

    section_str = input("Choose a section 'start:stop:step' ex: 10:100:10 (empty -> entire data)\n")
    if not section_str:
        df = dfb
    else:
        section = list(map(lambda n: int(n), section_str.split(':')))
        df = dfb.iloc[slice(section[0], section[1], section[2])]

    columns = df.columns
    vals = prompt.choose("Choose 2 parameter:", columns, limit=2, min=2)
    val1 = columns[vals[0]]
    val2 = columns[vals[1]]
    fig, ax = plt.subplots(figsize=(15, 9))
    df[val1] = pd.to_numeric(df[val1])
    df[val2] = pd.to_numeric(df[val2])
    ax.scatter(x = df[val1], y = df[val2])
    plt.xlabel(val1)
    plt.ylabel(val2)
    fig.show()
    plt.show()