import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import marimo as mo
    return mo, pd


@app.cell
def _(pd):
    # loading balatro data
    path_to_data = r"C:\Users\WanDr\Desktop\balatro_hands.xlsm"
    df = pd.read_excel(path_to_data, sheet_name="run_tracker", skiprows=2)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Most Frequenctly Used Jokers**
    """)
    return


@app.cell
def _(df):
    joker_cols = ['Main Joker 1', 'Main Joker 2', 'Main Joker 3', 'Main Joker 4', 'Main Joker 5', 'Additional Jokers']

    # Melt all joker columns into one column
    melted = df[joker_cols].melt(value_name='Joker', var_name='Type')

    # Drop missing values
    melted = melted.dropna(subset=['Joker'])

    # Split additional jokers by comma and flatten
    melted = melted.assign(Joker=melted['Joker'].str.split(',')).explode('Joker')

    # Strip whitespace and normalize -- remove "(copy)"
    melted['Joker'] = melted['Joker'].str.strip().str.replace(r'\s*\(copy\)$', '', regex=True)

    # Count frequency
    joker_count = melted['Joker'].value_counts()

    joker_count
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Most Used Card Modifiers**
    """)
    return


@app.cell
def _(df):
    modifier_series = df['Card Modifiers'].dropna()

    # dropping empty cells
    modifier_series.dropna()
    modifier_series = modifier_series[modifier_series.str.strip() != '']

    # split the comma seperated entries and flatten into single list
    all_modifiers = modifier_series.str.split(',').explode().str.strip()

    # count frequency of each modifier
    modifier_counts = all_modifiers.value_counts()

    # showing all modifiers
    modifier_counts
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Most Played Main & Secondary Hands**
    """)
    return


@app.cell
def _(df, pd):
    # Hand frequency count
    main_hand_count = df['Main Hand'].value_counts()
    secondary_hand_count = df['Secondary Hand'].value_counts()

    # combine both into a single dataframe
    hand_counts = pd.concat(
        [main_hand_count, secondary_hand_count],
        axis=1
    )

    # setting column names
    hand_counts.columns = ['Main Hand count', 'Secondary Hand count']

    # filling in NAN values with "Not Played Yet"
    hand_counts = hand_counts.fillna('Not Played')

    # show hand count
    hand_counts
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Deck, Stake, Main Hand, Run Status, Seed, Highest Ante of seed, Highest Score of seed.**
    #### ***(sorted by highest score in descending order)***
    """)
    return


@app.cell
def _(df):
    #Ante seed
    ante_seed = df[['Deck', 'Stake', 'Main Hand','Win/Loss','Seed','Highest Ante', 'Highest Score']]

    # sorting by highest ante descending
    ante_seed = ante_seed.sort_values(by='Highest Score', ascending=False)

    # Filling Nan Values with None
    ante_seed = ante_seed.fillna('NONE')

    # Resetting index
    ante_seed = ante_seed.reset_index(drop=True)

    # show ante seed
    ante_seed
    return


@app.cell
def _():
    # exporting to csv
    # df.to_csv("./data/balatro_powerbi.csv", index=False)
    return


if __name__ == "__main__":
    app.run()
