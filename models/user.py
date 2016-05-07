# !/usr/bin/env python
# coding=utf8
# Author: quheng

from manager import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    @staticmethod
    def get_users():
        return User.query.all()

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return '<User %r>' % (self.nickname)
