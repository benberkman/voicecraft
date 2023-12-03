from sklearn.model_selection import train_test_split
import pandas as pd
import json
import os

def load_data(json_directory):
    data = []
    for filename in os.listdir(json_directory):
        if filename.endswith('.json'):
            file_path = os.path.join(json_directory, filename)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                for fragment in json_data['fragments']:
                    text = ' '.join(fragment['lines'])
                    start_time = fragment['begin']
                    end_time = fragment['end']
                    data.append((filename, start_time, end_time, text))
    return pd.DataFrame(data, columns=['filename', 'start_time', 'end_time', 'text'])

def split_data(df):
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)  # Adjust the test_size as needed
    return train_df, val_df

def main():
    json_directory = '../processed_data/aligned_data'
    df = load_data(json_directory)
    train_df, val_df = split_data(df)

    # Save the datasets
    train_df.to_csv('../data/model/train.csv', index=False)
    val_df.to_csv('../data/model/val.csv', index=False)

if __name__ == "__main__":
    main()
