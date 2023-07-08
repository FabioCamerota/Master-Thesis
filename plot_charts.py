import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import List

# This way plots have bigger font size
plt.rcParams.update({'font.size': 18})


# This function is used to plot a single bar chart
def single_plot(scores: List[float], title: str):
    data = {'model': ['BERT', 'BERT+EAR', 'XLNet', 'XLNet+EAR'],
            'score': scores
            }
    df = pd.DataFrame(data)

    colors = ['blue', 'darkblue', 'red', 'darkred']
    plt.bar(df['model'], df['score'], color=colors)
    # add values on top of bars
    # for i in range(len(df['model'])):
    #    plt.text(i, df['score'][i]+0.01, df['score'][i], ha='center')
    plt.title(title, fontsize=14)
    plt.ylim(0, 1)
    plt.show()


# This function is used to plot multiple bar charts in the same image for 4 different models
def multiple_plots(BERT, BERT_EAR, XLNET, XLNET_EAR):
    metrics = ("Subgroup AUC", "BPSN AUC", "BNSP AUC")
    models = {
        'BERT': BERT,
        'BERT+EAR': BERT_EAR,
        'XLNet': XLNET,
        'XLNet+EAR': XLNET_EAR,
    }

    x = np.arange(len(metrics))  # the label locations
    width = 0.20  # the width of the bars
    multiplier = 0
    colors = ['blue', 'darkblue', 'red', 'darkred']

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement, color in zip(models.keys(), models.values(), colors):
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width,
                       label=attribute, color=color)
        #ax.bar_label(rects, padding=4)
        multiplier += 1

    ax.set_title('AUC')
    ax.set_xticks(x + 0.30, metrics)
    ax.legend(loc='upper left', ncols=4)
    ax.set_ylim(0, 1.1)
    plt.show()


# This function is used to plot multiple bar charts in the same image for only 2 different models
def multiple_plots_2(BERT, BERT_EAR):
    metrics = ("Subgroup AUC", "BPSN AUC", "BNSP AUC")
    models = {
        'BERT': BERT,
        'BERT+EAR': BERT_EAR,
    }

    x = np.arange(len(metrics))  # the label locations
    width = 0.20  # the width of the bars
    multiplier = 0
    colors = ['blue', 'darkblue', ]

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement, color in zip(models.keys(), models.values(), colors):
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width,
                       label=attribute, color=color)
        #ax.bar_label(rects, padding=2)
        multiplier += 1

    ax.set_title('AUC')
    ax.set_xticks(x + 0.1, metrics)
    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 1.1)

    plt.show()


# F1-score (full test dataset)
F1_full_score = [0.6780, 0.6629, 0.6529, 0.6067]
F1_full_title = 'F1-score (full test dataset)'
# single_plot(F1_full_score, F1_full_title)

# F1-score (half test dataset)
F1_half_score = [0.6763, 0.6622, 0.6498, 0.6045]
F1_half_title = 'F1-score (half test dataset)'
# single_plot(F1_half_score, F1_half_title)


# GENDER
BERT = (0.8809, 0.8821, 0.8823)
BERT_EAR = (0.8741, 0.8736, 0.8740)
XLNET = (0.7699, 0.7688, 0.7773)
XLNET_EAR = (0.8452, 0.8438, 0.8455)
#multiple_plots(BERT, BERT_EAR, XLNET, XLNET_EAR)
# GENDER-ALL
BERT = (0.9064, 0.9068, 0.9072)
BERT_EAR = (0.8993, 0.8988, 0.8991)
#multiple_plots_2(BERT, BERT_EAR)
# ETHNICITY
BERT = (0.9619, 0.9631, 0.9618)
BERT_EAR = (0.9843, 0.9839, 0.9844)
XLNET = (0.9553, 0.9552, 0.9550)
XLNET_EAR = (0.9293, 0.9283, 0.9311)
#multiple_plots(BERT, BERT_EAR, XLNET, XLNET_EAR)
# RELIGION
BERT = (0.9525, 0.9525, 0.9525)
BERT_EAR = (0.9873, 0.9873, 0.9873)
XLNET = (0.9483, 0.9483, 0.9483)
XLNET_EAR = (0.9333, 0.9333, 0.9333)
#multiple_plots(BERT, BERT_EAR, XLNET, XLNET_EAR)
# AGE
BERT = (0.9187, 0.9227, 0.9181)
BERT_EAR = (0.9392, 0.9445, 0.9383)
XLNET = (0.8881, 0.8905, 0.8859)
XLNET_EAR = (0.8995, 0.9029, 0.8988)
#multiple_plots(BERT, BERT_EAR, XLNET, XLNET_EAR)
# overall mean
BERT = (0.9282, 0.9298, 0.9285)
BERT_EAR = (0.9440, 0.9449, 0.9438)
XLNET = (0.8875, 0.8877, 0.8890)
XLNET_EAR = (0.8998, 0.8999, 0.9004)
#multiple_plots(BERT, BERT_EAR, XLNET, XLNET_EAR)
