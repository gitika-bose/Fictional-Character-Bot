from openai import OpenAI

client = OpenAI(
  organization='org-tZQmKjHFNVsoxJDBXnNrTP6L',
  project='proj_cBTsydGjBpAcyqUZWooltSF0',
)

client.files.create(
  file=open("validation_dialogues.jsonl", "rb"),
  purpose="fine-tune"
)