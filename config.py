# from sqlalchemy import create_engine,text
# import pymysql
# db_connector_string="mysql+pymysql://vivek_bagul:D6p1mQJnEBnxq4d9nAWytdGAh5yUIhKl@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/job_search_site"

# engine = create_engine(db_connector_string,
#                        connect_args={
#                            "ssl": {
#                                "ca": "./singlestore_bundle.pem"
#                            }
#                        }
#                       )
# print("hello world")
# with engine.connect() as conn:
#   result=conn.execute(text('select * from jobs'))
#   print(result.all())
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://vivek_bagul:D6p1mQJnEBnxq4d9nAWytdGAh5yUIhKl@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/job_search_site?ssl_ca=./singlestore_bundle.pem"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class jobs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  job_name = db.Column(db.String())
  created_date = db.Column(db.Date)
  job_requirments = db.Column(db.String())
  job_responsibilities = db.Column(db.String())


with app.app_context():
  # Fetch all jobs
  all_jobs = jobs.query.all()

  # Print all jobs
print(all_jobs)
