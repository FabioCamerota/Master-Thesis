# Master-Thesis
This repository contains the code used to obtain the results of my master's thesis.
## Project structure
- `BERT+EAR_implementation.ipynb` contains the code used to train, validate and test the BERT+EAR model (i.e. the BERT model with EAR _regularization_strength = 0.01_) and the BERT model.
  
- `XLNet+EAR_implementation.ipynb` contains the code used to train, validate and test both the XLNet+EAR model (i.e. the XLNet model with EAR _regularization_strength = 0.01_) and the XLNet model.
  
- `max_length_analysis.ipynb` was used to analyze the subword distribution within the comments in the Wiki Toxic data set.
  
- `plot_charts.py` and `plot_appendix_charts.py` were used to generate the charts of the "Results and Analysis" chapter and of the "Appendix", respectively.
## Data sets
- _Wiki Toxic data set_ can be downloaded from this [Hugging Face repository](https://huggingface.co/datasets/OxAISH-AL-LLM/wiki_toxic/tree/main).

- _Synthetic data set_ can be downloaded from this [GitHub repository](https://github.com/conversationai/unintended-ml-bias-analysis).
## Abstract
The abstract will be added after my thesis is published to avoid self-plagiarism.

## References
- The _EAR_ technique was introduced by Attanasio et al. in "Entropy-based Attention Regularization Frees Unintended Bias Mitigation from Lists". DOI: 10.4855 0
- _BERT_ was presented by Devlin et al. in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". DOI: 10.4 8550
- _XLNet_ was presented by Yang et al. in "XLNet: Generalized Autoregressive Pretraining for Language Understanding". DOI: 10.48550
