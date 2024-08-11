import docx
import json

def generate_dialogues(filepath):

    doc = docx.Document(filepath)

    # Initialize variables
    dialogues = []
    previous_line = None

    # Iterate through paragraphs to find dialogues
    # count = 1
    for table in doc.tables:
        for row in table.rows:
            if not row.cells[0].text.startswith('['):
                if row.cells[0].text.startswith('Tanjirou'):
                    # if count < 20:
                    #     print('.'.join(row.cells[1].text.split('\n')))
                    #     count+=1
                    # Extract Tanjirou's line
                    tanjirou_line = '.'.join(row.cells[1].text.split('\n'))

                    # Save the previous speaker's line
                    if previous_line:
                        dialogues.append([{"role": "system", "content": "You are Tanjiro from 'Demon Slayer', kind by nature and full of determination."},{"role": "user", "content": previous_line},{"role": "assistant", "content": tanjirou_line}])
                        previous_line = None
                else:
                    # if count < 20:
                    #     print('.'.join(row.cells[1].text.split('\n')))
                    # Save the previous line
                    if row.cells[1].text.strip() and not row.cells[1].text.isupper():
                        previous_line = '.'.join(row.cells[1].text.split('\n'))
    return dialogues

docs = ['Demon Slayer S.2 E.02 (ENG sub).docx', 'Demon Slayer S.2 E.18 (ENG sub).docx', 'Demon Slayer S.3 E.01 (ENG sub).docx', 'Demon Slayer S.3 E.02 (ENG dub).docx', 'Demon Slayer S.3 E.03 (ENG sub).docx', 'Demon Slayer S.4 E.01 (ENG sub).docx', 'Demon Slayer S.4 E.02 (ENG sub).docx']
formatted_dialogues = []

for doc in docs:
    dialogues = generate_dialogues(doc)
    formatatted_dialogue = [{"messages":dialogue} for dialogue in dialogues]
    formatted_dialogues.extend(formatatted_dialogue)

# Save the formatted dialogues to a new file
with open('formatted_dialogues.jsonl', 'w') as f:
    for entry in formatted_dialogues:
        json_line = json.dumps(entry)
        f.write(json_line + '\n')

print("Tanjirou's dialogues and the lines right before them have been formatted and saved to 'formatted_dialogues.json'")