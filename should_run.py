import random
import os

should_run = random.random() < 0.1

with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"SHOULD_RUN={should_run}\n")
