INPUT_FOLDER="/home/ubuntu/MetReTrim/data/fastq_files"
OUTPUT_FOLDER="/home/ubuntu/MetReTrim/results/barplots"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class PlotNucleotidePercentages:

    def extract_first_twenty_positions(self,input_folder,fastq_file):
        file_prefix=fastq_file.split(".")[0]
        count_list=[]
        with open("%s/%s"%(INPUT_FOLDER,fastq_file)) as fh:
            while True:
                info=fh.readline()
                if len(info)==0:
                    break
                seq=fh.readline().strip()
                fh.readline()
                fh.readline()
                seq_20=seq[:20]
                seq_20_list=list(seq_20)
                count_list.append(seq_20_list)

        df = pd.DataFrame(count_list)
        df.columns = [str(i) for i in range(20)]
        #print(df)
        return df,file_prefix

    def prepare_nucleotide_percentages_per_column(self,df):
        nucleotides = ['A', 'T', 'G', 'C']
        percentages = []
        for i in range(20):
            column = df[str(i)]
            counts = column.value_counts()
            perc = counts / column.count() * 100
            percentages.append(perc.reindex(nucleotides).fillna(0).tolist())

        percentages_df = pd.DataFrame(percentages, columns=nucleotides)
        percentages_df.index = range(20)
        #print(percentages_df)
        return percentages_df

    def plot_grouped_barplots(self,output_folder,percentages_df,file_prefix):
        sns.set_style("whitegrid")
        plt.figure(figsize=(10,6))
        width = 0.2
        for i, nucleotide in enumerate(["A", "T", "G", "C"]):
            plt.bar(percentages_df.index + (i - 1.5) * width, percentages_df[nucleotide], width=width)
        plt.xticks(percentages_df.index, range(1,21))
        plt.xlabel('Position on read')
        plt.ylabel('Percentage nucleotide per position')
        plt.ylim(0,100)
        plt.legend(['A', 'T', 'G', 'C'], loc='upper right')
        plt.tight_layout()
        plt.show()
        plt.savefig('%s/%s.pdf'%(output_folder,file_prefix), bbox_inches='tight')

    def main(self,input_folder,output_folder):
        for fastq_file in os.listdir(input_folder):
            df,file_prefix=self.extract_first_twenty_positions(input_folder,fastq_file)
            percentages_df=self.prepare_nucleotide_percentages_per_column(df)
            self.plot_grouped_barplots(output_folder,percentages_df,file_prefix)

if __name__=="__main__":
    plot_object=PlotNucleotidePercentages()
    plot_object.main(INPUT_FOLDER,OUTPUT_FOLDER)
