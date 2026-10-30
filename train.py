from src.model import train_model

if __name__ == "__main__":
    model, metrics = train_model()
    print("CampusPulse model trained successfully.")
    for name, value in metrics.items():
        print(f"{name}: {value:.3f}")
    print("The model is trained in memory; no model file is required.")
