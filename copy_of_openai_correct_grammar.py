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
    st.title("Grammar check- Generate correct grammar")
    st.text("by: Exekiel Dela Cruz BSCS 3A")
    instructions = ['1. Grammer correct']

    str_inst = ''
    count = 0
    for i in instructions:
        str_inst = str_inst + i
        if count < len(instructions)-1:
            str_inst = str_inst + ',\n'
        count += 1



def correct_grammar(input_string):
    # Add your grammar correction logic here
    # For demonstration purposes, let's just return the input_string as is.
    return input_string

def main():
    st.title("Grammar Correction App")

    # Input
    input_string = st.text_area("Enter the input string:")
    
    if st.button("Correct Grammar"):
        # Call the correct_grammar function to get the output
        output = correct_grammar(input_string)

        # Display the results
        st.text(f"Input: {input_string}")
        st.text(f"Output: {output}")

if __name__ == "__main__":
    main()

