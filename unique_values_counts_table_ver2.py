def unique_values_counts_table(data, columns):

    tables = []

    for column in columns:
        if column in data:
            #counting unique values
            counts = {}
            for item in data[column]:
                counts[item] = counts.get(item, 0) + 1

            #sorting the counts in ascending order
            sorted_counts = sorted(counts.items(), key=lambda x: x[1])

            #width for formatting
            max_key_length = max(len(str(key)) for key, _ in sorted_counts)
            max_value_length = max(len(str(value)) for _, value in sorted_counts)

            #header and separator
            header = f"| {column.ljust(max_key_length)} | {'Count'.rjust(max_value_length)} |"
            separator = '+' + '-' * (max_key_length + 2) + '+' + '-' * (max_value_length + 7) + '+'

            #table rows
            table_rows = [f"| {str(key).ljust(max_key_length)} | {str(value).rjust(max_value_length)} |"
                          for key, value in sorted_counts]

            #combining all parts of the table
            table = separator + '\n' + header + '\n' + separator + '\n' + '\n'.join(table_rows) + '\n' + separator
            tables.append(table)
        else:
            tables.append(f"Column '{column}' not found in data.")

    return '\n\n'.join(tables)

print(unique_values_counts_table(df, ['credit_policy', 'inq_last_6mths', 'delinq_2yrs', 'pub_rec', 'not_fully_paid']))