import os
import yaml

def create_training_folders(base_dir):
    # Definiere die Trainings- und Validierungsordner
    train_folder = os.path.join(base_dir, "train")
    val_folder = os.path.join(base_dir, "val")

    # Erstelle die Ordner, falls sie nicht existieren
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    return train_folder, val_folder

def create_yaml_file(yaml_path, train_folder, val_folder):
    # Erstelle die Datenstruktur für die YAML-Datei
    data = {
        'train': train_folder,
        'val': val_folder,
        'nc': 2,  # Anzahl der Klassen
        'names': ['oven', 'refrigerator']  # Namen der Klassen
    }

    # Schreibe die YAML-Datei
    with open(yaml_path, 'w') as file:
        yaml.dump(data, file)

def main():
    base_dir = "/path/to/coco"  # Basisverzeichnis für die Daten (Passe den Pfad an)
    
    # Erstelle die Ordner für Training und Validierung
    train_folder, val_folder = create_training_folders(base_dir)

    # Erstelle die YAML-Datei
    yaml_path = os.path.join(base_dir, "custom_coco.yaml")
    create_yaml_file(yaml_path, train_folder, val_folder)

    print("Training- und Validierungsordner sowie YAML-Datei wurden erstellt.")

if __name__ == "__main__":
    main()
