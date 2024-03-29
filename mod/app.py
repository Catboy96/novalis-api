from flask_restful import Api, Resource
from flask import abort, jsonify, Response
import database


class AppList(Resource):
    def get(self):
        try:
            database.CURALL.execute("SELECT name FROM app")
            return jsonify(database.CURALL.fetchall())
        except:
            abort(404)


class AppListDev(Resource):
    def get(self, dev):
        try:
            database.CURALL.execute("SELECT name FROM app WHERE author = '%s'" % dev)
            return jsonify(database.CURALL.fetchall())
        except:
            abort(404)


class AppAll(Resource):
    def get(self, name):
        try:
            database.CURALL.execute("SELECT * FROM app WHERE name = '%s'" % name)
            return jsonify(database.CURALL.fetchall()[0])
        except:
            abort(404)


class AppAllTitle(Resource):
    def get(self, name):
        try:
            name = name.replace('_', ' ')
            database.CURALL.execute("SELECT * FROM app WHERE title = '%s'" % name)
            return jsonify(database.CURALL.fetchall()[0])
        except:
            abort(404)


class AppTitle(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT title FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class AppAuthor(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT author FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class AppDescription(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT description FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class AppULS(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT uls FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class AppInstall(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT install FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class AppReqOS(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT reqos FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)


class AppReqArch(Resource):
    def get(self, name):
        try:
            database.CUR.execute("SELECT reqarch FROM app WHERE name = '%s'" % name)
            result = database.CUR.fetchone()[0]
            return result
        except:
            abort(404)
