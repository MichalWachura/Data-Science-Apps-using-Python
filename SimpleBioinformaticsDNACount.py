
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

#Page Title

#image = Image.open("C:\Users\USER\Desktop\StreamLit_DataScience\dna-logo.jpg")

#st.image(image,use_column_width=True)

st.write("""
DNA Nucleotide Count Web App
This app counts the nucelotide composition of querry DNA

***
""")

st.header("Enter DNA sequence")

sequence_input = ">DNA QUERRY\nGAGAGAGAGAGAGGGAGAGGGGGGGGGATAGTAGTAGATGATGTAGTATGTGATGTGTGCGCGCGCGCTAGCTACGTACGTGCTATATATAATTCG"

sequence = st.text_area("Sequnce Input :",sequence_input,height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]#skip the seqeunce name
sequence = "".join(sequence)

st.write("""
***
""")

#prints the input DNA Sequnece
st.header("INPUT(DNA Query)")
sequence

#DNA nucleotide count
st.header("Output(DNA Nucletide Count")

# 1. print dictionary

st.subheader("1. Print dictionary")
def DNA_nuckleotide_count(seq):
    d = dict(
        [
            ("A",seq.count("A")),
            ("T", seq.count("T")),
            ("G", seq.count("G")),
            ("C", seq.count("C")),

        ]

    )
    return d

x = DNA_nuckleotide_count(sequence)
x_label = list(x)
x_values = list(x.values())

#this just print data like print() in streamlit
x
x_values
x_label

# 2 Print Text
st.subheader('2.Print text')
st.write("there are  " + str(x["A"]) + " adenine (A)")
st.write("there are  " + str(x["T"]) + " adenine (T)")
st.write("there are  " + str(x["G"]) + " adenine (G)")
st.write("there are  " + str(x["C"]) + " adenine (C)")


# 3. Display Data Frame
st.subheader("3. Display Data Frame")
df = pd.DataFrame.from_dict(x,orient='index')
df = df.rename({0:"count"},axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index":"nucleotide"})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart using Altair')
p = alt.Chart(df).mark_bar().encode(x="nucleotide",y="count")
p = p.properties(width=alt.Step(80))
st.write(p)