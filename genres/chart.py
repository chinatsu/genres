import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from collections import Counter
from datetime import timedelta


def save(args, history, genres):
    ef = pd.json_normalize(
        [
            {"count": 0, "genre": g, "date": d}
            for d in [
                history[-1]["date"] - timedelta(days=x)
                for x in range((history[-1]["date"] - history[0]["date"]).days + 1)
            ]
            for g in set([x for y in genres for x in genres[y]])
        ]
    )
    df = pd.json_normalize(history)
    ef["date"] = ef["date"].dt.date.astype(str)
    df["date"] = df["date"].dt.date.astype(str)

    df = df.groupby(["date", "genre"]).size().reset_index(name="count")

    df = pd.concat([df, ef])

    df = df.groupby(["date", "genre"]).sum().groupby("genre").cumsum().reset_index()

    print(df)
    fig = px.bar(
        df, animation_frame="date", y="count", x="genre", range_y=[0, df["count"].max()]
    )
    path = f"charts/{args.user}_{args.formatted['from']}-{args.formatted['to']}.html"
    fig.write_html(path)
    # sns.set_theme(style="whitegrid")
    # fig = sns.catplot(
    #     data=pd.DataFrame({"genre": genres}),
    #     kind="count",
    #     y="genre",
    #     height=abs(args.top) / 2,
    #     aspect=1,
    #     palette=sns.color_palette("pastel"),
    # )
    # plt.title(
    #     f"{args.end} {abs(args.top)} genres for {args.user} in the period {args.formatted['from']} to {args.formatted['to']}"
    # )
    # path = f"charts/{args.user}_{args.formatted['from']}-{args.formatted['to']}.png"
    # fig.savefig(path)
    print(f"Saved to {path}")
