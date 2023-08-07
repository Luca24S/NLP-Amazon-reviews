from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL).to("mps" if torch.backends.mps.is_built() else "cpu")

def robertaScores(text):
    """Gets sentiment scores for a given text using RoBERTa."""
    try:
        encoded_text = tokenizer(text, return_tensors="pt").to("mps")
        output = model(**encoded_text)
        scores = softmax(output[0][0].detach().cpu().numpy())
        return {"roberta_neg": scores[0], "roberta_neu": scores[1], "roberta_pos": scores[2]}
    except Exception as e:
        print(f"Error processing text: {e}")
        return {"roberta_neg": None, "roberta_neu": None, "roberta_pos": None}