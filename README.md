# Boardgamegeek-review-rating-predictor using SVM

This project compares Naïve Bayes and SVM and then selects SVM classifier model  to predect rating of a comment on game review dataset .

# Deploy Flask Implementation Using AWS EC2
-	Download repository.
-	Download data from here: https://www.kaggle.com/jvanelteren/boardgamegeek-reviews
-	Now make aws account and then launch EC2 instance.
-	use this command to copy all files of your flask app to EC2 instance: scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx- xxx.compute-1.amazonaws.com:path/to/file
-	Use command pip install -r /path/to/requirements.txt and install all requirements in your instance.
-	Run command sudo python3 app.py
-	You must use python3 and pip3 for linux instance.
-	Now go on aws and using Public DNS (IPv4) you can see your application.

