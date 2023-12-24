```python
# Import necessary libraries
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from nltk import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk import ne_chunk

def run():
    print("Module 3: Named Entity Recognition (NER) in Medical Text")

    # This is a placeholder for the actual content of the module.
    # In the actual implementation, this could be a series of lessons, exercises, or projects.
    # For example, you might have a lesson on the basics of Named Entity Recognition,
    # followed by an exercise where students apply these concepts to a medical text.

    # Lesson: Basics of Named Entity Recognition
    print("\nLesson: Basics of Named Entity Recognition")
    print("In this lesson, we will explore the basics of Named Entity Recognition...")

    # Exercise: Applying Named Entity Recognition to a Medical Text
    print("\nExercise: Applying Named Entity Recognition to a Medical Text")
    print("In this exercise, you will apply Named Entity Recognition concepts to a medical text...")
    # Note: In the actual implementation, you would provide the text and the instructions for the exercise.

    # Placeholder for the Named Entity Recognition function
    def named_entity_recognition(text):
        # Tokenize the text
        tokens = word_tokenize(text)

        # Apply part of speech tagging
        pos_tags = pos_tag(tokens)

        # Apply named entity recognition
        named_entities = ne_chunk(pos_tags)

        # Convert the named entities to the conll format
        named_entities = tree2conlltags(named_entities)

        return named_entities

    # Placeholder for a sample text
    text = "Dr. Smith diagnosed the patient with diabetes and prescribed Metformin."

    # Apply the Named Entity Recognition function to the sample text
    named_entities = named_entity_recognition(text)

    # Print the named entities
    print("\nNamed Entities:")
    for named_entity in named_entities:
        print(named_entity)
```
