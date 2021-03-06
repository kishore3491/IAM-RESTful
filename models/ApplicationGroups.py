from dbconfig import db


class ApplicationGroup(db.Model):
    __tablename__ = 'appgroups'

    applicationID = db.Column(db.INTEGER, db.ForeignKey('applications.id'), primary_key=True)
    groupID = db.Column(db.INTEGER, db.ForeignKey('groups.id'), primary_key=True)

    def __init__(self, applicationID, groupID):
        self.applicationID = applicationID
        self.groupID = groupID

    def __repr__(self):
        return ApplicationGroup
