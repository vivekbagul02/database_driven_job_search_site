from sqlalchemy import create_engine,text
import pymysql
db_connector_string="mysql+pymysql://vivek_bagul:D6p1mQJnEBnxq4d9nAWytdGAh5yUIhKl@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/job_search_site"

engine = create_engine(db_connector_string,
                       connect_args={
                           "ssl": {
                               "ca": "./singlestore_bundle.pem"  
                           }
                       }                  
                      )
print("hello world")
with engine.connect() as conn:
  result=conn.execute(text('select * from jobs'))
  print(result.all())

