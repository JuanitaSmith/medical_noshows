import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_relationships(df, x, y):
    """ plot relationships between two variables """

    sns.set(style='white', font_scale=1)
    fig, ax = plt.subplots(figsize=(16, 4))
    g = sns.countplot(data=df, x=x, hue=y, ax=ax)

    g.set_xticklabels(g.get_xticklabels(), rotation=90, fontsize=8)
    g.set_ylabel('Number of patients with {}'.format(y), fontsize=10)
    g.set_title('Relationship between {} and {}'.format(x, y), fontsize=12)
    plt.show()


def display_correlations(corr_matrix,
                         figsize=(10, 10),
                         title='Correlation Heatmap for most influential features',
                         dpi=600):
    """ Shows the top correlated features in a more condense triangle"""

    sns.set(style='white', font_scale=3)

    # display shows all of a dataframe
    plt.subplots(figsize=figsize, dpi=dpi)

    # hide the upper triangle, as it's the same as bottom triagle there is no need to show it
    # create array of zero's the same shape and type as the data
    mask = np.zeros_like(corr_matrix, dtype=bool)

    # triu_indices_from returns the indices for the upper triangle of the data
    mask[np.triu_indices_from(mask)] = True

    cmap = "RdBu"
    s = sns.heatmap(corr_matrix,
                    mask=mask,
                    annot=True,
                    cmap=cmap,
                    cbar=False,
                    linecolor="grey",
                    square=True,
                    linewidths=1,
                    vmin=-1,
                    vmax=1,
                    annot_kws={"size": 8})

    plt.title(title, fontsize=12)
    s.set_yticklabels(s.get_yticklabels(), rotation=0, fontsize=8)
    s.set_xticklabels(s.get_xticklabels(), rotation=90, fontsize=8)

    plt.show()


def plot_proportions(df, columns, y, sort_ascending=False):
    """plot a bar chart for each column showing proportional relationship with a binary indicator

    inputs:
    df: dataframe
    columns: columns for which a bar chart needs to be produced
    y: binary indicator

    outputs: bar chart

    """

    for col in columns:

        # no plot is needed for the binary indicator
        if y in col:
            continue

        # calculate proportions/percentages for each feature
        data = df.groupby(col)[y].value_counts(normalize=True)
        data = data.mul(100)
        data = data.rename('percentage').reset_index()

        # only plot no_show relationships
        query = "{} == 0".format(y)
        data.drop(data.query(query).index, inplace=True)
        data = data.sort_values('percentage', ascending=sort_ascending)

        title = ('Relationship between {} and {}'.format(col, y))
        g = sns.catplot(x=col, y='percentage', data=data, orient='v', kind='bar').set(title=title)

        # control figure size so we don't get big ugly fat barcharts
        if df[col].nunique() < 4:
            g.fig.set_size_inches(3, 2)
        else:
            g.fig.set_size_inches(15, 4)

        # annotate % values on top of bar chart
        if data.shape[0] < 30:
            for p in g.ax.patches:
                txt = str(p.get_height().round(2)) + '%'
                txt_x = p.get_x()
                txt_y = p.get_height()
                g.ax.text(txt_x, txt_y, txt, fontsize=8)

        g.set_xticklabels(fontsize=8)
        plt.xticks(rotation='vertical')

        plt.show()
