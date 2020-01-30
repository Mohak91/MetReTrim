# MetReTrim

**Mohak Sharda**   
**v0.1**

***mohaks@ncbs.res.in***  
***sharda.mohak@gmail.com***

MetReTrim is a pipeline, written in python, for trimming heterogeneity 'N' spacers from the pre-processed reads given the primer sequences. It locates the primer sequence provided by a user in a given read and trims any length of the heterogenous spacer sequence towards the 5' end of the primer. It can be used for single-end and/or paired-end sequencing data.

## Installation

MetReTrim has been tested to work with the latest versions of Python 2 and Python 3. It only requires python to be installed on the system.

Users can check the version of python on their system using the following command via terminal:

```
python --version
```

#### Installation via pip


The current version of MetReTrim can be installed using the pip command on the terminal with the following syntax:

```
sudo pip install MetReTrim
```

or


For python version 2,

```
sudo python -m pip install MetReTrim
```

For python version 3,

```
sudo python3 -m pip install MetReTrim
```


In case pip is not installed on the system, it can installed using the following command:

```
sudo apt install pip
```

or


For python version 2,

```
sudo apt install python-pip
```

For python version 3,

```
sudo apt install python3-pip
```


#### Manual Installation

In case installation via pip doesn't work, users can download the MetReTrim executable directly from the github link: https://github.com/Mohak91/MetReTrim
Please make sure the executable is either in $PATH or users run the command line version of the executable from within the folder where it is present.

#### Installing dependencies

MetReTrim requires the following python packages to be installed for a successful run:

+ os
+ sys
+ subprocess
+ getopt
+ re
+ regex

Usually, all the above mentioned packages are pre-installed in all the python versions.

However regex needs to be installed separately on the system. It can be done using the following command:

For python version 2,

```
python -m pip install regex
```

For python version 3,

```
python3 -m pip install regex
```

## Running MetReTrim

#### Input

MetReTrim can be run as a command line tool on the terminal. It requires the following inputs to run:

+ Complete path of the folder containing the unprocessed fastq files in a .fastq.gz or .fastq format.
+ Complete path of the desired folder where the users wish the processed files to be stored.
+ Primer sequence(s) used in the experiment.

In case the users wish to keep the processed files in the same folder as the unprocessed files, the output folder path is not required.

By default, MetReTrim allows upto 3 mismatches in the primer sequence(s) provided by the user when locating it in the reads. This can be changed according to the user using the -m option. (See below)

By default, MetReTrim retains the primer sequence and just trims the heterogenous 'N' spacer sequence in the processed reads. Users can trim the primer sequence as well using the -k option. (See below)

#### Output

MetReTrim creates two sets of output files for a given .fastq file - trimmed and untrimmed. The trimmed fastq file will contain the reads where the heterogenous 'N' spacer sequence has been removed. The untrimmed fastq file will contain those reads for which the primer sequence provided couldn't be located on the reads and therefore couldn't be processed.

#### Usage

The usage of the command can be checked using the following command:

```
MetReTrim -h
```

It will output the following text on the terminal:

```
usage: MetReTrim [OPTIONS] -i INPUT -o OUTPUT -p PRIMER_SINGLE_END -f PRIMER_FORWARD -r PRIMER_REVERSE

Trim heterogenous 'N' spacer sequences from the 5' end of the pre-processed reads.

positional arguments:

-i, --ifolder
	Takes INPUT folder path. INPUT contains the fastq files to be processed.
	Fastq files can be in a .fastq format or .fastq.gz format.
	In case an output folder is not provided, the processed files will be created in INPUT.

-o, --ofolder
	Takes OUTPUT folder path as the desired directory to store the processed reads.
	In case OUTPUT doesn't already exist, the program creates OUTPUT first and then stores the processed files.

-p, --primer
	Takes PRIMER_SINGLE_END sequence if the read files have a single end sequencing read data.

-f, --primer1
	Takes PRIMER_FORWARD sequence as the forward primer sequence if the read files have a paired end sequencing read data.

-r, --primer2
	Takes PRIMER_REVERSE sequence as the reverse primer sequence if the read files have a paired end sequencing read data.


optional arguments:

-h
	Shows this help message and exit

-k, --keep
	Controls if primer sequence needs to be trimmed along with the 'N' heterogenous spacer sequence
	It can take either of the two options: 1) -k keep or, 2) -k unkeep
	Default: -k keep (retains the primer sequence in the reads)

-m, --mismatch
	Controls the number of mismatches to be allowed in the primer sequence(s) while locating them in the reads to be processed
	Default: -m 3 (locates primer sequences in the reads to be processed by allowing upto 3 mismatches)

NOTE:

1) In case the input folder has both single-end and paired-end read files, all the three -f -r and -p primer sequence options are required.
2) If using paired end reads, make sure the forward reads and reverse reads are segregated into two files.
3) Please provide the full and correct paths of the input and output folders.

Happy Trimming!! :)
```

