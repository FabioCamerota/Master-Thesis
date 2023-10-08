# Master-Thesis
This repository contains the code used to obtain the results of my master's thesis.
Read my full master's thesis [here](https://www.politesi.polimi.it/handle/10589/211114).
## Project structure
- `BERT+EAR_implementation.ipynb` contains the code used to train, validate, and test the BERT+EAR model (i.e. the BERT model with EAR _regularization_strength = 0.01_) and the BERT model.
  
- `XLNet+EAR_implementation.ipynb` contains the code used to train, validate and test both the XLNet+EAR model (i.e. the XLNet model with EAR _regularization_strength = 0.01_) and the XLNet model.
  
- `max_length_analysis.ipynb` was used to analyze the subword distribution within the comments in the Wiki Toxic data set.
  
- `plot_charts.py` and `plot_appendix_charts.py` were used to generate the charts of the "Results and Analysis" chapter and of the "Appendix", respectively.
## Data sets
- _Wiki Toxic data set_ can be downloaded from this [Hugging Face repository](https://huggingface.co/datasets/OxAISH-AL-LLM/wiki_toxic/tree/main).

- _Synthetic data set_ can be downloaded from this [GitHub repository](https://github.com/conversationai/unintended-ml-bias-analysis).
## Abstract
The proliferation of hate speech is a growing challenge for social media platforms, as toxic online comments can have dangerous consequences also in real life. There is a need for tools that can automatically and reliably detect hateful comments, and deep learning models have proven effective in solving this issue. However, these models have been shown to have unintended bias against some categories of people. Specifically, they may classify comments that reference certain frequently attacked identities (such as gay, trans, or Muslim) as toxic even if the comments themselves are actually not toxic (e.g. “I am Muslim”). To address this bias, previous authors introduced an Entropy-based Attention Regularization (EAR) method which, when applied to BERT, has been shown to reduce its unintended bias. In this study, the EAR method was applied not only to BERT, but also to XLNet. The investigation involved the comparison of four models: BERT, BERT+EAR, XLNet, and XLNet+EAR. Several experiments were performed, and the associated code is available on GitHub. The classification performance of these models was measured using the F1-score on a public data set containing comments collected from Wikipedia forums. While their unintended bias was evaluated by employing AUC-based metrics on a synthetic data set consisting of 50 identities grouped into four macro categories: Gender & Sexual orientation, Ethnicity, Religion, and Age & Physical disability. The results of the AUC-based metrics proved that EAR performs well on both BERT and XLNet, successfully reducing their unintended bias towards the 50 identity terms considered in the experiments. Conversely, the F1-score results demonstrated a negative impact of EAR on the classification performance of both BERT and XLNet.

## References
- The _EAR_ technique was introduced by Attanasio et al. in "Entropy-based Attention Regularization Frees Unintended Bias Mitigation from Lists". DOI: 10.4855 0
- _BERT_ was presented by Devlin et al. in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". DOI: 10.4 8550
- _XLNet_ was presented by Yang et al. in "XLNet: Generalized Autoregressive Pretraining for Language Understanding". DOI: 10.48550
