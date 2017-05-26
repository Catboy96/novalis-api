from flask_restful import Api, Resource
from flask import abort, jsonify, Response, request
import database, datetime, oss2, verify, os
import werkzeug.security as sec

# OSS instance
auth = oss2.Auth("SgTzZLGkSYBsgBdM", "YWp3W4lHZGSSe8QiDPa2qtaiW0CXXA")
bucket = oss2.Bucket(auth, "static.ralf.ren", "bvm")

class DevUploadAppInfo(Resource):
    def post(self):
        try:
            # Invalid request
            if not request.json \
                    or 'mail' not in request.json \
                    or 'pass' not in request.json \
                    or 'name' not in request.json \
                    or 'title' not in request.json \
                    or 'author' not in request.json \
                    or 'description' not in request.json \
                    or 'uls' not in request.json \
                    or 'install' not in request.json \
                    or 'reqos' not in request.json \
                    or 'reqarch' not in request.json \
                    or 'reqvirt' not in request.json \
                    or 'version' not in request.json:
                abort(400)

            # Get information from JSON
            strMail = request.json.get('mail')
            strPass = request.json.get('pass')
            strName = request.json.get('name')
            strTitle = request.json.get('title')
            strAuthor = request.json.get('author')
            strDescription = request.json.get('description')
            strULS = request.json.get('uls')
            strVersion = request.json.get('version')
            strInstall = request.json.get('install')
            strReqOS = request.json.get('reqos')
            strReqArch = request.json.get('reqarch')
            strVirt = request.json.get('reqvirt')

            # Auth
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            # Write database
            database.CUR.execute("INSERT INTO app VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                                 strName,
                                 strTitle,
                                 strAuthor,
                                 strDescription,
                                 strULS,
                                 strVersion,
                                 strInstall,
                                 strReqOS,
                                 strReqArch,
                                 strVirt))
            database.CUR.execute("INSERT INTO appstat VALUES ('%s', '%s', '0')" % (
                                 strName,
                                 datetime.date.today().strftime('%Y-%m-%d')))
            return "ok"
        except:
            abort(500)


class DevUploadAppFile(Resource):
    def post(self, name):
        try:
            if not request.headers \
                    or "mail" not in request.headers \
                    or "pass" not in request.headers \
                    or "name" not in request.headers \
                    or "file" not in request.headers:
                abort(400)
            if not request.files:
                abort(400)
            strMail = request.headers.get("mail")
            strPass = request.headers.get("pass")
            strName = request.headers.get("name")
            strFile = request.headers.get("file")


            # Auth
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            # Check for record exists
            database.CUR.execute("SELECT title FROM app WHERE name = '%s'" % strName)

            # Check for file
            file = request.files[strFile]
            if file and verify.AllowedFile(file.filename):
                file.save('/root/bvm/' + strName + '.' + strFile)

            # Upload
            bucket.put_object_from_file("app/" + strName + '.' + strFile)

            # Remove temp file
            os.remove('/root/bvm/' + strName + '.' + strFile)

            return "ok"
        except:
            abort(500)


class DevUploadIotInfo(Resource):
    def post(self):
        try:
            # Invalid request
            if not request.json \
                    or 'mail' not in request.json \
                    or 'pass' not in request.json \
                    or 'name' not in request.json \
                    or 'title' not in request.json \
                    or 'author' not in request.json \
                    or 'description' not in request.json \
                    or 'uls' not in request.json \
                    or 'install' not in request.json \
                    or 'reqos' not in request.json \
                    or 'version' not in request.json:
                abort(400)

            # Get information from JSON
            strMail = request.json.get('mail')
            strPass = request.json.get('pass')
            strName = request.json.get('name')
            strTitle = request.json.get('title')
            strAuthor = request.json.get('author')
            strDescription = request.json.get('description')
            strULS = request.json.get('uls')
            strVersion = request.json.get('version')
            strInstall = request.json.get('install')
            strReqOS = request.json.get('reqos')


            # Auth
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            # Write database
            database.CUR.execute("INSERT INTO iot VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                                 strName,
                                 strTitle,
                                 strAuthor,
                                 strDescription,
                                 strULS,
                                 strVersion,
                                 strInstall,
                                 strReqOS))
            database.CUR.execute("INSERT INTO iotstat VALUES ('%s', '%s', '0')" % (
                                 strName,
                                 datetime.date.today().strftime('%Y-%m-%d')))
            return "ok"
        except:
            abort(500)


