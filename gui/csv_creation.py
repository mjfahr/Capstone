from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd
import nltk

#output_directory = "csv/"


# Write CSV for (Index, Section_Index, File_Name)
def write_section_csv(data, output_directory):
    section_files = []
    for i in range(0, len(data)):
        s = data[i]
        section_index = 0
        while 1:
            start_index = s.find('[file:///', section_index)
            end_index = s.find(']', start_index + 1)

            if start_index == -1:
                break
            else:
                fn = s[start_index + 9:end_index]
                section_files.append((i, fn))
                section_index = end_index
    section_df = pd.DataFrame(section_files, columns=['Section_Index', 'File_Name'])
    section_df.index.name = "Index"
    section_df.to_csv(output_directory + "section_files.csv")


# Write CSV for (Index, Section_Index, Word, Frequency)
def write_section_statistics_csv(sections, output_directory):
    index_count = 0
    frames = []
    for i in range(0, len(sections)):
        section = sections[i]
        section = section.replace("\\n", " ")
        section_tokens = word_tokenize(section)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [w for w in section_tokens if not w in stop_words]
        filtered_tokens = [word for word in filtered_tokens if word.isalnum()]

        fdist = FreqDist(filtered_tokens)

        df = pd.DataFrame.from_dict(fdist, orient="index")
        df.columns = ['Frequency']
        df = df.sort_values(by=['Frequency'], ascending=False)
        df['Section_ID'] = [i] * len(df)
        df['Index'] = list(range(index_count, index_count + len(df)))
        df['Word'] = df.index
        df.set_index("Index", inplace=True)
        df = df[['Section_ID', 'Word', 'Frequency']]
        frames.append(df)

        index_count = index_count + len(df) + 1

    result = pd.concat(frames)
    # Write Index, Word, and Frequency to a CSV
    result.to_csv(output_directory + "section_word_statistics.csv")


# Write CSV for (Index, Word, Frequency)
def write_document_word_statistics(data, output_directory):
    # Frequency Distribution of filtered tokens
    fdist = FreqDist(data)
    df = pd.DataFrame.from_dict(fdist, orient="index")
    df.columns = ['Frequency']
    df = df.sort_values(by=['Frequency'], ascending=False)
    df['Index'] = list(range(0, len(df)))
    df['Word'] = df.index
    df.set_index("Index", inplace=True)
    df = df[['Word', 'Frequency']]

    # Write Index, Word, and Frequency to a CSV
    df.to_csv(output_directory + "document_word_statistics.csv")


# Write CSV for (Index, Word, Frequency)
# Grabs top 10% of data
def write_important_document_word_statistics(data, output_directory):
    # Frequency Distribution of filtered tokens
    fdist = FreqDist(data)
    df = pd.DataFrame.from_dict(fdist, orient="index")
    df.columns = ['Frequency']
    df = df.sort_values(by=['Frequency'], ascending=False)
    df['Index'] = list(range(0, len(df)))
    df['Word'] = df.index
    df.set_index("Index", inplace=True)
    df = df[['Word', 'Frequency']]

    length = int(len(df) / 10)
    data = df.iloc[:length]

    # Write Index, Word, and Frequency to a CSV
    data.to_csv(output_directory + "important_document_word_statistics.csv")


# Write CSV for (Index, Word, Frequency)
# Grabs nouns
def write_noun_document_word_statistics(data, output_directory):
    data = nltk.pos_tag(data)

    nouns = [word for (word, pos) in data if pos == 'NN']

    # Frequency Distribution of filtered tokens
    fdist = FreqDist(nouns)
    df = pd.DataFrame.from_dict(fdist, orient="index")
    df.columns = ['Frequency']
    df = df.sort_values(by=['Frequency'], ascending=False)
    df['Index'] = list(range(0, len(df)))
    df['Word'] = df.index
    df.set_index("Index", inplace=True)
    df = df[['Word', 'Frequency']]

    length = int(len(df) / 10)
    data = df.iloc[:length]

    # Write Index, Word, and Frequency to a CSV
    data.to_csv(output_directory + "noun_document_word_statistics.csv")


# Write CSV for (Index, Word, Frequency)
# Grabs nouns
def write_section_total_word_count(sections, output_directory):
    index_count = 0
    section_files = []
    for i in range(0, len(sections)):
        section = sections[i]
        section_tokens = word_tokenize(section)
        section_files.append((i, len(section_tokens)))

    section_df = pd.DataFrame(section_files, columns=['Section_Index', 'Total_Word_Count'])
    section_df.index.name = "Index"
    # Write Index, Word, and Frequency to a CSV
    section_df.to_csv(output_directory + "section_total_word_count.csv")