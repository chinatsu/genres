import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def save(args, genres):
    sns.set_theme(style="whitegrid")
    fig = sns.catplot(
        data=pd.DataFrame({"genre": genres}),
        kind="count",
        y="genre",
        height=abs(args.top) / 2,
        aspect=1,
        palette=sns.color_palette("pastel"),
    )
    plt.title(
        f"{args.end} {abs(args.top)} genres for {args.user} in the period {args.formatted['from']} to {args.formatted['to']}"
    )
    path = f"charts/{args.user}_{args.formatted['from']}-{args.formatted['to']}.png"
    fig.savefig(path)
    print(f"Saved to {path}")
