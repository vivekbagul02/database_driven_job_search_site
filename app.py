from flask import Flask, render_template, jsonify

app = Flask(__name__)

all_jobs_list = [{
    "job_id": 101,
    'position': 'Python Developer',
    "location": "Pune,Maharashtra",
    "salary": "Rs. 12,00,000"
}, {
    "job_id": 102,
    'position': 'Data Scientist',
    "location": "Pune,Maharashtra",
    "salary": "Rs. 12,00,000"
}, {
    "job_id": 103,
    'position': 'Python AWS',
    "location": "Pune,Maharashtra",
    "salary": "Rs. 12,00,000"
}, {
    "job_id": 104,
    'position': 'Data Analyst',
    "location": "Pune,Maharashtra"
}, {
    "job_id": 105,
    'position': 'Python Automation Engineer',
    "location": "Pune,Maharashtra",
    "salary": "Rs. 12,00,000"
}]



@app.route("/")
def home_page():
  all_jobs = jsonify(all_jobs_list)

  return render_template("home.html", all_jobs_list=all_jobs_list)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
from replit import db
from replit import db
from replit import db
from replit import db
from replit import db
from replit import db
db["key"] = "value"
