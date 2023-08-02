!pip install openai



# Commented out IPython magic to ensure Python compatibility.
# %env OPENAI_API_KEY=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

import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
def correct_grammar(input_string):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Correct this to standard English: " + input_string +"\n",
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop="\n\n",
    )
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.set_page_config(page_title="Grammar check!")
    st.title("GRammar check- Generate correct grammar")
    st.text("by: Exekiel Dela Cruz BSCS 3A")


def correct_grammar(input_string):
    # Add your grammar correction logic here
    # For example, you can use language processing libraries like NLTK or SpaCy
    # to correct grammar errors in the input_string.

    # For demonstration purposes, let's just return the input_string as is.
    return input_string

str_inst = "Some text to be included in the input_string."
input_string = "Generate grammar for the following tasks:\n" + str_inst
output = correct_grammar(input_string)
print(f"Input: {input_string}\nOutput:\n{output}")

if __name__ == "__main__":
    main()

input_string = "She no went to the market"
output = correct_grammar(input_string)
print(f"Input: {input_string}\nOutput: {output}")
