## Deploying webapp to Google Cloud

1. Redeem the free student google cloud credit by following instructions from announcement email a couple weeks back.
2. Install gcloud CLI (https://cloud.google.com/sdk/docs/install).

    **FAQ**: if you're using mac and have the folder in Downloads, run 

    `~/Downloads/google-cloud-sdk/install.sh` instead.

    **FAQ**: if that gives you a 'no permission' error, run

    `sudo ~/Downloads/google-cloud-sdk/install.sh` and enter your macbook password when prompted.
    
    **FAQ**: make sure to open a new terminal after installation before trying out `gcloud --version`.
    
3. Copy this repo into your local computer. Both `git clone` and downloading the zip file works.

4. Inside the code folder `pic16b-mnist-demo`, run 
 ```
conda activate PIC16B
export FLASK_ENV=development
flask run
```
to make sure you're in the correct directory and the code and flask is working. 
Once you've checked that the website is working locally, you can close the flask app.

  **FAQ**: If you get an error message like "port 5000 is in use", make sure no other flask app is running in your laptop, and run `flask run -p 5001` (or any other number than 5000) instead.

5. Now, go to Google Cloud console (https://console.cloud.google.com/) and create a new project. 
Project ID can be anything, and the organization can be "no organization". 
The most important thing is that the billing account is connected to your "education" billing account (which is where your free credit should be at).

6. Assuming your gcloud CLI is correctly installed, go to your terminal and run `gcloud init`. The prompt should be pretty self explanatory - it will ask you to log in and choose your project.

7. Next, run `gcloud run deploy`. You'll see prompts like this:

- Source code location (/Users/harlin/Desktop/16B-W23/lectures/flask/mnist): just hit enter, as long as you're in the same folder where you locally ran the flask app earlier.

- Service name (mnist): just hit enter.

- Please specify a region: type in one of the us-west numbers.

- Whenever it asks you a y/n question about permission, type in y.

- If everything goes smoothly, it should print out some url that looks like https://mnist-[...]-wn.a.run.app/.

**FAQ**: Can I change the weird url? Looks like you can but it's a lot more involved than I initially thought: https://cloud.google.com/run/docs/mapping-custom-domains

**FAQ**: You can deploy multiple times in the same project. My understanding is that you can only delete the deployed app by deleting the entire project. But there's a quota for the number of projects so be careful.

## What you should look for in the website

1. Go to `submit (advanced)` page and upload some of the .txt files from https://github.com/HarlinLee/pic16b-mnist-demo/tree/main/mnist-model/sample-data.

2. Look at the `submit` function in `app.py` and try to understand the general logic.

3. Look at the css files are in the static folder. If you have javascript files, that should also go in there.

4. As before, the jinja template files (and html files) are in the templates folder. This time, some of the templates `extend` the `base.html`, which you can read more about [here](https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/#register) and [here](https://jinja.palletsprojects.com/en/3.1.x/templates/#template-inheritance).

5. When you're working on the web app homework or project, I fully expect you to copy the files from this git repo and modify it.
   You may need to change requirements.txt, but I recommend keeping the `Dockerfile` as is (unless you have a good understanding of what you're doing!).

