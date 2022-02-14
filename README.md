# SSA_Chatbot

## How to Get the Bot running by Using the Github Code
Firstly clone the repo locally or Download the source code.

After getting the source code you need to install python and rasa on to your system. Our recommendation is to download python using miniconda or Anaconda.

> Link for miniconda: https://docs.conda.io/en/latest/miniconda.html

> Link for Anaconda: https://www.anaconda.com/products/individual

After installing the python, it is recommended to create a seperate environment for RASA and install the required libraries into it.( Sometimes the libraries versions may differ for differnet packeges which might cause some dependency issues while using rasa )

Command to create a new Env.

> conda create -n \<Name of Environment> python=3.7

> conda create -n SSA python=3.7

Once the environment is created you can activate it using
> conda activte \<name of environment>

> conda activate rasa

After activating the environment you can install rasa by using
    
    > python -m pip install --upgrade pip  # to upgrade the pip version
    > pip install rasa

To check that rasa is working or not you can run the below command
> rasa --version

** note if you get some error related to `sanic` you can run the below command to resolve it
> pip install sanic==21.9.3

Now you are ready with all the required dependencies. Let's now see how you can train the model.

### To train model
you can train your model using below command
> rasa train

### To talk to bot in shell we need to run following two commands in parallel
    > rasa shell
    > rasa run actions
rasa shell will provide us with a command line prompt using which we can have conversation with the bot.

### To see bot working locally with UI
we need first run the following to commands in parallel.
    
    > rasa run -m models --enable-api --cors "*" 
    > rasa run actions
After running the above commands. The next step is to open the <b>index.html</b> file in browser.(index.html file is present with the source code)

### Note - If Got an error like "you must install a WebSocket server that is compatible with your async mode to enable it."
    > pip install gevent-websocket
    > pip install eventlet

### Note - If issue still persists
    > pip install sanic==21.6.0
    > pip install Sanic-Cors==1.0.0
    > pip install sanic-routing==0.7.0

## Workflow of the project

There are multiple important things to note in order to understand the workflow.

- The `data` directory contains the nlu data and these nlu files are divided into different batchs. Named as `nlu-faq-agri-wheat-b0.yml` for each batch file there is a domain file too.
- The `domain-grp` directory contains batched files corresponding to the nlu files.
- When new data for nlu and domian is added to the above described directories we have to execute the `build-domain.py` script which will make sure that all the responses are being considered by rasa while training.

### Process followed
1. First using the s-bert transformer we narrow down the number of unique questions based on sentence similarity.
2. Using the unique sentences from above step we compare the new sentences with already added data to get questions which are not yet ingested in the model (Levenshtein Distance is used for the comparison here).
3. With the help of T-5 transformer we get parapharse examples for each unique question
4. Generate NLU and DOMAIN files
5. Execute 'build-domain.py`
6. Train model

Apart from these steps we are doing one addtional check by taking the top words and the words at a distance of 1 from these top words on both sides in sentence which helps in identifying which queryTypes have same questions.
