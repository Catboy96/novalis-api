from flask_restful import Api, Resource
from flask import abort, jsonify, Response, request
import database, datetime
import werkzeug.security as sec


class UserRegister(Resource):
    def post(self):
        if not request.json or 'mail' not in request.json or 'pass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strPass = request.json.get('pass')
        try:
            database.CUR.execute("INSERT INTO user VALUES ('%s', '%s', '%s', '')" % (
                                 strMail,
                                 sec.generate_password_hash(strPass),
                                 datetime.date.today().strftime('%Y-%m-%d')))
            return "ok"
        except:
            abort(500)


class UserAuth(Resource):
    def post(self):
        if not request.json or 'mail' not in request.json or 'pass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strPass = request.json.get('pass')
        try:
            database.CUR.execute("SELECT pass FROM user WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == True:
                return "ok"
            else:
                return "failed"
        except:
            abort(500)


class UserSubDate(Resource):
    def post(self):
        if not request.json or 'mail' not in request.json or 'pass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strPass = request.json.get('pass')
        try:
            # AUTH
            database.CUR.execute("SELECT pass FROM user WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            database.CUR.execute("SELECT subdate FROM user WHERE mail = '%s'" % strMail)
            strSub =  database.CUR.fetchone()[0]
            if strSub == "":
                return "null"
            else:
                return strSub
        except:
            abort(500)


class UserSubscribe(Resource):
    def post(self):
            if not request.json \
                    or 'mail' not in request.json \
                    or 'pass' not in request.json \
                    or 'method' not in request.json \
                    or 'key' not in request.json:
                abort(400)
            strMail = request.json.get('mail')
            strPass = request.json.get('pass')

            try:
                # AUTH
                database.CUR.execute("SELECT pass FROM user WHERE mail = '%s'" % strMail)
                strHash = database.CUR.fetchone()
                if sec.check_password_hash(strHash, strPass) == False:
                    abort(401)

                database.CUR.execute("UPDATE user SET subdate = '%s' WHERE mail = '%s'" % (
                                     datetime.date.today().strftime('%Y-%m-%d'),
                                     strMail))
                return "ok"
            except:
                abort(500)


class UserChgPass(Resource):
    def post(self):
        if not request.json \
                or 'mail' not in request.json \
                or 'oldpass' not in request.json \
                or not 'newpass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strOld = request.json.get('oldpass')
        strNew = request.json.get('newpass')
        # AUTH
        database.CUR.execute("SELECT pass FROM user WHERE mail = '%s'" % strMail)
        strHash = database.CUR.fetchone()[0]
        if sec.check_password_hash(strHash, strOld) == False:
            abort(401)
        try:
            database.CUR.execute("UPDATE user SET pass = '%s' WHERE mail = '%s'" % (
                                 sec.generate_password_hash(strNew),
                                 strMail))
            return "ok"
        except:
            abort(500)
