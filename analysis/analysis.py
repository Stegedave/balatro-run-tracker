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
    # flattening jokers and counting frequency of each joker
    joker_cols = ['Main Joker 1', 'Main Joker 2', 'Main Joker 3', 'Main Joker 4', 'Main Joker 5', 'Additional Jokers']

    # All jokers df
    all_jokers = df[joker_cols].stack().dropna()

    # counting frequency of each joker
    joker_count = all_jokers.value_counts()

    # show joker count
    joker_count
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
    # **Run Status, Seed, and Highest Ante Reached in Seed**
    #### ***(sorted in descending order)***
    """)
    return


@app.cell
def _(df):
    #Ante seed
    ante_seed = df[['Main Hand', 'Secondary Hand','Win/Loss','Seed','Highest Ante']]

    # sorting by highest ante descending
    ante_seed = ante_seed.sort_values(by='Highest Ante', ascending=False)

    # Filling Nan Values with None
    ante_seed = ante_seed.fillna('NONE')

    # Resetting index
    ante_seed = ante_seed.reset_index(drop=True)

    # show ante seed
    ante_seed
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
