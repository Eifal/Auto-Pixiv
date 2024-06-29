import random

should_run = random.random() < 0.1
print(f"::set-output name=should_run::{should_run}")
