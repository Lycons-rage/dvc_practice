# **DVC SETUP STEPS AND NOTES**

##### *(Make sure python 3.0+ and pip is installed in the system)*
### Create an environment 
```
conda create -p env python=<python_version_here> -y
```

### Activate the environment
```
conda activate <absolute_location_of_env_folder>
```

### Install all the required libraries 
```
pip install -r requirements.txt
```

### Whats and whys of Data Version Control (DVC) :
 - DVC is an open-source tool for data versioning
 - SVC (Source Version Control) or SCM (Source Code Management) is a technique for versioning our project
 - Project Components can be categorised into Versions chronologically, tracking all the changes 
 - Git, GitLab, Code Commit (by AWS) are an example of SVC, where source is synchronised into local repo and then committed into the cloud
 - DVC can be used for :
    - Re-producablity
    - Managing and versioning large dataset and mmachine learning model
    - We cannot use DVC alone, we have to use Git first then we can use DVC along with Git
    - Experiment Tracking
    - Efficient Storage
 - .dvc directory must be created inside our project, inside which there is .dvc/cache, .dvc/temp, .dvc/state files
 - dvc.yaml, conatins entire config of dvc
 - .dvcignore, pretty self-explainatory
 - dvc.lock, tracking each and every experiment
 - data.dvc file, storing data and version in terms of dvc, name can be anything but extension must be .dvc 
 - .dvcconfig
 - something similar to git, no?!
 - we created pipelines manually in our diamond_price_predictor project, that can be automated using dvc

### Commands of DVC :
 - ```dvc init``` : to initialise a new dvc project in current directory
 - ```dvc add``` : to add a file into dvc project
 - ```dvc repro``` : to reproduce multiple time and is directly connected to dvc.yaml file which stores all the config
 - ```dvc remote add public_url``` : to connect to remote location
 - ```dvc push``` : to push to the remote location
 - ```dvc pull``` : to pull from the remote location
 - ```dvc dag``` : to visualise a directed acyclic graph of our dependencies

### How to(s) of DVC:
 - run ```dvc init``` to initialise a local dvc project
 - you'll see a .dvc directory created in your project along
 - prepare the project files in sequential stages or phases
 - create a dvc.yaml file and set commands to be executed, stage dependencies and their respective outputs
 - run ```dvc repro``` to execute the stages 
 - stages will be executed in the config specified in dvc.yaml file
 - dvc.lock file will be created inside the root project directory in which all the info regarding stages' execution can be found
 - all the respective output will be stored in cache inside .dvc directory
 - run ```dvc dag``` to visualise a directed acyclic graph or dependencies