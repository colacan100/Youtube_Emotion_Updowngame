
from flask import Flask, copy_current_request_context, render_template, request
from pymongo import MongoClient
import secrets
from random import randrange,choice
from bson.objectid import ObjectId
#from PyMongo import MongoClient

app = Flask(__name__, static_url_path="/static")
#app.config['MONGO_URI']= "mongodb://3.37.202.252:27017/youtube_comment_database"
#mongo=PyMongo(app)
#mydb = mongo['youtube_comment_comment']
# -------------------------------------------------
#cluster = MongoClient("mongodb+srv://harim:<password>@youtube-comment-cluster.vg6ok.mongodb.net/?retryWrites=true&w=majority")
# -------------------------------------------------
mongo= MongoClient("mongodb://3.37.202.252:27017")
db = mongo['youtube_comment_database']
col = db['youtube_comment_collection']

image_id = '62c435ce295b8b83703bf5a1'
emotion_id = '62c2f41206c7162af6c94639'
emotion_list= ['행복','슬픔','놀람','분노','중립','혐오','공포']
emtoion_dict= {'행복':1,'슬픔':2,'놀람':3,'분노':4,'중립':5,'혐오':6,'공포':7}

@app.route('/')
def homepage():
    return render_template('index.html')

cnt = 1
movie1 = ''
@app.route('/main')
def main(cnt = 1, my_score=0):
    #ns = request.args.get('namespace', default = 'ns-abc-aaa', type = str)
    cnt = request.args.get('cnt', default = 0, type = int)
    my_score = request.args.get('my_score', default = 0, type = int)
    ans = request.args.get('ans', default = '', type = str)
    emotion_ = request.args.get('emotion_', default = '', type = str)
    movie1_emotion = request.args.get('movie1_emotion', default = '', type = str)
    movie2_emotion = request.args.get('movie2_emotion', default = '', type = str)
    print('!',cnt, ans, emotion_, movie1_emotion, movie2_emotion, 'my_score :', my_score)
    if ans !='' :
        my_score=score(ans, movie1_emotion, movie2_emotion, my_score)
    if cnt < 5 :
        emotion_ = emotion()
        movie1, movie2=chooseMovie()
        image1=showImage(movie1)
        image2=showImage(movie2)
        movie1_emotion = movieEmotion(movie1, emotion_)
        movie2_emotion = movieEmotion(movie2, emotion_)
        cnt +=1
        return render_template(
            'main.html',
            emotion_=emotion_, 
            movie1=movie1,
            movie2=movie2,
            image1=image1,
            image2=image2,
            movie1_emotion = movie1_emotion,
            movie2_emotion = movie2_emotion,
            cnt=cnt,
            my_score=my_score
            )
    else : 

        return render_template('results.html', my_score = my_score)
#--- Choose Randomized Two Films ---#
def chooseMovie():
    x = col.find_one({'_id':ObjectId(image_id)},{'_id':0})
    movie1 = secrets.choice([i for i in x])
    x = col.find_one({'_id':ObjectId(image_id)},{'_id':0})
    movie2 = secrets.choice([i for i in x])
    if movie1 == movie2 :
        chooseMovie()
    return movie1, movie2

#--- Input Image ---#
def showImage(movie):
    x = col.find_one({'_id':ObjectId(image_id)},{'_id':0})
    x = x[movie][1]
    return x

#--- Choose Randomized Emotion ---#
def emotion():
    emotion_ = secrets.choice(emotion_list)
    return emotion_

def movieEmotion(movie, emotion_):
    emotion_list1 = []
    new_name = movie + 'emotion'
    x = col.find({'_id':ObjectId(emotion_id)},{'_id':0})
    x = x[0][new_name][emotion_]
    return x

#--- Choose Correct Answer ---#
# def answer():
#     correct = '/#'
#     wrong = '/result'
#     if chooseMovie() > chooseMovie2():
#         up = correct
#         down = wrong
#         return up, down
#     elif chooseMovie() < chooseMovie2():
#         up = wrong
#         down = correct
#         return up, down

#     else:
#         up = correct
#         down = correct
#         return up, down

#--- 제출용 ---#
# def randnum():
#     return randrange(0,30,1)

#--- My score ---#
def score(ans, movie1_emotion, movie2_emotion, my_score = 0):
    movie1_emotion = float(movie1_emotion)
    movie2_emotion = float(movie2_emotion)
    print('xx', movie1_emotion, movie2_emotion)
    if movie1_emotion > movie2_emotion: 
        if ans == 'down':   # right
            my_score += 20
            return my_score
        else :              # wrong
            return my_score
    elif movie1_emotion < movie2_emotion:
        if ans == 'up':     # right
            my_score += 20
            return my_score
        else :              # wrong
            return my_score
    else :                  # same
        my_score += 20
        return my_score

def end_game():
    return result()

@app.route('/results')
def result():
    return render_template('results.html', score_=score())


if __name__ == '__main__':
    app.run(debug=True)