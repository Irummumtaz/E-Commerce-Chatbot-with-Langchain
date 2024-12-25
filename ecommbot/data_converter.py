import pandas as pd
from langchain_core.documents import Document

def data_converter():
    product_data=pd.read_csv(r'D:\\Data Science\\E-Commerce-Chatbot-with-Langchain\\data\\flipkart_product_review.csv')
    data=product_data[['product_title','review']]

    product_list=[]

    #iterate over the row of dataframe 
    for index,row in data.iterrows():
        #construct an object with poduct name and review attribute
        obj={
            'product_name':row['product_title'],
            'review':row['review']
        }
        #append the object to the list
        product_list.append(obj)

    docs=[]
    for entry in product_list:
        metadata={'product_name':entry['product_name']}
        doc=Document(page_content=entry['review'],metadata=metadata)
        docs.append(doc)
    return docs