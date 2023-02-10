gcloud config set project dft-ppd-prt-projectengtracker
gcloud auth login
/home/will/cloud_sql_proxy -instances=dft-ppd-prt-projectengtracker:europe-west1:tracker=tcp:6543