#### Examples

If MetReTrim has been installed via pip or the executables are present in the global path $PATH, the command can be run directly with the name of the executable. For example, if want to check the usage, users can type:

```
MetReTrim -h
```

If users have downloaded the script from github (as mentioned above) and the script is being run from the folder where it is present, the command of the usage would be as follows:

```
./MetReTrim -h
```


Running MetReTrim for single end reads:

```
MetReTrim -i /abc/xyz/test/fastq -o /abc/xyz/test/output -p AATTTGCGATCGAGTCTAATCGAG
```

where,  '/abc/xyz/test/fastq' is the directory where all the pre-processed fastq files are present,
	'/abc/xyz/test/output' is the directory where all the processed fastq files will be stored after trimming,
	'AATTTGCGATCGAGTCTAATCGAG is the primer sequence used for single-end sequencing.

Running MetReTrim for paired end reads:

```
MetReTrim -i /abc/xyz/test/fastq -o /abc/xyz/test/output -f AATTTGCGATCGAGTCTAATCGAG -r ATCGACTGAGCATTATATTACGCG
```

where,  '/abc/xyz/test/fastq' is the directory where all the pre-processed fastq files are present,
        '/abc/xyz/test/output' is the directory where all the processed fastq files will be stored after trimming,
        'AATTTGCGATCGAGTCTAATCGAG' is the forward primer sequence used for paired-end sequencing,
	'ATCGACTGAGCATTATATTACGCG' is the reverse primer sequence used for paired-end sequencing.

Note: Paired-end reads should be segregated in two files - forward primer and reverse primer reads respectively.

Running MetReTrim for both single and paired-end reads together :

```
MetReTrim -i /abc/xyz/test/fastq -o /abc/xyz/test/output -p ACACACACTAGGCTACGTATGCCA -f AATTTGCGATCGAGTCTAATCGAG -r ATCGACTGAGCATTATATTACGCG
```

where,  '/abc/xyz/test/fastq' is the directory where all the pre-processed fastq files are present,
	'/abc/xyz/test/output' is the directory where all the processed fastq files will be stored after trimming,
	'AATTTGCGATCGAGTCTAATCGAG' is the forward primer sequence used for paired-end sequencing,
	'ATCGACTGAGCATTATATTACGCG' is the reverse primer sequence used for paired-end sequencing.
	'ACACACACTAGGCTACGTATGCCA' is the primer sequence used for single-end sequencing

Running MetReTrim for paired end reads and also removing the primer sequences along with the heterogenous 'N' spacer sequences:

```
MetReTrim -i /abc/xyz/test/fastq -o /abc/xyz/test/output -f AATTTGCGATCGAGTCTAATCGAG -r ATCGACTGAGCATTATATTACGCG -k unkeep
```

Running MetReTrim for paired end reads and allowing upto 5 mismatches (default: 3) in the primer sequence while locating in the reads:

```
MetReTrim -i /abc/xyz/test/fastq -o /abc/xyz/test/output -f AATTTGCGATCGAGTCTAATCGAG -r ATCGACTGAGCATTATATTACGCG -m 5
```

## Citing MetReTrim

... to be updated
