# Write methods to log hits and get number of hits in past 'x' minutes. 


#when user visits, add visit to database with timestamp
#find current time
#query database for count of records between now - 5 minutes and now

###OR###

#every minute add a visit row to database
#when user visits, update row to reflect additional user
#query database for last n rows, find sum of user visits

##OR##

#keep a queue of users from last n minutes (collections.deque)
#once the first user's time is < n minutes ago, delete them


##OR##

#keep a fixed length queue of 60
#every second, delete first item of queue, and append count of users in second
#import time
#time.sleep(1)

###additional sidenote: distributed system. Multiple machines run same code for
###different users(maybe distributed by hash)
###each machine returns a counter, and server adds them together

#MODEL.PY
db = SQLAlchemy()

class UserVisits(db.Model):

    __tablename__ = "user_visits"

    time_id = db.Column(db.Integer, autoincrement=True, primarykey=True)
    time = db.Column(db.DateTime, nullable=False)
    visits = db.Column (db.Integer, nullable=True)

    def __repr__(self):

        return "<UserVisits time_id=%s visits=%s" % (self.time_id, self.visits)


#APP.PY
import datetime
def add_visits():

    #if current time - time of last entry in db > 60 seconds
        # create new row in user_visits table and add 1
    #else, update most recent row's visits adding 1

    current_time = datetime.datetime.now()

    last_entry = db.session.query(UserVisits).order_by(desc(UserVisits.time)).one()
    last_time = last_entry.time

    if current_time - db_time > 60:
        user_visit = UserVisits(time=current_time, visits=1)
        db.session.add(user_visit)
        db.session.commit()

    else:
        last_time.visits += 1
        db.session.commit()



def count_visits(minutes):

    #return visits for 5 last rows
    #find sum of all visits

    visits = db.session.query(UserVisits.visits).order_by(UserVisits.time.desc).limit(minutes).all()

    # sql = "SELECT visits FROM user_visits ORDER BY time DESC LIMIT minutes"
    # cursor = db.session.execute(sql)
    # visits = cursor.fetchall()

    visits = [visits[0] for visit in visits]

    return sum(visits)

