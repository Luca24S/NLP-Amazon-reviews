def assign_sentiment(row):
    """Assigns sentiment label based on RoBERTa scores."""
    if row["roberta_neg"] > row["roberta_neu"] and row["roberta_neg"] > row["roberta_pos"]:
        return "Negative"
    elif row["roberta_pos"] > row["roberta_neu"] and row["roberta_pos"] > row["roberta_neg"]:
        return "Positive"
    else:
        return "Neutral"

def validate_model(df):
    """Validates the model by comparing actual and predicted sentiments."""
    correct = sum(df["Actual_Sentiment"] == df["Predicted_Sentiment"])
    return correct / len(df)