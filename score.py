with open("output_4.txt", "r", encoding="utf-8") as file:
    tag_tuples = []
    unique_tags = set()
    for line in file:
        parts = line.strip().split("\t")
        if len(parts) >= 3:
            tag_tuple = (parts[1], parts[2])
            tag_tuples.append(tag_tuple)
            unique_tags.add(parts[1])
            unique_tags.add(parts[2])

tag_counts = [[tag, 0, 0, 0] for tag in unique_tags]

for tag_count in tag_counts:
    for tag_tuple in tag_tuples:
        if tag_count[0] == tag_tuple[0] and tag_count[0] == tag_tuple[1]:
            tag_count[1] += 1

for tag_count in tag_counts:
    for tag_tuple in tag_tuples:
        if tag_count[0] != tag_tuple[0] and tag_count[0] == tag_tuple[1]:
            tag_count[2] += 1

for tag_count in tag_counts:
    for tag_tuple in tag_tuples:
        if tag_count[0] == tag_tuple[0] and tag_count[0] != tag_tuple[1]:
            tag_count[3] += 1

tag_analysis_counts = [[tag, 0, 0, 0] for tag in unique_tags]

for tag_count in tag_counts:
    for tag_analysis in tag_analysis_counts:
        if tag_count[0] == tag_analysis[0]:
            tag_analysis[1] = tag_count[1]/(tag_count[1] + tag_count[2])
            tag_analysis[2] = tag_count[1]/(tag_count[1] + tag_count[3])
            tag_analysis[3] = (2*tag_analysis[1]*tag_analysis[2])/(tag_analysis[1]+tag_analysis[2])

with open('analysis_output.txt', 'a', encoding='utf-8') as output_file:
    output_file.write(f'''File 4:\n\n''')
    for analysis in tag_analysis_counts:
        output_file.write(f'''Tag: {analysis[0]}\nPrecision: {analysis[1]:.2f}\nRecall: {analysis[2]:.2f}\nF1: {analysis[3]:.2f}\n\n''')
