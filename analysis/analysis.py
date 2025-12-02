import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # loading balatro data
    path_to_data = r"C:\Users\WanDr\Desktop\balatro_hands.xlsx"
    df = pd.read_excel(path_to_data, sheet_name="run_tracker", skiprows=2)

    # preview data
    print(df.head())
    return (df,)


@app.cell
def _(df):
    # flattening jokers and counting frequency of each joker
    joker_cols = ['Main Joker 1', 'Main Joker 2', 'Main Joker 3', 'Main Joker 4', 'Main Joker 5', 'Additional Jokers']

    # All jokers df
    all_jokers = df[joker_cols].stack().dropna()

    # counting frequency of each joker
    joker_count = all_jokers.value_counts()

    # show joker count
    joker_count.to_frame(name="Joker Count")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
