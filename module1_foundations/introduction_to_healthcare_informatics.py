```python
# Import necessary libraries
import pandas as pd
import numpy as np

def run():
    print("Module 1: Introduction to Healthcare Informatics")

    # This is a placeholder for the actual content of the module.
    # In the actual implementation, this could be a series of lessons, exercises, or projects.
    # For example, you might have a lesson on the history of healthcare informatics,
    # followed by an exercise where students analyze a healthcare dataset using pandas.

    # Lesson: History of Healthcare Informatics
    print("\nLesson: History of Healthcare Informatics")
    print("In this lesson, we will explore the history of healthcare informatics...")

    # Exercise: Analyzing a Healthcare Dataset
    print("\nExercise: Analyzing a Healthcare Dataset")
    print("In this exercise, you will analyze a healthcare dataset using pandas...")
    # Note: In the actual implementation, you would provide the dataset and the instructions for the exercise.
    # For the purpose of this example, we will just simulate the exercise with a simple pandas operation.

    # Load a sample dataset (in the actual implementation, this would be a real healthcare dataset)
    data = pd.DataFrame({
        'Patient ID': np.arange(1, 101),
        'Age': np.random.randint(20, 80, size=100),
        'Condition': np.random.choice(['Healthy', 'Disease A', 'Disease B'], size=100)
    })

    # Perform a simple analysis: count the number of patients with each condition
    condition_counts = data['Condition'].value_counts()
    print("\nNumber of patients with each condition:")
    print(condition_counts)

    # End of module
    print("\nEnd of Module 1: Introduction to Healthcare Informatics")

if __name__ == "__main__":
    run()
```
