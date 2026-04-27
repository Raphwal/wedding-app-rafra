import streamlit as st
import streamlit.components.v1 as components


form_url = "https://forms.gle/y2YtYHRe11mX2RLr6"

st.markdown(f"""
## Liebe Gäste,
wir freuen uns, am **27.09.2025** mit euch im Landhaus [Alte Scheune](https://www.alte-scheune.de/) unsere Hochzeit zu feiern!
Alle wichtigen Informationen haben wir hier zusammengestellt. Damit auch wir die beste Feier für euch planen können, bitten wir euch bis spätestens zum **15.05.2025** eure Rückmeldungen über folgendes [Google Formular]({form_url}) zu geben.
Wir haben das Formular auch für euch eingebettet.

Solltet ihr versehentlich eine falsche Angabe gemacht haben, füllt das Formular einfach erneut aus. Wir werten die jüngste Rückmeldung aus.

**Liebe Grüße**<br>
Neda & Peter
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
### Rückmeldeformular
""")

components.html(f"""
    <style>
        .responsive-iframe-container {{
            position: relative;
            width: 100%;
            height: 0;
            padding-bottom: 150%; /* Adjust based on content ratio */
            overflow: hidden;
        }}
        .responsive-iframe-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 2px solid #ccc;
            border-radius: 10px;
        }}
    </style>

    <div class="responsive-iframe-container">
        <iframe
            src="{form_url}"
            frameborder="0"
            marginheight="0"
            marginwidth="0">
        </iframe>
    </div>
    """,
    height=900,
)