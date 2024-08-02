import datetime
import random

def random_date(start, end):
    """
    Generate a random datetime between `start` and `end` dates.
    
    :param start: The start date.
    :param end: The end date.
    :return: A random datetime between `start` and `end`.
    """
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

def add_random_timestamps_to_songs(input_file, output_file, start_date, end_date):
    """
    Add random timestamps to each song in the input file and write to the output file.
    
    :param input_file: Path to the input file containing song names.
    :param output_file: Path to the output file to save song names with random timestamps.
    :param start_date: The start date for generating random timestamps.
    :param end_date: The end date for generating random timestamps.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                song_name = line.strip()
                if song_name:
                    # Generate a random timestamp
                    timestamp = random_date(start_date, end_date).strftime('%Y-%m-%d')
                    # Write the timestamp and song name to the output file
                    outfile.write(f"{timestamp} {song_name}\n")
        print(f"Random timestamps added and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input and output file paths
input_file = 'songplays.txt'
output_file = 'songplays_with_random_timestamps.txt'

# Define the range for random timestamps (last year)
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.datetime.now()

# Call the function to add random timestamps to song names
add_random_timestamps_to_songs(input_file, output_file, start_date, end_date)
