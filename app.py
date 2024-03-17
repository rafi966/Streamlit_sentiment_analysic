from textblob import TextBlob
import pandas as pd 
import streamlit as st 
import cleantext 



st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text: 
        blob = TextBlob(text)
        st.write('polarity: ',round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2)) 


    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all = False, extra_spaces=True , stopwords=True , lowercase=True , punct=True))
       
with st.expander('Analyze csv'):
    Upl = st.file_uploader('Upload file') 

    def Ratings(x):
        blob1 = TextBlob(x)   
        return blob1.sentiment.polarity


    def analyze(x):
        if x>= 0.5:
            return 'Positive'
        elif x<= -0.5:
            return 'Negative'
        else:
            return 'Neutral'
        
    if Upl: 

      # Read the Excel file into a DataFrame
        df = pd.read_excel(Upl)

        # Drop any unnecessary columns
        df = df[['Ratings', 'Cleaned Review Text']]

        # Display the DataFrame
        st.write(df.head(10))

       # df = pd.read_excel(Upl)
       # del df['Unnamed: 0']
       # df['Score'] = df['tweets'].apply(score)          ##########
       # df['analysis'] = df['score'].apply(analyze)      ################
       # st.write(df.head())


        @st.cache
        def convert_df(df):
            return df.to_csv().encode('Utf-8')
        

        csv = convert_df(df)
        
        st.download_button(
            label="Download data as CSV",
            data =csv,
            file_name='sentiment_c.csv', ##########
            mime='text/csv'
        )
