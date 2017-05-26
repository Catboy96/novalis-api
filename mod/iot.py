from flask_restful import Api, Resource
from flask import abort, jsonify, Response
import database


class IotList(Resource):
    def get(self):
        try:
            database.CURALL.execute("SELECT name FROM iot")
            return jsonify(database.CURALL.fetchall())
        except:
            abort(500)


class IotListDev(Resource):
    def get(self, dev):
        try:
            database.CURALL.execute("SELECT name FROM iot WHERE author = '%s'" % dev)
            return jsonify(database.CURALL.fetchall())
        except:
            abort(500)


class IotAll(Resource):
    def get(self, name):
        try:
            database.CURALL.execute("SELECT * FROM iot WHERE name = '%s'" % name)
            return jsonify(database.CURALL.fetchall()[0])
        except:
            abort(500)


class IotTitle(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT title FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(500)


class IotAuthor(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT author FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(500)


class IotDescription(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT description FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(500)


class IotULS(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT uls FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(500)


class IotInstall(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT install FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(500)


class IotReqOS(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT reqos FROM iot WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(500)