class DevUploadIotFile(Resource):
    def post(self, name):
        try:
            if not request.headers \
                    or "mail" not in request.headers \
                    or "pass" not in request.headers \
                    or "name" not in request.headers \
                    or "file" not in request.headers:
                abort(400)
            if not request.files:
                abort(400)
            strMail = request.headers.get("mail")
            strPass = request.headers.get("pass")
            strName = request.headers.get("name")
            strFile = request.headers.get("file")


            # Auth
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            # Check for record exists
            database.CUR.execute("SELECT title FROM iot WHERE name = '%s'" % strName)

            # Check for file
            file = request.files[strFile]
            if file and verify.AllowedFile(file.filename):
                file.save('/root/bvm/' + strName + '.' + strFile)

            # OSS instance
            auth = oss2.Auth("SgTzZLGkSYBsgBdM", "YWp3W4lHZGSSe8QiDPa2qtaiW0CXXA")
            bucket = oss2.Bucket(auth, "static.ralf.ren", "bvm")

            # Upload
            bucket.put_object_from_file("iot/" + strName + '.' + strFile)

            # Remove temp file
            os.remove('/root/bvm/' + strName + '.' + strFile)

            return "ok"
        except:
            abort(500)


class DevRegister(Resource):
    def post(self):
        if not request.json or 'mail' not in request.json or 'pass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strPass = request.json.get('pass')
        strName = request.json.get('name')
        try:
            database.CUR.execute("INSERT INTO dev VALUES ('%s', '%s', '%s', '%s')" % (
                                 strMail,
                                 strPass,
                                 strName,
                                 datetime.date.today().strftime('%Y-%m-%d')))
            return "ok"
        except:
            abort(500)


class DevAuth(Resource):
    def post(self):
        if not request.json or 'mail' not in request.json or 'pass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strPass = request.json.get('pass')
        try:
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                return "ok"
            else:
                return "failed"
        except:
            abort(500)


class DevChgPass(Resource):
    def post(self):
        if not request.json or 'mail' not in request.json or 'oldpass' not in request.json or not 'newpass' not in request.json:
            abort(400)
        strMail = request.json.get('mail')
        strOld = request.json.get('oldpass')
        strNew = request.json.get('newpass')
        # AUTH
        database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
        strHash = database.CUR.fetchone()[0]
        if sec.check_password_hash(strHash, strOld) == False:
            abort(401)
        try:
            database.CUR.execute("UPDATE dev SET pass = '%s' WHERE mail = '%s'" % (
                                 sec.generate_password_hash(strNew),
                                 strMail))
            return "ok"
        except:
            abort(500)


class DevRemoveIot(Resource):
    def post(self):
        try:
            # Invalid request
            if not request.json \
                    or "mail" not in request.json \
                    or "pass" not in request.json \
                    or "name" not in request.json:
                abort(400)

            # Get information from JSON
            strMail = request.json.get('mail')
            strPass = request.json.get('pass')
            strName = request.json.get('name')

            # Auth
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            # Remove from database
            database.CUR.execute("DELETE FROM iot WHERE name='%s'" % strName )
            database.CUR.execute("DELETE FROM iotstat WHERE name='%s'" % strName)

            # Remove from OSS
            bucket.delete_object("iot/" + strName + ".png")
            bucket.delete_object("iot/" + strName + ".install.sh")
            bucket.delete_object("iot/" + strName + ".uninstall.sh")
            return "ok"

        except:
            abort(500)


class DevRemoveApp(Resource):
    def post(self):
        try:
            # Invalid request
            if not request.json \
                    or "mail" not in request.json \
                    or "pass" not in request.json \
                    or "name" not in request.json:
                abort(400)

            # Get information from JSON
            strMail = request.json.get('mail')
            strPass = request.json.get('pass')
            strName = request.json.get('name')

            # Auth
            database.CUR.execute("SELECT pass FROM dev WHERE mail = '%s'" % strMail)
            strHash = database.CUR.fetchone()[0]
            if sec.check_password_hash(strHash, strPass) == False:
                abort(401)

            # Remove from database
            database.CUR.execute("DELETE FROM app WHERE name='%s'" % strName )
            database.CUR.execute("DELETE FROM appstat WHERE name='%s'" % strName)

            # Remove from OSS
            bucket.delete_object("app/" + strName + ".png")
            bucket.delete_object("app/" + strName + ".install.sh")
            bucket.delete_object("app/" + strName + ".uninstall.sh")
            return "ok"

        except:
            abort(500)
