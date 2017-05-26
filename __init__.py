#!/usr/bin/env python
from flask_restful import Api, Resource
from flask import Flask, make_response, jsonify
import mod.app, mod.iot, mod.user, mod.dev, database
import MySQLdb

app = Flask(__name__)
api = Api(app)

# Register /USER/ APIs
api.add_resource(mod.user.UserRegister,         '/user/register')
api.add_resource(mod.user.UserAuth,             '/user/auth')
api.add_resource(mod.user.UserSubDate,          '/user/subdate')
api.add_resource(mod.user.UserSubscribe,        '/user/subscribe')
api.add_resource(mod.user.UserChgPass,          '/user/chgpass')

# Register /DEV/ APIs
api.add_resource(mod.dev.DevRegister,           '/dev/register')
api.add_resource(mod.dev.DevAuth,               '/dev/auth')
api.add_resource(mod.dev.DevChgPass,            '/dev/chgpass')
api.add_resource(mod.dev.DevUploadAppInfo,      '/dev/upload/app/info')
api.add_resource(mod.dev.DevUploadAppFile,      '/dev/upload/app/file')
api.add_resource(mod.dev.DevUploadIotInfo,      '/dev/upload/iot/info')
api.add_resource(mod.dev.DevUploadIotFile,      '/dev/upload/iot/file')
api.add_resource(mod.dev.DevRemoveApp,          '/dev/remove/app')
api.add_resource(mod.dev.DevRemoveIot,          '/dev/remove/iot')

# Register /APP/ APIs
api.add_resource(mod.app.AppList,               '/app/all')
api.add_resource(mod.app.AppListDev,            '/app/all/<dev>')
api.add_resource(mod.app.AppAll,                '/app/<name>')
api.add_resource(mod.app.AppTitle,              '/app/<name>/title')
api.add_resource(mod.app.AppAuthor,             '/app/<name>/author')
api.add_resource(mod.app.AppDescription,        '/app/<name>/description')
api.add_resource(mod.app.AppULS,                '/app/<name>/uls')
api.add_resource(mod.app.AppInstall,            '/app/<name>/install')
api.add_resource(mod.app.AppReqOS,              '/app/<name>/reqos')
api.add_resource(mod.app.AppReqArch,            '/app/<name>/reqarch')

# Register /IOT/ APIs
api.add_resource(mod.iot.IotList,               '/iot/all')
api.add_resource(mod.iot.IotListDev,            '/iot/all/<dev>')
api.add_resource(mod.iot.IotAll,                '/iot/<name>')
api.add_resource(mod.iot.IotTitle,              '/iot/<name>/title')
api.add_resource(mod.iot.IotAuthor,             '/iot/<name>/author')
api.add_resource(mod.iot.IotDescription,        '/iot/<name>/description')
api.add_resource(mod.iot.IotULS,                '/iot/<name>/uls')
api.add_resource(mod.iot.IotInstall,            '/iot/<name>/install')
api.add_resource(mod.iot.IotReqOS,              '/iot/<name>/reqos')


# Override Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return make_response('bad request', 400)


@app.errorhandler(401)
def unauthorized(error):
    return make_response('unauthorized', 401)


@app.errorhandler(404)
def not_found(error):
    return make_response('not found', 404)


@app.errorhandler(500)
def internal_server_error(error):
    return make_response('internal server error', 500)


if __name__ == '__main__':
    database.DB = MySQLdb.Connect("cnqc.dtct.cf", "lombax", "itoon#1q2w#", "omniwrench")
    database.CUR = database.DB.cursor()
    database.CURALL = database.DB.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    app.config['UPLOAD_FOLDER'] = '/home/ralf/bvm'
    context = ('/etc/letsencrypt/live/api.ralf.ren/fullchain.pem', '/etc/letsencrypt/keys/0000_key-certbot.pem')
    app.run(host='0.0.0.0', port=443, debug=False, ssl_context=context)
