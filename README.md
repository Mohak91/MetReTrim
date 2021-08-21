# MetReTrim

**Mohak Sharda**   
**v1.0**

***mohaks@ncbs.res.in***  
***sharda.mohak@gmail.com***

MetReTrim is a pipeline, written in python, for trimming heterogeneity 'N' spacers from the pre-processed reads given the primer sequences. It locates the primer sequence provided by a user in a given read and trims any length of the heterogenous spacer sequence towards the 5' end of the primer. It can be used for single-end and/or paired-end sequencing data.

As a test run, two files from paired-end sequencing have been included in the folder "metretrim_test". The command can be run on the folder, as given in the examples below, under the section for paired-end sequencing. It should generate a folder "metretrim_trim_output" with the processed files included in it. The primer sequences for both the read files are also included in the commmand presented in the examples.

## Installation

MetReTrim has been tested to work with the latest versions of Python 2 and Python 3. It only requires python to be installed on the system.

Users can check the version of python on their system using the following command via terminal:

```
python --version
```

#### Manual Installation

Users can download the MetReTrim executable directly from the github link: https://github.com/Mohak91/MetReTrim
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
./MetReTrim -h
```

It will output the following text on the terminal:

```
usage: ./MetReTrim [OPTIONS] -i INPUT -o OUTPUT -p PRIMER_SINGLE_END -f PRIMER_FORWARD -r PRIMER_REVERSE

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

If the script is being run from the folder where it is present, the command of the usage would be as follows:

```
./MetReTrim -h
```


Running MetReTrim for single end reads:

```
./MetReTrim -i ./metretrim_test -o ./metretrim_trim_output -p AATTTGCGATCGAGTCTAATCGAG
```

where,  './metretrim_test' is the directory where all the fastq files to be processed are present,
	'./metretrim_trim_output' is the directory where all the processed fastq files will be stored after trimming,
	'AATTTGCGATCGAGTCTAATCGAG' is the primer sequence used for single-end sequencing.

Running MetReTrim for paired end reads:

```
./MetReTrim -i ./metretrim_test -o ./metretrim_trim_output -f CCTACGGGNGGCWGCAG -r GACTACHVGGGTATCTAATCC
```

where,  './metretrim_test' is the directory where all the fastq files to be processed are present,
        './metretrim_trim_output' is the directory where all the processed fastq files will be stored after trimming,
        'CCTACGGGNGGCWGCAG' is the forward primer sequence used for paired-end sequencing,
	'GACTACHVGGGTATCTAATCC' is the reverse primer sequence used for paired-end sequencing.

Note: Paired-end reads should be segregated in two files - forward primer and reverse primer reads respectively.

Running MetReTrim for both single and paired-end reads together :

```
./MetReTrim -i ./metretrim_test -o ./metretrim_trim_output -p ACACACACTAGGCTACGTATGCCA -f CCTACGGGNGGCWGCAG -r GACTACHVGGGTATCTAATCC
```

where,  './metretrim_test' is the directory where all the fastq files to be processed are present,
	'./metretrim_trim_output' is the directory where all the processed fastq files will be stored after trimming,
	'CCTACGGGNGGCWGCAG' is the forward primer sequence used for paired-end sequencing,
	'GACTACHVGGGTATCTAATCC' is the reverse primer sequence used for paired-end sequencing.
	'ACACACACTAGGCTACGTATGCCA' is the primer sequence used for single-end sequencing

Running MetReTrim for paired end reads and also removing the primer sequences along with the heterogenous 'N' spacer sequences:

```
./MetReTrim -i ./metretrim_test -o ./metretrim_trim_output -f CCTACGGGNGGCWGCAG -r GACTACHVGGGTATCTAATCC -k unkeep
```

Running MetReTrim for paired end reads and allowing upto 5 mismatches (default: 3) in the primer sequence while locating in the reads:

```
./MetReTrim -i ./metretrim_test -o ./metretrim_trim_output -f CCTACGGGNGGCWGCAG -r GACTACHVGGGTATCTAATCC -m 5
```

## Install and Run via Docker

Note: It is recommended that the latest version (18 or more) of docker engine is installed on your system. There might be issues with the older versions of docker while running the images. [Read the docker documentation for more details.](https://docs.docker.com/release-notes/ "Docker docs")

#### Pull from dockerhub and run

Checkout the [tutorial video on how to run MetReTrim via Docker](https://drive.google.com/file/d/1FLLvFxyOuwzRIG2L4cI2RojTY4Gg6TAB/view?usp=sharing "Run metretrim via docker")

Run the command(s) on your terminal on the folder containing files to be processed (here **metretrim_test**). Here the example is shown for paired-end sequencing data. You are creating a workspace inside the container with the name **metretrim_files** (name it according to your wish) starting from the root. The folders **metretrim_test** and **metretrim_output** will be stored inside this folder inside the container.

```
sudo docker run --rm -d\
-v ${PWD}:/metretrim_files -ti \
--name metretrim_container \
mohaksharda/metretrim:1.0 \
-i /metretrim_files/metretrim_test \
-o /metretrim_files/metretrim_output \
-f CCTACGGGNGGCWGCAG \
-r GACTACHVGGGTATCTAATCC \
-m 5 \
-k unkeep
```

Optional: Removing **metretrim** image from the system, if desired

	```
	sudo docker rmi mohaksharda/metretrim:1.0
	```

## Install and Run via Singularity (recommended if MetReTrim needs to be run on remote server)

Make sure singularity is installed. For more details on how to install singularity and other features refer to its [documentation:](https://sylabs.io/docs/)


Checkout the [tutorial video on how to run MetReTrim via Singularity](https://drive.google.com/file/d/1ISqgPCuS8Z0_7-_nsy9wtHLVCEYUsnnH/view?usp=sharing "Run metretrim via singularity")

The image can be downloaded from dockerhub. The following command needs to be run on the system (e.g local system) with root privelages:

```
sudo singularity pull docker://mohaksharda/metretrim:1.0
```

The above command will pull the image from dockerhub and automatically convert it into .sif file (image format required to run with singularity).

The following command can be used to run MetReTrim using singularity from anywhere.

```
singularity run metretrim_1.0.sif -h
```

The above command prints out the usage for MetReTrim. To run MetReTrim on an input folder containing paired end read files (here named 'metretrim_test'), run the following command:

```
singularity run metretrim_1.0.sif \
-i ./metretrim_test \
-o ./metretrim_output \
-f CCTACGGGNGGCWGCAG \
-r GACTACHVGGGTATCTAATCC
```

## Citing MetReTrim

... to be updated
