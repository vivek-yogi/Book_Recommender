from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd


popular_df        = pd.read_pickle('C:\\Users\\Admin\\Projects\\Book Recommender\\popular.pkl')
pt                = pd.read_pickle('C:\\Users\\Admin\\Projects\\Book Recommender\\pt.pkl')
books             = pd.read_pickle('C:\\Users\\Admin\\Projects\\Book Recommender\\books.pkl')
similarity_scores = pd.read_pickle('C:\\Users\\Admin\\Projects\\Book Recommender\\similarity_scores.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            book_name = list(popular_df['title'].values),
                            author    = list(popular_df['author'].values),
                            image     = list(popular_df['image_url'].values),
                            votes     = list(popular_df['num_ratings'].values),
                            rating    = list(popular_df['avg_ratings'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input    = request.form.get('user_input')
    index         = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('title')['title'].values))
        item.extend(list(temp_df.drop_duplicates('title')['author'].values))
        item.extend(list(temp_df.drop_duplicates('title')['image_url'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)