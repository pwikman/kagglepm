import pandas as pd
import pickle

date_cut_off = 86

def main():

	print("Starting process!")
	df = pd.read_csv('Data/train.csv')
	mask = df.date > date_cut_off
	df = df[mask]
	pickle.dump(df,open('df_down_sampled.p','wb'))
	print("Process finished!")

if __name__ == "__main__":

	main()
