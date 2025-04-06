#!/usr/bin/env python3

import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

# create the server
server = Flask(__name__)
server.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

mongo = PyMongo(server)

# we use this to handle large files instead of using the classic BSON
fs = gridfs.GridFS(mongo.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

# take an email and a password and return a token
@server.route("/login",  methods=["POST"])
def login():
	token, err = access.login(request)
	
	if not err:
		return token
	else:
		return err
	
@server.route("/login", methods=["POST"])
def upload():
	access, err = validate.token(request)
	
	# convert to a python object
	access = json.loads(access)
	
	if access["admin"]:
		if len(request.files) > 1 or len(request.files) < 1:
			return "exactly 1 file required", 400
		
		for _, f in request.files.items():
			err = util.upload(f, fs, channel, access)
			
			if err:
				return err
			
		return "success!", 200
	else:
		return "Not authorized", 401

@server.route("/download", methods=["GET"])
def download():
	pass
	