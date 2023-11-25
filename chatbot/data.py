from datasets import load_dataset

# Load the dataset
dataset = load_dataset("audiofolder", data_dir="/path/to/data")

# Print the first item in the dataset
print(dataset["train"][0])

# Map the labels to the genre names
genre_names = {0: 'electronic', 1: 'punk'}

# Print the genre name of the first item in the dataset
print(genre_names[dataset["train"][0]['label']])