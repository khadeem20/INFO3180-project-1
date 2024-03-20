from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    numBedrooms = db.Column(db.Integer)
    numBathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Float)
    pType = db.Column(db.String(10))
    desc = db.Column(db.String(300))
    fileName = db.Column(db.String(128), unique=True)

    def __init__ (self, title, numBathrooms, numBedrooms, location, price, pType, desc, fileName):
        self.title = title
        self.numBedrooms = numBedrooms
        self.numBathrooms = numBathrooms
        self.location = location
        self.price = price
        self.pType= pType
        self.desc = desc
        self.fileName = fileName

    def __repr__(self):
        return '<Property %r>' % (self.title)