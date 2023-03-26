# Import relevant libraries
import spacy

nlp = spacy.load('en_core_web_lg')

gardenPathSentences = ["The train raced towards The Bridge fell.", "The man who hunts ducks \
out on weekends.", "She told me a little white lie will come back to haunt me", "When Fred eats food gets thrown.", "That Jack is never here hurts."]

# Tokenisation --------------------------------------------------------------------------------------------------------
doc_tokens = [] # This list stores the token for each sentence in gardenPathSentences
for sentence in gardenPathSentences:
    doc = nlp(sentence)
    doc_token = [token.orth_ for token in doc]
    doc_tokens.append(doc_token)

# Print tokens
for token in doc_tokens:
    print(token)

# Entity Recognition
print("\n")
for sentence in gardenPathSentences:
    doc = nlp(sentence)
    print([(i, i.label_, i.label) for i in doc.ents])

# I do not really understand the FAC and Date entities. I will get an explanation of it and print it
print("\n")
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

print("\n")
entity_date = spacy.explain("DATE")
print(f"Date:{entity_date}")

# 1. FAC Entity
#   The FAC Entity is used to identify a span of text that refers to a facility or building e.g hospitals, airports,
#   highways etc. The Bridge is recognized as an FAC entity and this makes sense as bridge is a facility.

# 2. Date Entity
#   The DATE Entity is a predefined named entity used to identify a span of text that refers to specific dates or periods of time.
#   Weekend is recognized as a DATE entity and this makes sense as weekend is a time period.