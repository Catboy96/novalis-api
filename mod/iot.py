from flask_restful import Api, Resource
from flask import abort, jsonify, Response
import database


class IotList(Resource):
    def get(self):
        try:
            database.CURALL.execute("SELECT name FROM iot")
            return jsonify(database.CURALL.fetchall())
        except:
            abort(404)


class IotListDev(Resource):
    def get(self, dev):
        try:
            database.CURALL.execute("SELECT name FROM iot WHERE author = '%s'" % dev)
            return jsonify(database.CURALL.fetchall())
        except:
            abort(404)


class IotAll(Resource):
    def get(self, name):
        try:
            database.CURALL.execute("SELECT * FROM iot WHERE name = '%s'" % name)
            return jsonify(database.CURALL.fetchall()[0])
        except:
            abort(404)


class IotAllTitle(Resource):
    def get(self, name):
        try:
            name = name.replace('_', ' ')
            database.CURALL.execute("SELECT * FROM iot WHERE title = '%s'" % name)
            return jsonify(database.CURALL.fetchall()[0])
        except:
            abort(404)


class IotTitle(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT title FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class IotAuthor(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT author FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class IotDescription(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT description FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class IotULS(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT uls FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class IotInstall(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT install FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class IotReqOS(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT reqos FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)
