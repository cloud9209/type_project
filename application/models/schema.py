from application import db
class User(db.Model) :
  id            = db.Column(db.Integer, primary_key = True)
  email         = db.Column(db.String(60))
  username      = db.Column(db.String(45))
  password      = db.Column(db.String(100))

# class Follow(db.Model):
#   id          = db.Column(db.Integer, primary_key=True)
#   follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#   follower    = db.relationship('User', foreign_keys=[follower_id], backref = db.backref('followees', cascade='all, delete-orphan', lazy='dynamic'))
#   followee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#   followee    = db.relationship('User', foreign_keys=[followee_id], backref = db.backref('followers', cascade='all, delete-orphan', lazy='dynamic'))
#   __table_args__ = ( db.UniqueConstraint('follower_id', 'followee_id', name='uniq_follow'), )

# class Post(db.Model):
#   id          = db.Column(db.Integer, primary_key = True)
#   user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
#   user        = db.relationship('User',foreign_keys = [user_id], backref  = db.backref('posts_by_user', cascade = 'all, delete-orphan', lazy = 'dynamic') )
#   title       = db.Column(db.String(100))
#   description = db.Column(db.String(100))
#   url         = db.Column(db.String(100))
#   summary     = db.Column(db.String(100))
#   img_src     = db.Column(db.String(1000))
#   hearts_count= db.Column(db.Integer, default = 0 )
#   edited_time = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
#   created_time= db.Column(db.DateTime, default = db.func.now())