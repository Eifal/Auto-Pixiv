import random
import os

event_name = os.environ.get('GITHUB_EVENT_NAME')

if event_name == 'workflow_dispatch':
    should_run = True
else:
    should_run = random.random() < 0.3
    
with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"SHOULD_RUN={should_run}\n")
