from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, make_response, session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import httplib2
import json
import requests

app = Flask(__name__)

# Home route
@app.route('/')
@app.route('/category')
def showCategories():
    return "Show categories"


# Edit category
@app.route('/category/new')
def newCategory():
    return "New category"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
