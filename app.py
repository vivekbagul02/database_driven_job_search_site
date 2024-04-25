import config
from config import *


@app.route("/")
def home_page():
  all_jobs = config.all_jobs()

  return render_template("home.html", all_jobs_list=all_jobs)


@app.route("/job_discription/<id>")
def job_discription(id):
  result = job_details(id)
  print('result', result)
  return render_template("job_discription.html", job_detail=result)


print(all_jobs)
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
