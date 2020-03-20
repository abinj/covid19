pip install pymysql

pip install apache-airflow[mysql]

pip install mysqlclient

pip install --upgrade setuptools


pip install apache-airflow[celery]


#####
export AIRFLOW_HOME=airflow_home

airflow initdb


#References: https://airflow-tutorial.readthedocs.io/en/latest/first-airflow.html
             https://big-data-demystified.ninja/2019/10/03/airflow-mysql-integration-how-to/
             https://stackoverflow.com/questions/15701636/how-to-enable-explicit-defaults-for-timestamp
             https://airflow.apache.org/docs/stable/installation.html



To Run the Stanford NLP sentiment Analyzer
wget https://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip https://nlp.stanford.edu/software/stanford-english-corenlp-2018-10-05-models.jar
unzip stanford-corenlp-full-2018-10-05.zip
mv stanford-english-corenlp-2018-10-05-models.jar stanford-corenlp-full-2018-10-05
cd stanford-corenlp-full-2018-10-05
java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000


             