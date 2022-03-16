import pandas as pd


def main():
    data = pd.read_csv('data.csv', encoding='cp1250', delimiter=';')

    # Adding positive percent column
    data['testy_pozytywne_procent'] = data['liczba_testow_z_wynikiem_pozytywnym'] / \
        data['liczba_wykonanych_testow'] * 100

    # Rounding column to 4 digits after comma
    data = data.round(
        {"testy_pozytywne_procent": 4})

    # Sorting dataframe by positive percent column
    data.sort_values(by=['testy_pozytywne_procent'],
                     inplace=True, ascending=False)

    # Extracting rows with positive percent > 20
    more_than_20_percent = data[data['testy_pozytywne_procent'] > 20]

    # Printing rows
    for _, row in more_than_20_percent.iterrows():
        print(
            f"{row['wojewodztwo']}-{row['powiat']}: {row['testy_pozytywne_procent']}")


if __name__ == "__main__":
    main()
