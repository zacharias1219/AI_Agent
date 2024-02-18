from dotenv import load_dotenv
import os
import pandas as pd

population = os.path.join('data','population.csv')
population_df = pd.read_csv(population)



load_dotenv()