# Each line represents a new layer which is cached: image is re-built faster: 
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/  

# STEP 1: download base image
FROM continuumio/miniconda3:latest

# STEP 2: set project folder
WORKDIR /sunventure

# STEP 3: create conda environment
# Why copy just the environment.yml/requirements.text and not all files (see below COPY . .)
# Docker caches environment.yml, subsequent command to download packages depends on this line
# If the whole folder is copied at this step, any changes in the whole folder will cause the package download
# to NOT use the cached packages, resulting in a long image rebuild time     
COPY ./requirements.txt /sunventure

#adds conda-forge channel to defaults
RUN conda config --append channels conda-forge
RUN conda install --file requirements.txt -q -y

# STEP 4: copy entire folder to project folder
COPY . .

# STEP 5: setting the environment variable for flask run
# RUN export FLASK_APP=microblog.py does not work as it only creates the variable in the intermediate container
# https://stackoverflow.com/questions/39597925/how-do-i-set-environment-variables-during-the-build-in-docker 
ENV FLASK_APP=sunventure.py

# STEP 6: flask run with first_flask_app environment
# can't run conda activate (need to run conda init then close the bash shell), 
# however using conda run allow us to run the 'flask run' command in environment
# --no-capture-output to see stdout from conda run env only available in miniconda 4.9 
# import to set host to 0.0.0.0, public expose the ip addresss to the host machine
# everytime the container starts, entry point commands will be run
# ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "first_flask_app", "flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["./start_app.sh"]


# STEP 6: build image and run app from docker command line
# docker image build -t first_flask_app .
# docker run -p 5000:5000 -d first_flask_app