from config import dataset_path, output_path
from utils.data_loader import readJSON, save_to_json
from utils.preprocessing import preprocess_text, process_and_filter_reviews
from utils.sentiment_model import robertaScores
from utils.visualization import DistributionChart
from utils.analysis import assign_sentiment, validate_model
from utils.helper_functions import ensure_directory_exists

def main():
    # Assicurati che la cartella di output esista
    ensure_directory_exists(output_path)

    # Step 1: Carica il dataset
    print("Caricamento del dataset...")
    data = readJSON(dataset_path)
    print(f"Dataset caricato con {data.shape[0]} righe e {data.shape[1]} colonne.")

    # Step 2: Preprocessing
    print("Preprocessing del dataset...")
    data["reviewText_(processed)"] = data["reviewText"].apply(preprocess_text)
    data = process_and_filter_reviews(data, "reviewText_(processed)")
    print(f"Dopo il preprocessing, il dataset contiene {data.shape[0]} righe.")

    # Step 3: Sentiment Analysis con RoBERTa
    print("Esecuzione del modello RoBERTa per l'analisi del sentiment...")
    data["roberta_scores"] = data["reviewText_(processed)"].apply(robertaScores)
    data["Predicted_Sentiment"] = data.apply(assign_sentiment, axis=1)
    print("Analisi del sentiment completata.")

    # Step 4: Validazione del modello
    print("Validazione del modello...")
    accuracy = validate_model(data)
    print(f"Accuratezza del modello: {accuracy:.2%}")

    # Step 5: Visualizzazioni
    print("Generazione delle visualizzazioni...")
    DistributionChart(data, output_path)

    # Step 6: Salvataggio dei risultati
    print("Salvataggio dei risultati...")
    save_to_json(data, output_path / "processed_reviews.json")
    print("Tutti i risultati sono stati salvati nella cartella di output.")

if __name__ == "__main__":
    main()